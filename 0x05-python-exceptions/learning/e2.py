class CustomError(Exception):
    pass

class SpecificError(CustomError):
    pass

try:
    raise SpecificError("An error occured")
except CustomError:
    print("Caught CustomeError or its subclass")

