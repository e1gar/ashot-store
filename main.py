class Store:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.items = {}

    def add_item(self, item, price):
        self.items[item] = price
        print(f"{item} по цене {price} добавлен в ассортимент магазина {self.name}, по адресу {self.address}.")

    def remove_item(self, item):
        if item in self.items:
            del self.items[item]
            print(f"{item} удален из ассортимента магазина {self.name}, по адресу {self.address}.")
        else:
            print(f"{item} не найден в ассортименте магазина {self.name}, по адресу {self.address}.")

    def show_items(self):
        print(f"Ассортимент магазина {self.name}, по адресу {self.address}: ")
        for item, price in self.items.items():
            print(f"{item} - {price} рублей.")

    def show_price(self):
        for item, price in self.items.items():
            print(f"Стоимость {item} составляет {price} рублей.")

    def update_price(self, item, new_price):
        if item in self.items:
            self.items[item] = new_price
            print(f"Стоимость {item} изменилась и составляет {new_price} рублей.")
        else:
            print(f"Товар {item} не найден.")

store1 = Store("Магазин 'Березка'", "Осиновая роща, дом 4")
store2 = Store("Магазин 'Лента'", "улица Кривая, дом 15")
store3 = Store("Магазин 'ОК'", "Новый тупик, дом 1")
store4 = Store("Магазин 'У Ашота'", "Ереванский переулок, дом 777")

store4.add_item("Папиросы", 150.0)
store4.add_item("Коньяк", 2500.0)
store4.add_item("Люля-кебаб", 500.0)

store4.show_items()

store4.update_price("Папиросы", 200.0)
store4.show_items()

store4.remove_item("Коньяк")
store4.show_items()

store4.show_price()