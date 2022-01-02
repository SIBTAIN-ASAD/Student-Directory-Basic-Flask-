from Contact import Contact
from User import User
from AddressBookModel import AddressBookModel

def signup():

    print("---------------------")
    print("|     SIGN UP       |")
    print("---------------------")
    email = input("Enter Email: ")
    pwd   = input("Enter Password: ")

    while len(pwd) < 8:
        pwd = input("Enter Password greater then 8 charachters: ")


    u = User(email, pwd)

    model = AddressBookModel("localhost","root","","address")
    exist = model.checkAlreadyExist(u)
    if exist == False:
        insert = model.signupUser(u)
        if insert == True:
            print("You successfully Registered")
        else:
            print("Signup failed")
    else:
        print("Sorry, this email is already exits")


def signIn():
    print("---------------------")
    print("|      LOG IN       |")
    print("---------------------")

    email = input("Enter Email: ")
    pwd   = input("Enter Password: ")

    u = User(email,pwd)

    model = AddressBookModel("localhost","root","","address")
    ls = model.signIn(u)

    if len(ls) >0:
        print(f"Welcome to your account: " )
        print(f"Email: {ls[0][1]}")
        print(f"pswd : {ls[0][2]}")
        inp = ""
        while inp != "q":
            print("-----------------------")
            print("Press 1 to Create contact")
            print("Press 2 to Search contact")
            print("Press 3 to Update contact")
            print("Press 4 to Delete contact")
            print("Press q to Exit")
            inp = input()

            if inp == "1":
                name = input("Enter name: ")
                mobile = input("Enter mobile: ")
                city = input("Enter city: ")
                pro = input("Enter profession: ")
                cont = Contact(ls[0][0], name, mobile, city, pro)
                
                if model.insertContact(cont, ls[0][0]) == True:
                    print("Contact has Inserted")

            elif inp == "2":
                print("\nPress 1 to search by Name")
                print("Press 2 to search by city")
                print("Press 3 to search by profession")
                inp2 = input()
                if inp2 == "1":
                    inp3 = input("Enter Name: ")
                    lst = model.searchData(inp3)
                elif inp2 == "2":
                    inp3 = input("Enter city: ")
                    lst = model.searchData(inp3)
                elif inp2 == "3":
                    inp3 = input("Enter profession: ")
                    lst = model.searchData(inp3)
                else:
                    print("Invalid Number")
                    continue
                
                print("\nHere is your Data: ")
                if len(lst) > 0:
                    for i in lst:
                        print("------------------------")
                        print(f"Name:       {i[2]}")
                        print(f"Contact:    {i[3]}")
                        print(f"CIty:       {i[4]}")
                        print(f"Profesion:  {i[5]}")
                        print(f"Contact ID: {i[0]}")
                        print(f"User ID:    {i[1]}")
                else:
                    print("=== No data found ===")
                    continue

            elif inp == "3":
                nam = input("Enter name: ")
                curr = model.searchData(nam)
                print("\nHere is your Data: ")
                if len(curr) > 0:             
                    for i in curr:   
                        print("--------------------")
                        print(f"Name:       {i[2]}")
                        print(f"Contact:    {i[3]}")
                        print(f"CIty:       {i[4]}")
                        print(f"Profesion:  {i[5]}")
                        print(f"Contact ID: {i[0]}")
                        print(f"User ID:    {i[1]}")
                else:
                    print("=== No data found ===")
                    continue
                print("=== Enter Updated data")
                name = input("Enter name: ")
                mobile = input("Enter mobile: ")
                city = input("Enter city: ")
                pro = input("Enter profession: ")
                cont = Contact(ls[0][0], name, mobile, city, pro)
                
                if model.UpdateContact(cont, ls[0][0]) == True:
                    print("=== CONTACT UPDATED ===")
                
            elif inp == "4":
                lstd = model.AllData(ls[0][0])
                for lst in lstd:
                    print("--------------------")
                    print(f"Name:       {lst[2]}")
                    print(f"Contact:    {lst[3]}")
                    print(f"CIty:       {lst[4]}")
                    print(f"Profesion:  {lst[5]}")
                    print(f"Contact ID: {lst[0]}")
                    print(f"User ID:    {lst[1]}")

                val = input("Contact ID to be delete: ")
                model.deleteData(val)
                print(f"=== Contact ID {val} deleted === ")
                
            elif inp == "q":
                exit(0)
            else:
                print("Invalid Input")

            
    else:
        return None





def main():
    signup()
    signIn()



main()