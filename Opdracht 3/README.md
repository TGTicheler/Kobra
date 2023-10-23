Paul Tielens s3612031
Laura Faas s3443159
Thom Ticheler s3696820

# Kobra

In token.py is a function that takes in a string of an equation of lambda calculus and makes an array of tokens based on this string. 
This array is then parsed in parser.py and put in an abstract syntax tree

Python stops by itself after 1000 doing the same recursive step.


The Backus-Naur grammar that is used:
⟨judgement⟩ ::= ⟨expr⟩ ':' ⟨type⟩
⟨expr⟩ ::= ⟨lvar⟩ | '(' ⟨expr⟩ ')' | '\' ⟨lvar⟩ '^' ⟨type⟩ ⟨expr⟩ | ⟨expr⟩ ⟨expr⟩
⟨type⟩ ::= ⟨uvar⟩ | '(' ⟨type⟩ ')' | ⟨type⟩ '->' ⟨type⟩

⟨type⟩ ::= ⟨uvar⟩ | '(' ⟨type⟩ ')' | ⟨type⟩ '->' ⟨type⟩
⟨type⟩ ::=  '->' ⟨type⟩ | Empty


Voor mezelf:
⟨expr⟩ ::= ⟨var⟩ | '(' ⟨expr⟩ ')' | '\' ⟨var⟩ ⟨expr⟩ | ⟨expr⟩ ⟨expr⟩

(ook voor mezelf) LL:
⟨expr⟩ ::= ⟨lexpr⟩ ⟨expr'⟩
⟨expr'⟩ ::= ⟨lexpr⟩ ⟨expr'⟩ | Empty
⟨lexpr⟩ ::= ⟨pexpr⟩ | '\' ⟨var⟩ ⟨lexpr⟩
⟨pexpr⟩ ::= ⟨var⟩ | '(' ⟨expr⟩ ')'



