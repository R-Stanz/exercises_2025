adiciona(X, L1, [X|L1]).

apaga(X, [], []).    
apaga(X, [X | L], L1) :- apaga(X, L, L1).
apaga(X, [Y | L], [Y|L1]) :-
    apaga(X, L, L1).

concatena([], [], []).
concatena([], [X|L2], [X|L3]) :-
    concatena([], L2, L3).
concatena([X|L1], L2, [X|L3]) :-
    concatena(L1, L2, L3).

membro(X,[X|L]) :- !.
membro(X,[_|L]) :- membro(X,L).

comprimento(0, []).
comprimento(X,[H|L]) :- 
    comprimento(Y,L), 
    X is Y+1.
