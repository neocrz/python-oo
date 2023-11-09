# from phone import Phone
from keyboard import Keyboard
item1 = Keyboard("Keyboard", 1000, 3)

# polymosphism in action (len())
print(len(item1.name))
some_list = ["some", "name"] # list
print(len(some_list))

# Polymosphism (method in other class, from Item to Phone)
item1.apply_discount()

print(item1.price)