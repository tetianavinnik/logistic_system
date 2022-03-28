"""Create LogisticSystem class"""
from ivl import Item, Vehicle, Location
from order import Order


class LogisticSystem:
    """Class for logistic system representation"""
    def __init__(self, vehicles, orders=[]):
        """
        (LogisticSystem, list(Order), list(Vehicle)) -> NoneType
        Coordinate delivery.
        """
        self.vehicles = vehicles[:]
        self.orders = orders[:]


    def placeOrder(self, order):
        """
        (LogistucSystem, Order) -> NoneType
        Assign the delivery.
        """
        self.orders.append(order)
        for i in self.vehicles:
            order.assignVehicle(i)
            if order.vehicle != '':
                break
        if order.vehicle == '':
            return print('There is no available vehicle to deliver an order.')


    def trackOrder(self, id):
        """
        (LogisticSystem, int) -> NoneType
        Track the order.
        """
        for i in self.orders:
            if i.orderId == id and i.vehicle != '':
                return print('Your order #{0} is sent to {1}. \
Total price: {2} UAH.'\
                             .format(i.orderId, i.location.city, i.calcPrice()))
        return print('No such order.')
