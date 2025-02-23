progenitor(jose, joao).
progenitor(jose, ana).
progenitor(maria, joao).
progenitor(maria, ana).
progenitor(ana, helena).
progenitor(ana, joana).
progenitor(joao, mario).
progenitor(helena, carlos).
progenitor(mario, carlos).

mulher(maria).
mulher(ana).
mulher(helena).
mulher(joana).

homem(jose).
homem(joao).
homem(mario).
homem(carlos).


:- dynamic encontrados/2.

% Irmaos
irmaos(A, B) :-
    progenitor(X, A),
    progenitor(X, B),
    A \= B,
    \+ encontrados(A, B),
    assertz(encontrados(A, B)).

limpar_encontros :-
    retractall(encontrados(_, _)).


irma(A,B) :- irmaos(A,B),
    mulher(A).

irmao(A,B) :- irmaos(A,B),
    homem(A).


% Pais
mae(A,B) :- progenitor(A,B), mulher(A).
pai(A,B) :- progenitor(A,B), homem(A).


% Avos
avos(A,B) :- progenitor(A,C), progenitor(C,B).

mae_de_um_progenitor(A,B) :- avos(A,B),
    mulher(A).

pai_de_um_progenitor(A,B) :- avos(A,B),
    homem(A).


% Tios
tios(A,B) :- progenitor(D,A),
    progenitor(C,B), 
    progenitor(D,C).

tia(A,B) :- tios(A,B),
    mulher(A).

tio(A,B) :- tios(A,B),
    homem(A).


% Primos
primos(A,B) :- avos(C,A), 
    avos(C,B),
    A \= B,
    \+ irmaos(A,B),
    \+ encontrados(A, B),
    assertz(encontrados(A, B)).

prima(A,B) :- primos(A,B),
    mulher(A).

primo(A,B) :- primos(A,B),
    homem(A).


% Descendente
:- dynamic ancestrais_encontrados/3.

descendente(A,B) :- (progenitor(B,A);
    (progenitor(C,A), progenitor(B,C));
    (progenitor(C,A), descendente(C,B))),
    \+ ancestrais_encontrados(A, B, C),
    assertz(ancestrais_encontrados(A, B, C)).

limpar_ancestrais :-
    retractall(ancestrais_encontrados(_, _, _)).
