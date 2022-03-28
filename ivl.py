"""Create Item, Vehucle, Location classes"""


class Item:
    """Class for items representation"""
    def __init__(self, name, price):
        """
        (Item, str, float) -> NoneType
        Add a new item.
        """
        self.name = name
        self.price = price


    def __str__(self):
        """
        (Item) -> str
        Return the string representation of the item.
        """
        return 'Item: {0}_______Price: {1}'


class Location:
    """Class for location representation"""
    def __init__(self, city, postoffice):
        """
        (Location, str, int) -> NoneType
        Add a new location.
        """
        self.city = str(city)
        self.postoffice = postoffice


class Vehicle:
    """Class for vehicle representation"""
    def __init__(self, vehicleNo, isAvailable=True):
        """
        (Vehicle, int, bool) -> NoneType
        Add a new vehicle.
        """
        self.vehicleNo = vehicleNo
        self.isAvailable = isAvailable
