while (True):
    print("\nChoose an option:")
    print("1- NumPy Example")
    print("2- Pandas Example")
    print("3- Matplotlib Example")
    print("4- Exit")

    option = 0
    
    try:
        option = int(input("> "))
    except ValueError:
        print("\nInvalid input, try again!\n")

    match option:
        case 1:
            from . import numpy_example
        case 2:
            from . import pandas_example
        case 3:
            from . import matplotlib_example
        case 4:
            print("\nFinishing this operation...\n")
            break
        case 0:
            continue
        case _:
            print("\nUnknown option, try again!\n")