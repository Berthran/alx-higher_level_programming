import sys

try:
    f = open('myfile.txt')
    s = f.readline()
    i = int(s.strip())
except OSError as err:
    print("OS error:", err)
except Exception as err:
    print(f"Unexpected {err=}, {type(err)=}")
    raise
