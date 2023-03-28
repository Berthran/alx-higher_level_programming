#!/usr/bin/python3

def list_division(my_list, my_list_2, list_length):
    ''' A function that performs element-wise division
    on two lists '''
    new_list = []

    for i in range(list_length):
        ans = 0
        try:
            ans = my_list[i] / my_list_2[i]
        except TypeError:
            print("wrong type")
        except ZeroDivisionError:
            print("division by 0")
        except IndexError:
            print("out of range")
        finally:
            new_list.append(ans)
    return (new_list)
