#!/usr/bin/python3
import calculator_1


def main():
    a = 10
    b = 5
    add = calculator_1.add
    sub = calculator_1.sub
    mul = calculator_1.mul
    div = calculator_1.div
    print("a + b = {}".format(add(a, b)))
    print("a - b = {}".format(sub(a, b)))
    print("a * b = {}".format(mul(a, b)))
    print("a / b = {}".format(div(a, b)))


if __name__ == "__main__":
    main()
