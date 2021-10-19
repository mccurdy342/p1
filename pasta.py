class Menu():
  def __init__(self, name, items, start_time, end_time):
    self.name = name
    self.items = items
    self.start_time = start_time
    self.end_time = end_time
  def __repr__(self):
    return "{name} menu available from {start_time} to {end_time}".format(name = self.name, start_time = self.start_time, end_time = self.end_time)

  def calculate_bill(self, purchased_items):
    total = 0
    for item in purchased_items:
      total += self.items[item]
    return total

class Franchise():
  def __init__(self, address, menus):
    self.address = address
    self.menus  = menus

  def __repr__(self):
    return "The restaurant is located at {location}".format(location = self.address)

  def available_menus(self,time):
    available_menus = []
    for menu in self.menus:
      if menu.start_time <= time and menu.end_time >= time:
        available_menus.append(menu)
    return available_menus



items_brunch = {
  'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50
}

items_early_bird = {
  'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00, 'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00,
}
items_dinner = {
  'crostini with eggplant caponata': 13.00, 'ceaser salad': 16.00, 'pizza with quattro formaggi': 11.00, 'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00,
}
items_kids = {
  'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00
}
brunch = Menu("brunch", items_brunch, 11, 16)
early_bird = Menu("early_bird", items_early_bird, 15,18)
dinner = Menu("dinner", items_dinner, 17, 23)
kids = Menu("kids", items_kids, 11, 21)

print(brunch)
print(brunch.calculate_bill(['pancakes', 'home fries', 'coffee']))
print(early_bird.calculate_bill(['salumeria plate', 'mushroom ravioli (vegan)']))




flagship_store = Franchise("1232 West End Road", [brunch, early_bird, dinner, kids])

new_installment = Franchise("12 East Mulberry Street", [brunch, early_bird, dinner, kids])

print(flagship_store)
print(flagship_store.available_menus(12))
print(flagship_store.available_menus(17))
