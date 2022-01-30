def displayInventory(inventory:dict)->None:
    print("Inventory: ")
    item_count = 0
    for item, amount in inventory.items():
        item_count += amount
        print("{} ".format(amount)+item)
    print("Total # of Items: {}".format(item_count))

def addToInventory(inventory:dict, items:list)->dict:
    for i in items:
        if i in inventory.keys(): inventory[i]+=1
        else: inventory[i] = 1
    return inventory

stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
displayInventory(stuff)
#inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
print(stuff)
stuff = addToInventory(stuff, dragonLoot)
displayInventory(stuff)