import random 
>>> random.randint(1,9)
2   
>>> number=random.randint(1,9) 
>>> print(number)
2
>>> guess=input("Enter Your Guess Here")
Enter Your Guess Here1
>>> guess
'1'
>>> if guess==number:
...     print("Congratulations!")
...     break
... if not guess==number:
  File "<stdin>", line 4
    if not guess==number:
    ^
SyntaxError: invalid syntax
>>> guess
'1'
>>> if guess==number:
... ...     print("Congratulations!")
  File "<stdin>", line 2
    ...     print("Congratulations!")
    ^
IndentationError: expected an indented block
>>> if guess==number:
...     print("Congratulations!")
...     break
... 
  File "<stdin>", line 3
SyntaxError: 'break' outside loop
>>>   