#  ____  __.          ___.                      
# |    |/ _|   ____   \_ |__   _______  _____   
# |      <    /  _ \   | __ \  \_  __ \ \__  \  
# |    |  \  (  <_> )  | \_\ \  |  | \/  / __ \_
# |____|__ \  \____/   |___  /  |__|    (____  /
#         \/               \/                \/ 

Paul Tielens s3612031
Laura Faas s3443159
Thom Ticheler s3696820
Group number: ...
Class number: ...

Compiler Versions and operating systems:
...
...


The program works correctly, has no known defects and there are no deviations from the assignment.

To run the program type:
make run
alternatively:
python3 Kobra.py ".txt file" 

In token.py is a function that takes in a string of an equation of lambda calculus and makes an array of tokens based on this string. 
This array is then parsed in parser.py and put in an abstract syntax tree

Parser.py

In reductions.py a correct ast is put in the class reduce, which looks for ((\x M) N) and then reduces it to M[x:=N].
This is done by going through the ast and looking for ((\x M) N) (seekBeta()), then the program checks if any variable of N is bound in M.
If this is the case then these variables in M will be renamed. When this is done, every instance of x in M will be replaced with N and  ((\x M) N) is replaced with M[x:=N].

Python stops by itself after 1000 doing the same recursive step.

MakeVar can only make variablenames with a single letter.

The program does not support a dot after the lambda abstraction or anywhere else.

Reduction strategy:
The program reduces the equation from left to right.
The reduction strategy cannot be configured differrently by the command line. 