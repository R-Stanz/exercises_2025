adjacente(0,1).
adjacente(1,0).
adjacente(1,2).
adjacente(2,1).
adjacente(2,3). 
adjacente(3,2).
adjacente(2,4).
adjacente(4,2).
adjacente(4,5).
adjacente(5,4).

caminho([]).
caminho(X) :- path(X, P).
path([H|[]], P).
path([H|[Hs|T]], P) :- adjacente(H,Hs), path([Hs|T], P).

grau(X, W) :-
    findall(Y, adjacente(X, Y), Vizinhos), 
    length(Vizinhos, W).
