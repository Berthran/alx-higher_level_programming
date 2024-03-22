## map()

The advantage of the lambda operator can be seen when it is used in combination with the map() function. map() is a function which takes two arguments:
r = map(func, seq)
map() applies the function func to all the elements of the sequence seq.

Before Python3, map() returns a list. With Python3, map() returns an iterator which can be casted to a list or tuple

A list of functions can also be mapped

F = map(lambda x: map_functions(x, family_of_functions), [2, 3, 4])
family_of_functions = (square, cube)
map(map_functions, family_of_functions)
 def map_functions(x, functions)

## filter()

filter(function, sequence)

filter out all the elements of a sequence "sequence", for which the function function returns True

## reduce
reduce(func, seq)

continually applies the function func() to the sequence seq. It returns a single value.

If seq = [ s1, s2, s3, ... , sn ], calling reduce(func, seq) works like this:

At first the first two elements of seq will be applied to func, i.e. func(s1,s2) The list on which reduce() works looks now like this: [ func(s1, s2), s3, ... , sn ]
In the next step func will be applied on the previous result and the third element of the list, i.e. func(func(s1, s2),s3)
