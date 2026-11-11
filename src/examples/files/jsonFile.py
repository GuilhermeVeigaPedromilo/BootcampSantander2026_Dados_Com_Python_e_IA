import json

class JsonFile:
    PATH = './public/data/examples/'
    EXTENSION = '.json'

    def __init__(self, filename: str):
        self.filename = filename
        self.complete_path = self.PATH + self.filename + self.EXTENSION

    def getFilename(self):
        return self.filename

    def getCompletePath(self):
        return self.complete_path

    def createFile(self, content):
        with open(self.complete_path , "w") as file:
            json.dump(content, file)

    def loadFile(self):
        with open(self.complete_path, "r") as file:
            return json.load(file)

    def readFile(self):
        data = self.loadFile()
        for row in data:
            print(row)

def WorkingWithJsonFile():
    data = [
        {
            "customer_name": "Quiet",
            "company": "?",
            "locate": "?",
            "total_purchases": 234
        },
        {
            "customer_name": "Venom Snake",
            "company": "Diamond Dogs",
            "locate": "Mother Base on Indian Ocean",
            "total_purchases": 4324
        },
        {
            "customer_name": "Ocelot",
            "company": "Diamond Dogs",
            "locate": "Mother Base on Indian Ocean",
            "total_purchases": 7324
        },
        {
            "customer_name": "Skull Face",
            "company": "XOF",
            "locate": "?",
            "total_purchases": 17324
        }
    ]

    newFile = JsonFile("customers")
    newFile.createFile(data)
    
    print("\nInitial content:\n")
    newFile.readFile()