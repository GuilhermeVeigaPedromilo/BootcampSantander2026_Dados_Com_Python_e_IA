while (True):
    print("\nChoose an option:")
    print("1- Basic Charts")
    print("2- Static Charts")
    print("3- Interactive Charts")
    print("4- Exit")

    option = 0
    
    try:
        option = int(input("> "))
    except ValueError:
        print("\nInvalid input, try again!\n")

    match option:
        case 1:
            from . import basic_charts
        case 2:
            from . import static_charts
        case 3:
            from . import interactive_charts
        case 4:
            print("\nFinishing this operation...\n")
            break
        case 0:
            continue
        case _:
            print("\nUnknown option, try again!\n")