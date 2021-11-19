"""
Docs:
YAML: https://pyyaml.org/wiki/PyYAMLDocumentation
"""

import json
import yaml
import csv
import os
from PIL import Image #as Image_

class File():
    """File object."""
    def __init__(
        self, #FILE_NAME
    ):
        pass

    def is_exist(self, _pathToFile) -> bool:
        """Return True if file exists, otherwise False."""
        if os.path.exists(_pathToFile): #in os.listdir(self.PATH):
            return True # file exists.
        else:
            return False # file does not exist.

    def is_empty(self, _pathToFile) -> bool:
        """Return True if file is empty, False if not, None if file not exist."""
        try:
            if os.path.isfile(_pathToFile) and os.path.getsize(_pathToFile) == 0:
                return True # file is empty.
        except FileNotFoundError:
            return None # file does not exist.
        if os.path.isfile(_pathToFile) and os.path.getsize(_pathToFile) > 0:
            return False # file is not empty.

    def create(self, _pathToFile):
        """
        If file does not exist - create it, otherwise return an Error.
        A string argument should not contain ~ or $HOME due to error.
        """
        try:
            open(_pathToFile, "x")
        except FileExistsError:
            raise "File already exists!"

    def rename(self, _pathToFile:str, _pathToNewFile:str):
        """Rename file."""
        os.rename(_pathToFile, _pathToNewFile)

    def delete(self, _pathToFile):
        """Delete file from computer permanently."""
        if os.path.exists(_pathToFile):
            os.remove(_pathToFile)
        else:
            raise "File does not exist!"

    def insert(self, _data, _pathToFile):
        """Insert data to file."""
        pass

    def edit(self, _pathToFile):
        """Edit file."""
        pass

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

    def return_dict_as_object(self, _dict:dict):
        """
        Return dictionary (json, yaml, Python dictionary) as object.
        YAML and JSON need to be converted to Python dictionary first.
        """
        d = _dict
        class Object():
            def __init__(self, D):
                self.__dict__.update(D)
        return Object(d)

class JsonFile(File):
    """JSON object."""
    def __init__(
        self,
    ):
        super().__init__()

    def is_json(self, _pathToFile) -> bool:
        """Return True if file ends with .json, otherwise False."""
        if _pathToFile.endswith(".json"):
            return True
        else:
            return False
#        try:
#            with open(_pathToFile, "r+") as file:
#                json.load(file)
#        except json.decoder.JSONDecodeError:
#            return False # file is not *.json.
#        else:
#            return True # file is *.json.

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

    def load_from_json(self, _pathToFile:str) -> dict:
        """Return data as JSON."""
        with open(_pathToFile, "r+") as file:
            data = json.load(file)
        return data

class YamlFile(File):
    """Yaml object."""
    def __init__(
        self,
    ):
        super().__init__()

    def is_yaml(self, _pathToFile) -> bool:
        """Return True if file ends with .yaml or .yml, otherwise False."""
        if _pathToFile.endswith(".yaml") or _pathToFile.endswith(".yml"):
            return True
        else:
            return False
        #try:
        #    with open(_pathToFile, "r+") as file:
        #        yaml.load(file)
        #except yaml.YAMLError:
        #    return False
        #else:
        #    return True

    def dump_to_yaml(self, _data:dict, _pathToFile:str):
        """Dump data to *.yaml file."""
        with open(_pathToFile, "r+") as file:
            yaml.dump(_data, file)

    def load_from_yaml(self, _pathToFile:str) -> dict:
        """Return data as YAML."""
        with open(_pathToFile, "r+") as file:
            data = yaml.safe_load(file)
        return data

class ImageFile(File):
    """Image object."""
    def __init__(
        self,
    ):
        super().__init__()

    def remove_exif_metadata(self, _pathToImage=None, _pathToNewImage=None):
        """
        Remove meta-data from image and save it to new image.

        _pathToImage excepts also directory path as well as list of image names.
        _pathToImage excepts also list of image names.
        """
        image_file_formats = ["jpeg", "png"]
        if os.path.isdir(_pathToImage):
            f = list(os.listdir(_pathToImage))
        if os.path.isfile(_pathToImage):
            f = list(os.listdir(_pathToImage))
        p = list(_pathToNewImage)
        for file in f:
            for image_file_format in image_file_formats:
                if file.endswith("." + image_file_format):
                    image = Image.open(file)
                    data = list(image.getdata())
                    image_without_exif = Image.new(image.mode, image.size)
                    image_without_exif.putdata(data)
                    image_without_exif.save(p.pop(0))



#    def append_to_list_in_json_file(self, first_key, second_key):
#        """"""
#        with open(self.file, "r+") as file:
#            data = json.load(file)
#            data[first_key].append(second_key[first_key][0])
#            file.seek(0)
#            json.dump(data, file, indent=4)
