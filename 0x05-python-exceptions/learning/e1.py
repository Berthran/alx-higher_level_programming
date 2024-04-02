while True:
        try:
            try:
                x = int(input("Please enter a number: "))
                print("Successful")
                break;
            except (TypeError, ValueError):
                print("Oops! That was no valid number. Try again...")
            except ValueError:
                print("Value error: provide an integer")
        except ValueError:
            print("Oops! That was no valid number. Try again...")
