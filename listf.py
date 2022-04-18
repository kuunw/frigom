## Classes for the frigo and item
import csv
import string
from datetime import date
import datetime
from turtle import reset

(
    ITEM_NAME,
    ITEM_DATE,
    ITEM_MASS,
    PROP_PROTEIN
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
        self.saveList()

    def deleteItem(self,index) -> None:
        del self.inventory[index]
        self.refreshList()
        self.saveList()

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
                  self.addItem(item(row[ITEM_NAME],row[ITEM_DATE],row[ITEM_MASS],row[PROP_PROTEIN]))

    def saveList(self,path='inventory.csv') -> None:
        with open(path, "w") as csvfile:
            for item in self.inventory:
                itemOutput = item.itemName+";"+item.itemDate+";"+str(item.itemMass)+";"+str(item.propProtein)
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
        res = "No item in the fridge"
        if len(self.inventory) > 0:
            res = ''
            for item in self.inventory:
                res = res + str(item.index) + "|\t" + item.itemName + '\t' + item.itemDate + '\t' + str(item.itemMass) + '\t' + str(item.propProtein) + '\n'
        return res
