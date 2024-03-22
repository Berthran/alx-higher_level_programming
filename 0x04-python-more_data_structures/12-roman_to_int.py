#!/usr/bin/python3

def roman_to_int(roman_string):
    r_num = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    r_int = []
    if roman_string is None or type(roman_string) is not str:
        return (0)
    for i in roman_string:
        r_int.append(r_num[i])
    int_sum = r_int[0]
    for i in range(len(r_int) - 1):
        a = r_int[i]
        b = r_int[i + 1]
        if a >= b:
            int_sum += b
        else:
            int_sum += b - (2 * a)
    return (int_sum)
