while (True):
    print("\nChoose an option:")
    print("1- Regression")
    print("2- Classification")
    print("3- Clustering")
    print("4- Exit")

    option = 0
    
    try:
        option = int(input("> "))
    except ValueError:
        print("\nInvalid input, try again!\n")

    match option:
        case 1:
            from . import regression_example
        case 2:
            from . import classification_example
        case 3:
            # from . import interactive_charts
            continue
        case 4:
            print("\nFinishing this operation...\n")
            break
        case 0:
            continue
        case _:
            print("\nUnknown option, try again!\n")