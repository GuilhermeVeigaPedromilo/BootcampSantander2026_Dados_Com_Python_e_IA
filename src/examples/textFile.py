# To read a file, use the method open("filename.extension", "mode")
# "Mode" is 'r' (Read); 'w' (Write - delete the old content); 'a' (Add content).

from datetime import date

class File:
    def __init__(self, filename: str):
        self.filename = filename
        self.path = './public/data/examples/'

    def getFilename(self):
        return self.filename

    def getPath(self):
        return self.path

    def setFilename(self, filename: str):
        self.filename = filename

    def createFile(self, complete_path: str):
        with open(f"{complete_path}.txt", "w") as file:
            file.write("Python has created this file\n")
            file.write(f"Created on {date.today()}\n")

    def openFile(self):
        complete_path = self.path + self.filename
        try:
            with open(f"{complete_path}.txt", 'r') as file:
                content = file.read()
                return content
        except FileNotFoundError:
            print("\nWarn: file not found. It will be create.\n")
            self.createFile(complete_path)
        finally:
            try:
                with open(f"{complete_path}.txt", 'r') as file:
                                content = file.read()
                print("The file has been created.")
            except FileNotFoundError:
                 print("\nThere is another error and cannot possible create the file.\n")

    def readFile(self, content): # Read All Content
        print("\nFile content:\n")
        print(content + "\n")

    def readFileRowByRow(self, content): # Read All Content Row By Row
        print("\nFile content:\n")
        for row in content:
             print(row.strip())
        print("\n")

    def replaceAllContent(self, newContent):
        with open(f"{self.path + self.filename}.txt", "w") as file:
            file.write(newContent)

    def writeContent(self, newContent):
         with open(f"{self.path + self.filename}.txt", "a") as file:
              file.write(newContent)

def WorkingWithTextFile():
    filename = ""
    filename = input("Enter the filename: ")
    newFile = File(filename)
    content = newFile.openFile()

    if content != None:
        while (True):
             option = 0
             print("You desire:")
             print("1- Read All File")
             print("2- Read File Row by Row")
             print("3- Replace All Content")
             print("4- Add a row at the end from file")
             print("5- Back to before options")

             option = int(input("> "))
             match option:
                    case 1:
                        newFile.readFile(content)
                    case 2:
                       newFile.readFileRowByRow(content)
                    case 3:
                        newContent = input("Enter the new content: ")
                        newFile.replaceAllContent(newContent)
                        content = newFile.openFile()
                    case 4:
                        newContent = input("Enter the new content: ")
                        newFile.writeContent(newContent)
                        content = newFile.openFile()
                    case 5:
                       print("\nFinishing this operation...\n")
                       break
                    case _:
                       print("\nUknown option, try again!\n")