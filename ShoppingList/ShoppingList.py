import os

class ShoppingList:
    def __init__(self, filename='list.txt'):
        self.filename = filename
        self.shopping_list = {}
        self.load_list()

    def load_list(self):
        try:
            with open(self.filename, 'r') as file:
                for line in file:
                    product, quantity = line.strip().split('\t')
                    self.shopping_list[product] = int(quantity)
        except FileNotFoundError:
            open(self.filename, 'a').close()
        except Exception as e:
            print(f"An error occurred while loading the list: {e}")

    def add_product(self, product, quantity):
        if product in self.shopping_list:
            self.shopping_list[product] += quantity
        else:
            self.shopping_list[product] = quantity
        print(f"Added {quantity} of {product}.")

    def remove_product(self, product):
        if product in self.shopping_list:
            self.shopping_list[product] -= 1
            if self.shopping_list[product] <= 0:
                del self.shopping_list[product]
                print(f"{product} has been completely removed from the list.")
            else:
                print(f"Decreased quantity of {product} by one. Remaining: {self.shopping_list[product]}")
        else:
            print(f"{product} not found in the list.")

    def display_list(self):
        print("Shopping List:")
        for product, quantity in self.shopping_list.items():
            print(f"{product}: {quantity}")

    def save_list(self):
        try:
            with open(self.filename, 'w') as file:
                for product, quantity in self.shopping_list.items():
                    file.write(f"{product}\t{quantity}\n")
            print("Shopping list saved successfully.")
        except Exception as e:
            print(f"An error occurred while saving the list: {e}")

if __name__ == "__main__":
    shopping_list = ShoppingList()
    shopping_list.add_product("Pizza", 3)
    shopping_list.add_product("Juce", 2)
    shopping_list.remove_product("Qinoa")
    shopping_list.remove_product("Juce")
    shopping_list.display_list()
    shopping_list.save_list()
