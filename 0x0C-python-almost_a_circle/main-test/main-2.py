#!/usr/bin/python3
""" 2-main """
from models.rectangle import Rectangle

if __name__ == "__main__":

    try:
        print("Trying block 1\n=============")
        r1 = Rectangle("10", 2)
        print(r1.width)
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))

    try:
        print("\nTrying block 2\n=============")
        r = Rectangle(0, "2")
        print(r.width, r.height)
        r.width = -10
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))

    try:
        print("\nTrying block 3\n=============")
        r = Rectangle(10, 2, -1)
        print("width: ", r.width, "height: ", r.height)
        r.x = {}
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))

    try:
        print("\nTrying block 4\n=============")
        Rectangle(10, 2, 3, "1")
        print("width: ", r.width, "height: ", r.height)
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))
