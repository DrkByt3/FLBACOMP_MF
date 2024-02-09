business = []
"""Takes everything from the text file and puts it into the variable business"""
def RetrieveList ():
    with open('Data', 'r') as file:
        for line in file:
             if line != "\n":
                newLine = line.replace("\n", "")
                business[-1].append(newLine)
             else:
                business.append([])
"""Takes everything from the variable business and puts it in the text file"""
def SaveList():
    with open('Data', 'w') as file:
        for i in business:
            file.write("\n")
            for j in i:
                file.write(j + "\n")
"""Searches the text file for the organizations name the organizations resources or the organizations contact information"""
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
#This allows the user to edit the text file
def EditList():
    newOrg = input("Enter an organization: ")
    newRes = input("Enter the resources: ")
    newCon = input("Enter the contact information: ")
    newList = [newOrg, newRes, newCon]
    business.append(newList)
    SaveList()

continue_program = True

while continue_program == True:
    print("Welcome, this program will help you view search through and edit the list of organizations and community partners working with Countryside High School. ")
    continue_program = False


