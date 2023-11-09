from item import Item


class Phone(Item):


    def __init__(
            self, 
            name: str,
            price: float, 
            quantity: int = 0, 
            broken_phone: int = 0 ) -> None:
        
        assert broken_phone >= 0, f"Broken Phones {broken_phone} is not greater or equal to 0"

        super().__init__(name, price, quantity)
        self.broken_phone: int = broken_phone
