import json
import csv
import os

class File():
    """File object."""
    def __init__(
        self, #FILE_NAME
    ):
        #self.file = FILE_NAME
        # GETing Curent Working Directory.
        self.PATH = os.getcwd()

    def is_exist(self, _pathToFile) -> bool:
        """Return True if file exists, otherwise False."""
        if os.path.exists(_pathToFile): #in os.listdir(self.PATH):
            return True # file exists.
        else:
            return False # file does not exist.

    def create(self, _pathToFile):
        """
        If file does not exist - create it, otherwise return an Error.
        A string argument should not contain ~ or $HOME due to error.
        """
        try:
            open(_pathToFile, "x")
        except FileExistsError:
            raise "File already exists!"

    def delete(self, _pathToFile):
        """Delete file from computer permanently."""
        if os.path.exists(_pathToFile):
            os.remove(_pathToFile)
        else:
            raise "File does not exist!"

    def is_json(self, _pathToFile) -> bool:
        """Return True if file is *.json, otherwise False."""
        try:
            with open(_pathToFile, "r+") as file:
                json.load(file)
        except json.decoder.JSONDecodeError:
            return False # file is not *.json.
        else:
            return True # file is *.json.

    def is_empty(self, _pathToFile) -> bool:
        """Return True if file is empty, False if not, None if file not exist."""
        try:
            if os.path.isfile(_pathToFile) and os.path.getsize(_pathToFile) == 0:
                return True # file is empty.
        except FileNotFoundError:
            return None # file does not exist.
        if os.path.isfile(_pathToFile) and os.path.getsize(_pathToFile) > 0:
            return False # file is not empty.

    def dump_to_json(self, _data:dict, _pathToFile:str, _indent:int=4):
        """Dump data to *.json file."""
        with open(_pathToFile, "r+") as file:
            json.dump(_data, file, indent=_indent)

    def dump_template_to_json(self, _pathToFile:str, _template:dict, _indent:int=4):
        """Dump template if file is not empty."""
        if is_empty(_pathToFile) == False:
            pass # file is not empty.
        else:
            # Creating template for *.json file.
            with open(_pathToFile, "r+") as file:
                json.dump(_template, file, indent=_indent)

    def load_from_json(_pathToFile:str) -> dict:
        """"""
        with open(_pathToFile, "r+") as file:
            data = json.load(file)
        return data

    def convert_from_csv_to_json(self, _pathToCSV, _pathToJSON, _primaryColumn):
        """Convert CSV file to JSON."""
        data = dict()
        # Open CSV reader.
        with open(_pathToCSV, encoding="utf-8") as csvFile:
            csv = csv.DictReader(csvFile)
            # Convert each row into a dictionary and add it to json.
            for row in csv:
                key = rows[primary_column]
                data[key] = row
        # Dumping data to JSON.
        with open(_jsonFileName, "w", encoding="utf-8") as jsonFile:
            jsonFile.write(json.dumps(data, indent=4))


#    def append_to_list_in_json_file(self, first_key, second_key):
#        """"""
#        with open(self.file, "r+") as file:
#            data = json.load(file)
#            data[first_key].append(second_key[first_key][0])
#            file.seek(0)
#            json.dump(data, file, indent=4)
