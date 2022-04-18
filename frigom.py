import listf as l

workingList = l.listf()
workingList.readList()
print(workingList.showList())

##

##

def parseCommand(command):
    return command.split()

def functAdd(cmd):
    if len(cmd) == 5:
        workingList.addItem(l.item(cmd[1],cmd[2],cmd[3],cmd[4]))
    else:
        print("Error in parameters")

def functEat(cmd):
    if len(cmd) == 2:
        workingList.deleteItem(int(cmd[1]))
    else:
        print("Error in parameters")

command = input("Please type your command here: \n")
while command != "exit":
    workingList.showList
    cmd = parseCommand(command)
    if cmd[0] == "add":
        functAdd(cmd)
    elif cmd[0] == "eat":
        functEat(cmd)
    elif cmd[0] == "test":
        pass
    else:
        print("Error in the command")
        break
    print(workingList.showList())
    command = input("Your next command: \n")
