#!/usr/bin/python3
import hidden_4

def main():
    namespace = dir(hidden_4)
    no_of_names = len(namespace)
    for i in range(no_of_names):
        print("{}".format(namespace[i]))

if __name__ == "__main__":
    main()
