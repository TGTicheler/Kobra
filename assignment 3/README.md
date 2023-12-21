#  ____  __.          ___.                      
# |    |/ _|   ____   \_ |__   _______  _____   
# |      <    /  _ \   | __ \  \_  __ \ \__  \  
# |    |  \  (  <_> )  | \_\ \  |  | \/  / __ \_
# |____|__ \  \____/   |___  /  |__|    (____  /
#         \/               \/                \/ 

Paul Tielens s3612031
Laura Faas s3443159
Thom Ticheler s3696820
Concepts of Programming Languages, 2023

The compiler versions and operating systems:
...
...
...

The program works correctly, has no known defects and there are no deviations from the assignment.

In token.py is a function that takes in a string of an equation of lambda calculus and makes an array of tokens based on this string. 
This array is then parsed in parser.py and put in an abstract syntax tree

Parser.py takes in an array of tokens and makes this into an abstract syntax tree. The tree is made by going a recursive descent through the LL grammar. While doing this the ast is built. The resulting output is the root of this ast. It exits the programm when there is an error.
Types are given to variables by being assigned as their left child.

The LL grammar that is used:
⟨judgement⟩ ::= ⟨expr⟩ ':' ⟨type⟩
⟨expr⟩ ::= ⟨lexpr⟩ ⟨expr'⟩
⟨expr'⟩ ::= ⟨lexpr⟩ ⟨expr'⟩ | Empty
⟨lexpr⟩ ::= ⟨pexpr⟩ | '\' ⟨var⟩ ⟨lexpr⟩
⟨pexpr⟩ ::= ⟨var⟩ | '(' ⟨expr⟩ ')'

⟨type⟩ ::= ⟨uvar⟩ ⟨type'⟩ | '(' ⟨type⟩ ')' ⟨type'⟩ 
⟨type'⟩ ::=  '->' ⟨type⟩ | Empty

To Checker.py the rast root of a judgement is given. From this judgement, the expresson is taken and the type is derived from this expression. Then the derived type and the given type are compared and checked if they are the same.




