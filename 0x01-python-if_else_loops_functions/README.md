# Python with ALX-SE
## 0x01 Python - if/else, loops and functions

This is a repository of the solutions to the `0x01. Python - if\else, loops, functions` student project of the ALX Software Engineering Programme.

The objective of this project is to learn and be able to explain clearly the following:
* Why indentation is so important in Python
* How to use the if, if ... else statements
* How to use comments
* How to affect values to variables
* How to use the while and for loops
* How is Python’s for different from C‘s?
* How to use the break and continues statements
* How to use else clauses on loops
* What does the pass statement do, and when to use it
* How to use range
* What a function is and how do you use functions
* What does return a function that does not use any return statement
* Scope of variables
* What’s a traceback
* What are the arithmetic operators and how to use them


Each task in the project is solved in either a script or a program file.

--------------------------------------------------------

### Python Scripts

##### How to Run:
`./script_name` e.g `./1-last_digit.py`

| Scripts	  | Function	|
|:--------------| :-------- 	|
| 0-positive_or_negative.py	| handles [source code](https://intranet.alxswe.com/rltoken/rkvoXPA-lS3TAaemM9sChg) to determine the state of a random number |
| 1-last_digit.py | handles [source code](https://intranet.alxswe.com/rltoken/hU682hcMxVchqWAcmh32tA) to determine if the state of the last digit of a random number  |
| 2-print_alphabet | prints the ASCII alphabet, in lowercase, not followed by a new line. |
| 3-print_alphabet | prints the ASCII alphabet, in lowercase, not followed by a new line. |
| 4-print_hexa.py | prints all numbers from 0 to 98 in decimal and in hexadecimal |
| 5-print_comb2.py | prints numbers from 0 to 99. |
| 6-print_comb3.py | prints all possible different combinations of two digits. |
| 100-print_tebahpla.py | prints the ASCII alphabet, in reverse order, alternating lowercase and uppercase (z in lowercase and Y in uppercase) , not followed by a new line. |
| 101-remove_char_at.py | creates a copy of the string, removing the character at the position `n` |

--------------------------------------------------------

### Python Programs
| Program	  | Function	|
|:--------------| :-------- 	|
| 7-islower.py | checks for lowercase character. |
| 8-uppercase,py | prints a string in uppercase followed by a new line. |
| 9-print_last_digit.py | prints the last digit of a number. |
| 10-add.py |  adds two integers and returns the result. |
| 11-pow.py | computes `a` to the power of `b` and return the value. |
| 12-fizzbuzz.py | prints the numbers from 1 to 100 separated by a space. |
| 102-magic_calculation.py | does exactly the same as the [following Python bytecode](https://github.com/Berthran/alx-higher_level_programming/blob/master/0x01-python-if_else_loops_functions/images/102-magic_result_2.PNG.jpg) |

##### How to run
```
>>> magic_calc = __import__("102-magic_calculation").magic_calculation
>>> import dis
>>> dis.dis(magic_calc) # This shows the bytecode in a human readable form corresponding to that shown above
```

--------------------------------------------------------

### C Programs
| Program	  | Function	|
|:--------------| :-------- 	|
| 13-insert_number.c |  inserts a number into a sorted singly linked list. |

##### How to run
To run this move the files `13-main.c` and `linked_lists.c` from the `for_13-insert_number` folder to the parent folder. 

Then run this:

`gcc -Wall -Werror -Wextra -pedantic -std=gnu89 13-main.c 13-insert_number.c linked_lists.c -o insert`

`./insert`


--------------------------------------------------------

### Author
`Daniel Berthran`
