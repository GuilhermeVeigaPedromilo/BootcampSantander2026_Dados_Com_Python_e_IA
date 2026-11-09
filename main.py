#imports
from examples.textFile import ReadingTextFile

print("Hello World! This isn't my first program in Python\n")

while (True):
    print("Choose an option to access contents of this reposiroty:")
    print("1- Access examples.")
    print("2- Access projects.")
    print("3- Exit")

    option = 0
    try:
        option = int(input("> "))
    except ValueError:
        print("\nInvalid input, try again!\n")
    
    match option:
        case 1:
            while (True):
                print("\nChoose a example to run:")
                print("1- Read and Write in Text file")
                print("2- Exit")
                program_example = 0

                try:
                    program_example = int(input("> "))
                except ValueError:
                    print("\nInvalid input, try again!\n")

                match program_example:
                    case 1:
                        ReadingTextFile()
                    case 2:
                        print("\nFinishing this operation...\n")
                        break
                    case 0:
                        continue
                    case _:
                        print("\nUknown option, try again!\n")
        case 2:
            print("\nHi")
        case 3:
            print("\nFinishing your execution...")
            break
        case 0:
            continue
        case _:
            print("\nUknown option, try again!\n")