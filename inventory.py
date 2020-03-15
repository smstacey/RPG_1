dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

myInventory = {'gold coin': 3, 'rope': 1}

def addToInventory(inventory, addedItems):
	for i in addedItems:
		if i in inventory:
			inventory[i] += 1
		else:
			inventory[i] = 1
	return inventory

def displayInventory(inventory):
	counter = 0
	print("Inventory:")
	for i in inventory:
		counter += 1
		print(inventory[i], i)
	print("Total number of items:", counter)


displayInventory(myInventory)
myInventory = addToInventory(myInventory, dragonLoot)
displayInventory(myInventory)

