# Shop Test
# Demonstrate lists of items.
# In this project you can index a list, slice a list.
# Add a new items to the list and delete a list.

# create a list of items that a shop has and will be dislaying using a for loop
inventory = ["healing potion", "mana potion", "antidote", "warp scroll" ]
print("\nShop Keeper: Hello, here are my current items in my shop: ")
for items in inventory:
	print(items)

input("\nPress the Enter Key to continue.")

# Now lets display the length or number of items in the inventory
print("\nShop Keeper: The number of  items that I sell is ", len(inventory), ".")

# Now let's pretend a player bought a potion
item = str(input("\nHello, What Item do you want to buy? "))
print("\nShop Keeper: You want to have buy a  ", item , "?")
if item.lower() in inventory:
	print("The player just bought a ", item, ".")
else:
	print("Sorry, but we dont have the ", item,".")

input("\nPress the Enter Key to continue.")

# Displaying one index

print("""\n\n
Indexs of the items:
[0] - healing potion
[1] - mana potion
[2] - antidote
[3] - warp scroll
""")
index = int(input("\nShop Keeper: Please enter an index of item you want to buy. "))
print("The Index you choose is : ", index)
print("And that is the the item : ", inventory[index])

input("\nPress the Enter Key to continue.")