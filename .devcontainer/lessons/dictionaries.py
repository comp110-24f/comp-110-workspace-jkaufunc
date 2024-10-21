ice_cream: dict[str, int] = {"chocolate": 12, "vanilla": 8, "strawberry": 4}
# the string is the *key* and the int is the *value*

ice_cream["vanilla"] += 5
# this updates (or appends) the value associated with the key, vanilla

ice_cream.pop("chocolate")
# you can pop a key *and* a value using pop. Instead of an index, input the key

# how do you know if a certain key is in the dictionary? You can check! The syntax is
# <key> in <dict_name>, and it will return a bool (True/False)
print("coffee" in ice_cream)
