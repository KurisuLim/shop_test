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

input("\nPress the Enter Key to continue.")

# Now let's pretend a player bought a potion
item = str(input("\nHello, What Item do you want to buy? "))
print("\nShop Keeper: Do you want to have buy a ", item , "?")
if item.lower() in inventory:
	print("The player just bought a ", item, ".")
else:
	print("Shop Keeper: Sorry, but we dont have the ", item,".")

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


# Now lets try doing some slicing

begin = int(input("\nShop Keeper: Please enter a starting index from my inventory. "))
end = int(input("\nShop Keeper: Now please enter a end index from my inventory. "))
print("\nShop Keeper: Inventory[", begin, ":", end,"] is ", end=" ")
print(inventory[begin:end])

input("\nPress the Enter Key to continue.")

#Added a new item in the list by concat
playerTrash = ["goblin tooth", "toenail of ogre"]
print("\nPlayer just sold his ", playerTrash, " to the Shop Keeper")
inventory += playerTrash
print("\nShop keeper: Now I have these items to sell: ")

for items in inventory:
	print(items)

input("\nPress the Enter Key to continue.")

#Add a new list through index
print("\nPlayer just traded his dagger for a healing potion.")
inventory[0] = "dagger"
print("\nShop keeper: Thank you for your trade. Here is now the items I sell:")

for items in inventory:
	print(items)

input("\nPress the Enter Key to continue.")

# Adds new item through slice
print("\nPlayer sold his excalibur sword for 1 gold.")
inventory[2:3] = ["excalibur sword"]
print("\nShop Keeper: Thank you for your patronage. But here is the list of items that I sell now:")

for items in inventory:
	print(items)

input("\nPress the Enter Key to continue.")

# Now lets try removing an items from the list
print("\nThe player bought back his excalibur sword.")
del inventory[2]
print("\nShop Keeper: Thank you for buying back your sword for 100000000 gold. And here is the items that I have: ")

for items in inventory:
	print(items)

input("\nPress the Enter Key to continue.")

# Let's try removing an item through a slice
print("\nAn unkown man just bought the dagger and mana potion from the Shop Keeper.")
del inventory[:2]
print("\nShop keeper: Wow! I almost have no more inventory! ")

for items in inventory:
	print(items)

input("\nPress the Enter Key to continue.")

# Now lets punish the shop keeper for being greedy by removing all his items and gold.
print("\nA goblin with a torch comes into the shop and destorys everything.")
print("\nNow the Shop keeper lost his gold and the items he owns:")

for items in inventory:
	del inventory[0:2]
	print(items)

input("\nPress the Enter Key to exit.")