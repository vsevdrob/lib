class PyClass():
    """"""
    def __init__(
        self,
    ):
        pass

    def __str__():
        pass

    def return_attr_to_value(_pathToClass) -> dict:
        """Return object attributes of class as key with value."""
        attr_to_value = {}
        # Iterate through object attributes.
        for attr, value in _pathToClass.__dict__.items():
            attr_to_value[attr] = value
        return attr_to_value

    def return_dict_as_object(_dict:dict):
        """
        Return dictionary (json, yaml, Python dictionary) as object.
        YAML and JSON need to be converted to Python dictionary first.
        """
        d = _dict
        class Object():
            def __init__(self, D):
                self.__dict__.update(D)
        return Object(d)



