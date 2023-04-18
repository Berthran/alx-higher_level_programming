# doctest - Introduction and Usage


## Introduction to doctest
The doctest module searches for pieces of text that look like interactive Python sessions, and then executes those sessions to verify that they work exactly as shown.

doctests can be used to:
* check that the interactive examples still work as documented
* check that the interactive examples from a test file or test object work as expected
* write tutorial documentation for a package, liberally illustrated with input-output examples

For a simple example:
1. Create a Python script "example.py" containing a function.
2. Write the doctest alongside the function's documentation (docstring)
3. Run the Python script using the -v flag to see a detailed log of the testing process carried out by the Python's doctest module.
 	>>> python3 exmaple.py -v

There are many examples of doctests in the standard Python test suite and libraries.
Especially useful examples can be found in the standard test file Lib/test/test_doctest.py.


## Checking examples in docstrings
To do this you will have to end the module with this code
	if __name__ == "__main__":
    		import doctest
    		doctest.testmod()


The module can then be run as a script: 
1. which displays nothing unless an example fails, in which case the failing example(s) and the cause(s) of the failure(s) are printed to stdout.
	>>> python3 example.py

2. which displays a detailed report of all examples tried to stdout along with assorted summaries at the end using two methods:  
* the -v flag is passed
	>>> python3 example.py -v 
* the verbose parameter is set to True in which case passing the -v flag has no effect.
	if __name__ == "__main__":
    		import doctest
    		doctest.testmod(verbose=True)

If the module does not import the doctest module in its program, it can be done interactively on the command line using the -m flag.
	>>> python3 -m doctest -v examply.py
	>>> python3 -m doctest examply.py -v

## Checking examples in text file
To do this you will have to end the module with this code
	if __name__ == "__main__":
    		import doctest
    		doctest.testfile("example.txt")

* The testfile script executes and verifies any interactive Python examples contained n the text file. 
* The file doesn't need to contain a Python program. 
* The testfile() works similarly like the testmod() function. 
* By default, testfile() looks for files in the calling module's directory.

Ways to run (assuming example.py ends with doctest.testfile("filename.txt"))
	>>> python3 example.py [if doctest is imported in python file]
	>>> python3 example.py -v [to display detailed report]
	>>> python3 -m doctest -v example.txt [if doctest is not imported]

## END
