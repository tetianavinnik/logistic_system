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


# from logistic_system import LogisticSystem
# from order import Order
# from ivl import Item, Vehicle, Location

# >>> vehicles = [Vehicle(1), Vehicle(2)]

# >>> logSystem = LogisticSystem(vehicles)

# >>> my_items = [Item('book',110), Item('chupachups',44)]

# >>> my_order = Order(user_name = 'Oleg', city = 'Lviv', postoffice = 53, items = my_items)

# >>> logSystem.placeOrder(my_order)

# >>> logSystem.trackOrder()

# >>> my_items2 = [Item('flowers',11), Item('shoes',153), Item('helicopter',0.33)]

# >>> my_order2 = Order('Andrii', 'Odessa', 3, my_items2)

# >>> logSystem.placeOrder(my_order2)

# >>> logSystem.trackOrder(234976475)

# >>> my_items3 = [Item('coat',61.8), Item('shower',5070), Item('rollers',700)]

# >>> my_order3 = Order('Olesya', 'Kharkiv', 17, my_items3)

# >>> logSystem.placeOrder(my_order3)

# >>> logSystem.trackOrder(485932990)