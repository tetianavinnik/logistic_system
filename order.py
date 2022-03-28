"""Create Order class"""
from ivl import Location, Vehicle, Item
import random


ORDER_ID = []
class Order:
    """Class for orders representation"""
    def __init__(self, user_name, city, postoffice, items, vehicle=''):
        """
        (Order, str, Location, list(Item), None) -> NoneType
        Add a new order.
        """
        self.orderId = self.id_count()
        self.user_name = str(user_name)
        self.location = Location(city, postoffice)
        self.items = items[:]
        self.vehicle = vehicle
        print('Your order number is {0}.'.format(self.orderId))


    def __str__(self):
        """
        (Order) -> str
        Return the string representation of the order.
        """
        return 'Your order number is {0}.'.format(self.orderId)


    def id_count(self):
        """
        (Order) -> int
        Returns id for order.
        """
        global ORDER_ID
        id = random.randint(100000000, 999999999)
        if id not in ORDER_ID:
            ORDER_ID.append(id)
        return id


    def calculateAmount(self):
        """
        (Order) -> int
        Return amount of items.
        """
        return len(self.items)


    def calcPrice(self):
        """
        (Order) -> float
        Return price of items.
        """
        total = 0
        for i in self.items:
            total += i.price
        return total


    def assignVehicle(self, vehicle):
        """
        (Order, Vehicle) -> NoneType
        Assign vehicle for delivery.
        """
        if vehicle.isAvailable:
            self.vehicle = vehicle
            vehicle.isAvailable = False
