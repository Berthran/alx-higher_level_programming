# Python with ALX-SE
## 0x00 Python - Hello World

This is a repository of the solutions to the `0x00. Python - Hello, World` student project of the ALX Software Engineering Programme.

The objective of this project is to learn and be able to explain clearly the following:
* Why Python programming is awesome
* Who created Python
* Who is Guido van Rossum
* Where does the name ‘Python’ come from
* What is the Zen of Python
* How to use the Python interpreter
* How to print text and variables using print
* How to use strings
* What are indexing and slicing in Python
* What is the official Python coding style and how to check your code with `pycodestyle`

Each task in the project is solved in either a script or a program file.

--------------------------------------------------------

### Shell Scripts

##### How to Run:
`./script_name` e.g `./101-compile`

| Scripts	  | Function	|
|:--------------| :-------- 	|
| 0-run		| runs a Python script |
| 1-run_inline	| runs Python code |
| 100-compile   | compiles a Python script file |

--------------------------------------------------------

### Python Scripts

##### How to Run:
`./script_name` e.g `./100-write.py`

| Scripts	  | Function	|
|:--------------| :-------- 	|
| 2-print.py	| prints exactly `"Programming is like building a multilingual puzzle`, followed by a new line|
| 3-print_number.py | completes this [source code](https://github.com/holbertonschool/0x00.py/blob/master/3-print_number.py) in order to print the integer stored in the variable number, followed by __Battery street__, followed by a new line |
| 4-print_float.py | complete this [source code](https://github.com/holbertonschool/0x00.py/blob/master/4-print_float.py) in order to print the float stored in the variable number with a precision of 2 digits. |
| 5-print_string.py | completes this [source code](https://github.com/holbertonschool/0x00.py/blob/master/5-print_string.py) in order to print 3 times a string stored in the variable str, followed by its first 9 characters. |
| 6-concat.py | completes this [source code](https://github.com/holbertonschool/0x00.py/blob/master/6-concat.py) to print __Welcome to Holberton School!__ |
| 7-edges.py | completes this [source code] to produce [this](https://github.com/Berthran/alx-higher_level_programming/blob/master/0x00-python-hello_world/images/7-edges_result.jpg) result |
| 8-concat_edges.py | completes this [source code](https://github.com/holbertonschool/0x00.py/blob/master/8-concat_edges.py) to print __object-oriented programming with Python__, followed by a new line. |
| 9-easter_egg.py | prints __“The Zen of Python”__, by TimPeters, followed by a new line. |
| 100-write.py |  prints exactly __and that piece of art is useful - Dora Korpar, 2015-10-19__, followed by a new line. |

--------------------------------------------------------

### Python Programs
| Program	  | Function	|
|:--------------| :-------- 	|
| 102-magic_calculation.py | does exactly the same as the [following Python bytecode](https://github.com/Berthran/alx-higher_level_programming/blob/master/0x00-python-hello_world/images/102-magic_result.PNG) |

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
| 10-check_cycle.c | checks if a singly linked list has a cycle in it |

##### How to run
To run this move the files `10-main.c` and `10-linked_lists.c` from the `test_for_10-check_cycle` folder to the parent folder. 

Then run this:

`gcc -Wall -Werror -Wextra -pedantic -std=gnu89 10-main.c 10-check_cycle.c 10-linked_lists.c -o cycle`


--------------------------------------------------------

### Author
Daniel Berthran
