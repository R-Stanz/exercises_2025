from fastapi import FastAPI, Request
from classes.Clinic import Clinic
from pydantic import BaseModel
from typing import Optional
from time import localtime

clinic = Clinic("H2A", "Fiances's St.", "9829121")
clinic.add_doctor("Joseph Joestar", "922321-NY", "11-02-1911", "general")
clinic.add_doctor("John Galt", "72353-NV", "31-08-1920", "psychiatry")
clinic.add_doctor("John Savage", "777-KS", "02-02-2002", "psychiatry")

class DoctorCreate(BaseModel):
    full_name: str
    license_code: str
    birthdate: str
    speciality: str

    def params(self):
        return [self.full_name, self.license_code, 
                self.birthdate, self.speciality]

class DoctorOptional(DoctorCreate):
    full_name: Optional[str] = None
    license_code: Optional[str] = None
    birthdate: Optional[str] = None
    speciality: Optional[str] = None

app = FastAPI()

@app.get("/")
async def home():
    return {"msg": "An API to access a clinic object!",
            "clinic": clinic
    }

@app.get("/health-check")
async def health_check():
    time = localtime()
    return f"Server time: {time.tm_hour}:{time.tm_min}:{time.tm_sec} - OK" 

@app.get("/doctors")
async def list_doctors():
    return clinic.doctors

@app.post("/doctors")
async def add_doctor(new_doctor: DoctorCreate):
    return clinic.add_doctor(*new_doctor.params())


@app.get("/doctors/{doctor_license}")
async def get_doctor(doctor_license: str):
    return clinic.doctor_by_license(doctor_license)

@app.delete("/doctors/{doctor_license}")
async def del_doctor(doctor_license: str):
    return {
            "msg": f"Removed {doctor_license}",
            "removed_doctor": clinic.rm_doctor_by_license(doctor_license)
    }

@app.put("/doctors/{doctor_license}")
async def update_doctor(doctor_license: str, new_doctor: DoctorCreate):
    return {
            "msg": f"Updated {doctor_license}",
            "updated_doctor": clinic.update_doctor_by_license(*new_doctor.params())
    }

@app.patch("/doctors/{doctor_license}")
async def partial_update_doctor(doctor_license: str, new_doctor: DoctorOptional):
    new_doctor.license_code = doctor_license

    doctor = clinic.doctor_by_license(doctor_license)
    doctor_model = DoctorCreate(**doctor.dict())
    update_data = new_doctor.dict(exclude_unset=True)
    updated_doctor = doctor_model.copy(update=update_data)
    return {
            "msg": f"Updated {doctor_license}",
            "updated_doctor": clinic.update_doctor_by_license(*updated_doctor.params())
    }
