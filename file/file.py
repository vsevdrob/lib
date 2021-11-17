import json
import os

class File():
    """File object."""
    def __init__(
        self, FILE_NAME
    ):
        self.file = FILE_NAME
        # GETing Curent Working Directory.
        self.PATH = os.getcwd()

    def is_exist(self) -> bool:
        """Return True if file exists, otherwise False."""
        if self.file in os.listdir(self.PATH):
            return True # file exists.
        else:
            return False # file does not exist.

    def create(self):
        """If file exists - pass, otherwise create it."""
        if File.is_exist(self):
            pass # Checked: found file.
        else:
            open(self.file, "w") # Created new file.

    def delete(self):
        """Delete file from computer permanently."""
        os.system(f"rm {self.file}")

    def is_json(self) -> bool:
        """Return True if file is *.json, otherwise False."""
        try:
            with open(self.file, "r+") as file:
                json.load(file)
        except json.decoder.JSONDecodeError:
            return False # file is not *.json.
        else:
            return True # file is *.json.

    def is_empty(self) -> bool:
        """Return True if file is empty, False if not, None if file not exist."""
        try:
            if os.path.isfile(self.file) and os.path.getsize(self.file) == 0:
                return True # file is empty.
        except FileNotFoundError:
            return None # file does not exist.
        if os.path.isfile(self.file) and os.path.getsize(self.file) > 0:
            return False # file is not empty.

    def dump_to_json(self, _data:dict, _indent:int=None):
        """Dump data to *.json file."""
        with open(self.file, "r+") as file:
            json.dump(_data, file, indent=_indent)

    def dump_template_to_json(self, _template:dict, _indent:int=None):
        """Dump template if file is not empty."""
        if is_empty() == False:
            pass # file is not empty.
        else:
            # Creating template for *.json file.
            with open(self.file, "r+") as file:
                json.dump(_template, file, indent=_indent)

    def load_from_json(self) -> dict:
        """"""
        with open(self.file, "r+") as file:
            data = json.load(file)
        return data
    
    def convert_from_csv_to_json(self, _csvFilePath, _jsonFilePath, _primaryColumn):
        """Convert CSV file to JSON."""
        data = dict()
        # Open CSV reader.
        with open(_csvFilePath, encoding="utf-8") as csvFile:
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

