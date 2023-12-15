#  ____  __.          ___.                      
# |    |/ _|   ____   \_ |__   _______  _____   
# |      <    /  _ \   | __ \  \_  __ \ \__  \  
# |    |  \  (  <_> )  | \_\ \  |  | \/  / __ \_
# |____|__ \  \____/   |___  /  |__|    (____  /
#         \/               \/                \/ 

Paul Tielens s3612031
Laura Faas s3443159
Thom Ticheler s3696820

The compiler versions and operating systems:
...
...
...

The program works correctly, has no known defects and there are no deviations from the assignment.

In token.py is a function that takes in a string of an equation of lambda calculus and makes an array of tokens based on this string. 
This array is then parsed in parser.py and put in an abstract syntax tree

Parser.py ...

Checker.py ...


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



