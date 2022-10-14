class CashRegister:

    def __init__(self):
        self.total_items = {}  # {'item': 'price'}
        self.total_price = 0
        self.discount = 0

    def add_item(self, item_price: dict):
        self.total_items.update(item_price)
        for key, value in item_price.items():
            self.total_price += value
            print(f"The {key} with the price of £{value} has been added to the cart.")

    def remove_item(self, item):
        self.total_items.pop(item)
        print(f"{item.capitalize()} has been removed from the cart.")

    def apply_discount(self, discount_percentage: float):
        self.discount = round((self.total_price * discount_percentage), 2)
        print(f"The amount of £{self.discount} will be discounted from the total price.")

    def get_total(self):
        self.total_price -= self.discount
        print(f"The total price to be paid is £{self.total_price}.")

    def show_items(self):
        print("Here are the items in the cart:")
        for key, value in self.total_items.items():
            print(f"{key.capitalize():15s} £{value:.2f}")

    def reset_register(self):
        self.total_items.clear()
        self.total_price = 0
        self.discount = 0
        print("Cash register has been reset.")


# EXAMPLE code run:

register_1 = CashRegister()
register_2 = CashRegister()

# check if every function works
register_1.add_item({"apple": 2.50})
register_1.add_item({"mango": 3.99})
register_1.add_item({"tomato": 1.50})
register_1.add_item({"banana": 1.75})
register_1.add_item({"milk": 1.00})
register_1.remove_item("banana")
register_1.apply_discount(0.20)
register_1.show_items()
register_1.get_total()

# check if the cash register is reset properly
print("-----------")
print("-----------")
register_1.reset_register()
register_1.show_items()
register_1.get_total()

# check if register 2 has been initialized
print("-----------")
print("-----------")
print(register_2)


