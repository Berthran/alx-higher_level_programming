# doctest - How it works

## Which docstrings are examined by doctest module?
The doctest looks for interactive examples in the following docstrings:
* module docstring
* function docstring
* class and its method's docstring

Object's imported into the module are not searched

## How interactive examples are recognised by doctest
* The doctest module searches for pieces of text that look like interactive Python sessions.
	>>> # comments are ignored
	>>> x = 12
* Any expected output must immediately follow the final '>>> ' or '... ' line containing the code,
	>>> x
	12
* and the expected output (if any) extends to the next '>>> ' or all-whitespace line.
	>>> if x == 13:
	...     print("yes")
	... else:
	...     print("no")
	...     print("NO")
	...     print("NO!!!")
	...
	no
	NO
	NO!!!
	>>>
* If expected output does contain a blank line, put <BLANKLINE> in your doctest example each place a blank line is expected.
	>>> if 1:
  	...    print('a')
  	...    print()
  	...    print('b')
 	 a
  	<BLANKLINE>
  	b
* All hard tab characters are expanded to spaces 
	(hard tabs are the equivalent of using the tab key to tab your code while 
	soft tabds are spaces added in to emulate a tab either manually or via a 
	code editor like Sublime Text) 
* using 8-column tab stops. If the code output includes hard tabs, the only way the doctest can pass is if the NORMALIZE_WHITESPACE option or directive is in effect.
	example.py
	>>> print("Hello\tWorld")
	Hello	World
	
	>>> # This fails
	>>> python3 -m doctest example.py -v
	>>> # This works
	>>> python3 -m doctest -o NORMALIZE_WHITESPACE example.py -v
* Preserve your backslashes exactly as you type them using a raw string of double backlashes
	>>> def f(x):
	... 	r'''Backslashes in a raw docstring: m\n'''
	Or
	... def f(x):
	...	'''Backslashes in a raw docstring: m\\n'''
 

## What execution context does doctest uses?
* By default, each time doctest finds a docstring to test, it uses a shallow copy of module‘s globals. It does this so that:
	* running tests doesn’t change the module’s real globals
	* one test in the module can’t leave behind crumbs that accidentally 
	  allow another test to work.
You can force use of your own dict as the execution context by passing globs=your_dict to testmod() or testfile() instead.


## How does doctest handle exceptions
A traceback comprises of a traceback header, traceback stack and the line(s) containing the exception type and detail. 
* The best practice is to omit the traceback stack (using ellipsis), unless it adds significant documentation value to the example.

## doctest option flags
