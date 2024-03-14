#!/usr/bin/python3
import hidden_4


def main():
    namespace = dir(hidden_4)
    no_of_names = len(namespace)
    for name in namespace:
        if name.startswith("_") is False:
            print("{}".format(name))


if __name__ == "__main__":
    main()
