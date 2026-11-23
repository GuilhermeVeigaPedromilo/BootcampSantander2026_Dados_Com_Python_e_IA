#imports
from src.examples.files.textFile import WorkingWithTextFile
from src.examples.files.csvFile import WorkingWithCsvFile
from src.examples.files.jsonFile import WorkingWithJsonFile

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
                print("\nChoose an example to run:")
                print("1- Read and Write in Text file")
                print("2- Read and Write in CSV file")
                print("3- Read and Write in JSON file")
                print("4- API Integration (Brasil API)")
                print("5- SQLite3 database integration")
                print("6- Using Data Analytcs Libs")
                print("7- Product data manipulation")
                print("8- Tips per Day Report (Pipeline)")
                print("9- Charts")
                print("10- Exit")
                program_example = 0

                try:
                    program_example = int(input("> "))
                except ValueError:
                    print("\nInvalid input, try again!\n")

                match program_example:
                    case 1:
                        WorkingWithTextFile()
                    case 2:
                        WorkingWithCsvFile()
                    case 3:
                        WorkingWithJsonFile()
                    case 4:
                        import src.examples.apis.apiIntegration
                    case 5:
                        import src.examples.databases.db_products
                    case 6:
                        import src.examples.data_analytcs_libs.example
                    case 7:
                        import src.examples.data_manipulation.products_manipulation
                    case 8:
                        import src.examples.automation.pipeline_example
                    case 9:
                        import src.examples.charts.charts_example
                    case 10:
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