class MyError(Exception):
    def __init__(self, value):
        self.value = value

try:
    raise MyError("An error occurred")
except MyError as e:
    print("Custom error occurred:", e.value)

