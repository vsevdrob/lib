"""
Docs:
YAML: https://pyyaml.org/wiki/PyYAMLDocumentation
"""

import ast
import json
import yaml
import csv
import os
import pathlib
from PIL import Image
import sys

def is_exist(_path) -> bool:
    """Return True if file exists, otherwise False."""
    if os.path.exists(_path): # in os.listdir(_path):
        return True
    else:
        return False

def is_empty(_path) -> bool:
    """Return True if file is empty, False if not, None if file not exist."""
    is_file = None
    is_empty = os.path.getsize(_path) == 0

    try:
        is_file = os.path.isfile(_path)
    except FileNotFoundError:
        print("File does not exist.")
        sys.exit()

    if is_file and is_empty:
        return True
    else:
        return False

def create(_path):
    """
    If file does not exist - create it, otherwise return an Error.
    A string argument should not contain ~ or $HOME due to error.
    """
    try:
        open(_path, "x")
    except FileExistsError:
        print("File already exists.")

def read(_path):
    """
    Read file and return data as string representation.
    For literal evaluation use eval_literal() method.
    """
    with open(_path, "r", encoding="utf-8") as file:
        data = file.read()
    return data

def eval_literal(_path):
    """
    Return safely literal evaluated data from file.
    Returns error if data is incomparable with data structure of Python.
    Instead use read() method to return data as string.
    """
    try:
        with open(_path, "r", encoding="utf-8") as file:
            data = ast.literal_eval(file.read()); file.close()
        return data
    except FileNotFoundError:
        return None

def rename(_path:str, _pathToNewFile:str):
    """Rename file."""
    os.rename(_path, _pathToNewFile)

def remove(_path:str):
    """Delete file from computer permanently."""
    if os.path.exists(_path):
        os.remove(_path)
    else:
        raise FileNotFoundError

def append(_data: str, _path:str):
    """Append data to file."""
    with open(_path, "a", encoding="utf-8") as file:
        file.write(_data + "\n"); file.close()

def write(_data: str, _path: str):
    """
    Write data to file.
    Attention: overwrites whole file. Instead use append() method.
    """
    with open(_path, "w", encoding="utf-8") as file:
        file.write(_data + "\n"); file.close()

def edit(_path):
    """Edit file."""
    pass

def convert_from_csv_to_json(_pathToCSV, _pathToJSON, _primaryColumn):
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

#    def return_dict_as_object(_dict:dict):
#        """
#        Return dictionary (json, yaml, Python dictionary) as object.
#        YAML and JSON need to be converted to Python dictionary first.
#        """
#        d = _dict
#        class Object():
#            def __init__(D):
#                self.__dict__.update(D)
#        return Object(d)

def return_file_extension(_path):
    """Return string of file extension. Example: .txt; .py"""
    return pathlib.Path(_path).suffix

def return_file_name(_path):
    """Return string of file name."""
    split_tup = os.path.splitext(_path)
    file_name = split_tup[0]
    return file_name

def return_file_name_and_file_extension(_path):
    """Return tuple of file name and file extension."""
    split_tup = os.path.splitext(_path)
    file_name = split_tup[0]
    file_extension = split_tup[1]
    return (file_name, file_extension)

#class JsonFile(File):
#    """JSON object."""
#    def __init__(
#        self,
#    ):
#        super().__init__()

def is_json(_path) -> bool:
    """Return True if file ends with .json, otherwise False."""
    if _path.endswith(".json"):
        return True
    else:
        return False
#        try:
#            with open(_path, "r+") as file:
#                json.load(file)
#        except json.decoder.JSONDecodeError:
#            return False # file is not *.json.
#        else:
#            return True # file is *.json.

def dump_to_json(_data:dict, _path:str, _indent:int=4):
    """Dump data to *.json file."""
    with open(_path, "w") as file:
        json.dump(_data, file, indent=_indent)

def dump_template_to_json(_path:str, _template:dict, _indent:int=4):
    """Dump template if file is not empty."""
    if is_empty(_path) == False:
        pass # file is not empty.
    else:
        # Creating template for *.json file.
        with open(_path, "r+") as file:
            json.dump(_template, file, indent=_indent)

def load_from_json(_path:str) -> dict:
    """Return data as JSON."""
    if not os.path.exists(_path):
        dump_to_json({}, _path)

    with open(_path, "r+") as file:
        data = json.load(file)
    return data

def is_yaml(_path) -> bool:
    """Return True if file ends with .yaml or .yml, otherwise False."""
    if _path.endswith(".yaml") or _path.endswith(".yml"):
        return True
    else:
        return False
    #try:
    #    with open(_path, "r+") as file:
    #        yaml.load(file)
    #except yaml.YAMLError:
    #    return False
    #else:
    #    return True

def dump_to_yaml(_data:dict, _path:str):
    """Dump data to *.yaml file."""
    with open(_path, "r+") as file:
        yaml.dump(_data, file)

def load_from_yaml(_path:str) -> dict:
    """Return data as YAML."""
    with open(_path, "r+") as file:
        data = yaml.safe_load(file)
    return data

def read_from_csv(_path:str):
    """Read csv file and return field names and data rows."""
    fieldNames, dataRows = [], []
    with open(_path, "r", encoding="utf-8") as file:
        # Create a csv reader object.
        csvReader = csv.reader(file)
        # Extract field names through first row.
        fieldNames = next(csvReader)
        # Extract each data row one by one.
        for row in csvReader:
            dataRows.append(row)
    return (fieldNames, dataRows)

def return_field_names():
    pass

def write_to_csv(_fieldNames:list, _dataRows:list, _path:str):
    """Write data to csv file."""
    with open(_path, "w") as file:
        # Create csv writer object.
        csvWriter = csv.writer(file)
        # Write fields.
        csvWriter.writerow(_fieldNames)
        # Write data rows.
        csvWriter.writerows(_dataRows)

def remove_exif_metadata(_pathToImage=None, _pathToNewImage=None):
    """
    Remove meta-data from image and save it to new image.

    _pathToImage excepts also directory path as well as list of image names.
    _pathToImage excepts also list of image names.
    """
    image_file_formats = ["jpeg", "png"]
    if os.path.isdir(_pathToImage):
        f = sorted(list(os.listdir(_pathToImage)))
    if os.path.isfile(_pathToImage):
        f = list(_pathToImage)
    p = list(_pathToNewImage)
    for file in f:
        for image_file_format in image_file_formats:
            if file.endswith("." + image_file_format):
                image = Image.open(file)
                data = list(image.getdata())
                image_without_exif = Image.new(image.mode, image.size)
                image_without_exif.putdata(data)
                image_without_exif.save(p.pop(0))
