#  ____  __.          ___.                      
# |    |/ _|   ____   \_ |__   _______  _____   
# |      <    /  _ \   | __ \  \_  __ \ \__  \  
# |    |  \  (  <_> )  | \_\ \  |  | \/  / __ \_
# |____|__ \  \____/   |___  /  |__|    (____  /
#         \/               \/                \/ 

Paul Tielens s3612031
Thom Ticheler s3696820
Laura Faas s3443159

This program works correctly, there aren't any known defects.
There aren't any deviations from the assignment. 

To run the program type:
make run
alternatively:
python3 Kobra.py ".txt file"

All the sentences with 'must' and 'should' are implemented.
The following sentences with 'may' are not implemented:
- The explanation about the format
- Every sentence with specifications about dot
- The output may use the least amount of whitespace and parenthese in its output
  
The Backus-Naur grammar that is used:
⟨expr⟩ ::= ⟨var⟩ | '(' ⟨expr⟩ ')' | '\' ⟨var⟩ ⟨expr⟩ | ⟨expr⟩ ⟨expr⟩

Explanantion (MAY):
In token.py is a function that takes in a string of an equation of lambda calculus, the grammar is listed above, and makes an array of tokens based on this string.
This array is then parsed in parser.py and put in an abstract syntax tree

The standard format (MAY):
A variable name is alphanumerical: it consists of the letters a-z, A-Z, or the digits 0-9. 
A variable starts with the letter from the Latin alphabet (not with a digit). 
Whitespaces are used to separate application of two variables. 'λ' is accepted instead of '\'.
If no parentheses are used, the order of presedence for the operators
is as follows: lambda abstraction groups more strongly than application. And application associates to the left. The program does not support a dot after the lambda abstracion variable or anywhere else.

