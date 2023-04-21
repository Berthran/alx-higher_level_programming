# Notes on Unittest Module

## Brief introduction to Unittest Module
Unittest uses methods created in classes to manage tests.
Performing tests using the unittest framework allows us to test our code in an object-oriented approach. It supports many features such as test automation, setup, and code test teardown. 


The crux of each test is a call to 
* `assertEqual()`: to check for an expected result 
* `assertTrue() or assertFalse()`: to verify a condition, or 
* `assertRaises()`: to verify that a specific exception gets raised.

Two other methods are mostly used which allows the prorammer to define instructions that will be executed:
* before each test method [`setUp()`]
* after each test method [`tearDown()`]

## Using Unittest from the CLI
The unittest module can be used from the command line to run tests from:
* Modules
	python -m unittest test_module1 test_module2
* Classes
	python -m unittest test_module.TestClass
* Individual test methods
	python -m unittest test_module.TestClass.test_method
