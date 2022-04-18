## Classes for the frigo and item
import csv
import string
from datetime import date
import datetime

(
    ITEM_NAME,
    ITEM_DATE,
    ITEM_MASS,
    ITEM_CAT
) = range(4)

class item():
    def __init__(self,itemName,itemDate,itemMass,propProtein) -> None:
        self.itemName = itemName
        self.itemDate = itemDate
        self.itemMass = itemMass
        self.propProtein = propProtein

    def toString(self) -> string:
        return(self.itemName+";"+self.itemDate+";"+self.itemMass+";"+self.itemCat)
    
class listf():
    def __init__(self) -> None:
        self.inventory = []

    def addItem(self,item) -> None:
        self.inventory.append(item)
        self.refreshList()

    def deleteItem(self,index) -> None:
        self.inventory.remove(self.findItemByIndex(index))
        self.refreshList()

    def findItemByIndex(self,index) -> item:
        for item in self.inventory:
            if item.index == index:
                return item

    def refreshList(self) -> None:
        for idx, item in enumerate(self.inventory):
            item.index = idx

    def readList(self,path='inventory.csv') -> None:
        with open(path, newline='') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=';', quotechar='|')
            for row in spamreader:
                  self.addItem(item(row[ITEM_NAME],row[ITEM_DATE],row[ITEM_MASS],row[ITEM_CAT]))

    def saveList(self,path='inventory.csv') -> None:
        with open(path, "w") as csvfile:
            for item in self.inventory:
                itemOutput = item.itemName+";"+item.itemDate+";"+item.itemMass+";"+str(item.propProtein)
                csvfile.write(itemOutput+"\n")
    
    def almostUseBy(self,horizon=3):
        res = []
        today = date.today()
        for item in self.inventory:
            d = item.itemDate
            targetDate = datetime.datetime.date(datetime.datetime.strptime(d,'%Y-%m-%d'))
            #print((targetDate-today).days)
            if (targetDate - today).days <= horizon:
                res.append(item)
        return res

    def showList(self) -> None:
        pass

## Test
list = listf()
item1 = item("steak","2022-04-18","240",70)
item2 = item("steak2","2022-04-19","240",70)
list.addItem(item1)
list.addItem(item2)
list.saveList()
print(list.almostUseBy())