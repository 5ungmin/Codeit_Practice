class Employee:
    """Employee Class"""
    company_name = "Codeit Burger"
    raise_percentage = 1.03

    def __init__(self, name, wage):
        """Set instance variable"""
        self.name = name
        self.wage = wage

    def raise_pay(self):
        """Raise employee's wage"""
        self.wage *= self.raise_percentage

    def __str__(self):
        """Return employee's info in string"""
        return Employee.company_name + " employee: " + self.name


class Cashier(Employee):
    """Cashier class"""
    raise_percentage = 1.05
    burger_price = 4000

    def __init__(self, name, wage, number_sold):
        super().__init__(name, wage)
        self.number_sold = number_sold

    def take_order(self, money_received):
        """Get order and money, return change"""
        if Cashier.burger_price > money_received:
            print("Not enough money. Please check again.")
            return money_received
        else:
            self.number_sold += 1
            change = money_received - Cashier.burger_price
            return change

    def __str__(self):
        return Cashier.company_name + " Cashier: " + self.name


class DeliveryMan(Employee):
    pass


