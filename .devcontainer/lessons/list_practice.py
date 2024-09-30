"""Practice with lists"""

my_numbers: list[float] = list()
# print(my_numbers)

my_numbers.append(3.14)
# print(my_numbers)

# append only allows you to add one item to a list

# a list can be initialized with items when first defining it

new_list: list[str] = ["beginning", "middle", "end"]
# print(new_list)

# indexing allows you to retrieve or add an item in a specific location
# (counting starts at 0!)

# print(new_list[0])

# what if we want the last item, but don't know how long the list is?

# print(new_list[len(new_list) - 1])
# note: [-1] will also work because negatives count from the back/end

game_numbers: list[int] = [75, 43, 92]
# print(game_numbers)

# replacing an item with another in a specific location:

game_numbers[1] = 26
# print(game_numbers)

my_name: str = "James"

my_name_as_list: list[str] = list(my_name)
# print(my_name_as_list)

# do some experimentint with this!

# to remove an item from a list, use "pop"

game_numbers.pop(0)
# print(game_numbers)

# insert can be used to (!) insert an item to a specific index (shocker!)
