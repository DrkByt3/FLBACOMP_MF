business = []
def RetrieveList ():
    with open('Data.text', 'r') as file:
        for line in file:
             if line != "\n":
                newLine = line.replace("\n", "")
                business[-1].append(newLine)
             else:
                business.append([])
def SaveList():
    with open('Data.text', 'w') as file:
        for i in business:
            file.write("\n")
            for j in i:
                file.write(j + "\n")

def Search(key):
    result = []
    for i in business:
        for j in i:
            if (key in j):
                result.append(i)
    if result == []:
        print('Error')
    else:
        for w in result:
            print (w)

def EditList():
    newOrg = input("Enter an organization: ")
    newRes = input("Enter the resources: ")
    newCon = input("Enter the contact information: ")
    newList = [newOrg, newRes, newCon]
    business.append(newList)
    SaveList()


RetrieveList()
cont = True
while cont == True:
    Action = input("Would you like to search? (Y/N): ").upper()
    if (Action == "Y"):
        Search(input("Search for Organization, Resources, or Contact Information: "))
    elif (Action == "N"):
        cont = False
cont = True
while cont == True:
    Action = input("Would you like to edit? (Y/N): ").upper()
    if (Action == "Y"):
        EditList()#make it edit right :)
    elif (Action == "N"):
        cont = False



