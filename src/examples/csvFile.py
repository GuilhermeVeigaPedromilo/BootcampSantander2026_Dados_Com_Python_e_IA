import csv

class CsvFile:
    PATH = './public/data/examples/'
    EXTENSION = '.csv'

    def __init__(self, filename: str):
        self.filename = filename
        self.complete_path = self.PATH + self.filename + self.EXTENSION

    def getFilename(self):
        return self.filename

    def getCompletePath(self):
        return self.complete_path

    def createFile(self, content):
        with open(self.complete_path, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(content)

    def readAllContent(self):
        data = []
        with open(self.complete_path, "r") as file:
            content = csv.reader(file)
            for row in content:
                    data.append(row)

        return data

    def appendAContent(self, data):
        with open(self.complete_path, "a", newline='') as file:
            writer = csv.writer(file)
            writer.writerow(data)

def WorkingWithCsvFile():
    header_data = ["name", "age", "city"]
    data = [
        header_data,
        ["Big Boss", 43, "Angola"],
        ["Venom Snake", 42, "Afheganistan"],
        ["Ryder", 38, "Detroit"]
    ]

    newData = ["Wander", 27, "Forbidden Lands"]

    newFile = CsvFile("newCsv")
    newFile.createFile(data)
    content = newFile.readAllContent()
    print("Initial content:\n")
    for row in content:
        print(row)
    newFile.appendAContent(newData)
    content = newFile.readAllContent()
    print("\nCurrently Content:\n")
    for row in content:
        print(row)

WorkingWithCsvFile()