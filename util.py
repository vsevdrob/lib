def convert_list_to_string(_l:list, _sep:str=" "):
    """Convert list to string."""
    # map() method for mapping str (for converting elements in list to string).
    listToString = _sep.join(map(str, _l))
    return listToString

def convert_string_to_list(_str:str, _split:str=" "):
    """Convert string to list."""
    stringToList = list(_str.split(_split))
    return stringToList
