Paul Tielens s3612031
Laura Faas s3443159
Thom Ticheler s3696820

# Kobra

To run the program type:
make run
alternatively:
python3 Kobra.py < ".txt file" 

In token.py is a function that takes in a string of an equation of lambda calculus and makes an array of tokens based on this string. 
This array is then parsed in parser.py and put in an abstract syntax tree

Python stops by itself after 1000 doing the same recursive step.

makevar kan alleen maar variabelen maken van a-z en A-Z als deze allemaal bezet zijn, geen idee wat er gebeurd