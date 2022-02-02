import json


class FileReader:
    file = ""
    content = ""

    def __init__(self, file=""):
        with open(file, encoding='utf-8') as _file:
            self.content = json.load(_file)

    def sort_content(self):
        self.content.sort()
