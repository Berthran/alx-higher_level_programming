errors are problems that arise before the program starts running.
Exceptions, on the other hand, occur during the execution of a program. They are unexpected events that disrupt the normal flow of the program.

You should use an exception whenever you anticipate that a certain block of code might raise an error during its execution.

Enclose the code that might raise the exception inside a `try` block, and then use one or more except blocks to specify how to handle the differenct types of exceptions that might occur.

The purpose of catching exceptions is to gracefully handle errors and prevent your program from crashing. 

You can raise a built-in exception using the `raise` keyworkd followed by the type of exception you want to raise.

A clean-up action is required after an exception if the code perfroms operateions that need to be properly cleaned up or closed, such as closing files, releasing resources, or rolling back database transactions. A `finally` block is used to ensure that the clean-up action is always executed, regardless of whether an exception occurs or not.

1. A `try` block can have more than one except clause to handle different exception types. The first matching except clause is triggered.
2. If the exception occurs which does not match the namee exception clause, it is passed to the outer try statements.
3. An `except` clause can name multiple exceptions as a tuple
4. A class in an `except` clause is compatible with an exception if it is the same class or a base class thereof
