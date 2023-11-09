import csv

class Item:

    pay_rate: float = 0.8 # pay rate after 20% descont
    all: list = []

    def __init__(self, name: str, price: float, quantity: int = 0) -> None:
        assert price >= 0, f"Price '{price}' is not greater than or equal to 0!"
        assert quantity >=0, f"Quantity '{quantity}' is not greater than or equal to 0!"

        self.__name = name 
        self.__price = price
        self.quantity = quantity

        # Actions to execute
        Item.all.append(self)

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if len(value) > 10:
            raise Exception("The name is too long!")
        self.__name = value

    # encapsulation
    @property
    def price(self):
        return self.__price


    def calculate_total_price(self) -> float:
        return self.__price * self.quantity

    def apply_discount(self) -> None:
        self.__price = self.__price * self.pay_rate

    def apply_increment(self, increment_value):
        self.__price = self.__price + self.__price * increment_value

    @classmethod
    def instantiate_from_csv(cls) -> None:

        with open("items.csv", 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)

        for item in items:
            Item(
                name=item.get("name"), # type: ignore
                price=float(item.get("price")), # type: ignore
                quantity=int(item.get("quantity")), # type: ignore
            )
    @staticmethod
    def check_integer(num):
        # count the floats that are point zero
        if isinstance(num, float):
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False
    # representation
    def __repr__(self) -> str:
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity})"

    def __connect(self, smpt_server):
        pass

    def __prepare_body(self):
        return f"""
            Hello Someone.
            We have {self.name} {self.quantity} times.
            Regards.
        """

    def __send(self):
        pass
    # example of abstraction (only send_email is necessary to see)
    def send_email(self):
        self.__connect('')
        self.__prepare_body()
        self.__send()