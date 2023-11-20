import sys
sys.path.append(".")

from ctuClass import ctuStock
def start_menu(): #This is the main menu
    print("")
    print("Welcome to CTU Technologies")
    print("")
    print("1. Shop Management")
    print("2. Sales")
    print("3. Returns")
    print("99. Exit")
    print("")
    

def shop_management(): #This is the shop management menu
    print("")
    print("Shop Management")
    print("")
    print("1. Change shop name")
    print("2. Change shop location")
    print("3. Display current shops")
    print("4. Display all shops information")
    print("0. Back")
    print("")

def shop_sales(): #This shows the amount of shop sales per shop
    print("")
    print("Shop 1 Name: " + sh1.shopName)
    print(f"Sales:  {sh1.sales}")
    print("")
    print("Shop 2 Name: " + sh2.shopName)
    print(f"Sales:  {sh2.sales}")
    print("")
    print("Shop 3 Name: " + sh3.shopName)
    print(f"Sales:  {sh3.sales}")
    print("")
    print("Shop 4 Name: " + sh4.shopName)
    print(f"Sales:  {sh4.sales}")
    print("")

def shop_returns(): #This shows the amount of shop returns per shop
    print("")
    print("Shop 1 Name: " + sh1.shopName)
    print(f"Sales:  {sh1.returns}")
    print("")
    print("Shop 2 Name: " + sh2.shopName)
    print(f"Sales:  {sh2.returns}")
    print("")
    print("Shop 3 Name: " + sh3.shopName)
    print(f"Sales:  {sh3.returns}")
    print("")
    print("Shop 4 Name: " + sh4.shopName)
    print(f"Sales:  {sh4.returns}")
    print("")

def change_shop_name():            #This function displays the shops names and allows you to change them
    print("")
    print("Change shop name")
    print("")
    print("Select a shop")
    print("")
    print(f"1. {sh1.shopName}")
    print(f"2. {sh2.shopName}")
    print(f"3. {sh3.shopName}")
    print(f"4. {sh4.shopName}")
    print("0. to go back to main menu")
    print("")
    while True:
        try:
            myinput = int(input("select an option: "))
        except ValueError:
            print("--------Invalid Input--------")
            change_shop_name()
            continue
        else:
            break
    if myinput == 1:
        sh1.shopName = str(input("What would you like the shops name to be?"))
        print(f"1. {sh1.shopName}")
        print(f"2. {sh2.shopName}")
        print(f"3. {sh3.shopName}")
        print(f"4. {sh4.shopName}")
        print("0. to go back to main menu")

    elif myinput == 2:
        sh2.shopName = str(input("What would you like the shops name to be?"))
        print(f"1. {sh1.shopName}")
        print(f"2. {sh2.shopName}")
        print(f"3. {sh3.shopName}")
        print(f"4. {sh4.shopName}")
        print("0. to go back to main menu")

    elif myinput == 3:
        sh3.shopName = str(input("What would you like the shops name to be?"))
        print(f"1. {sh1.shopName}")
        print(f"2. {sh2.shopName}")
        print(f"3. {sh3.shopName}")
        print(f"4. {sh4.shopName}")
        print("0. to go back to main menu")

    elif myinput == 4:
        sh4.shopName = str(input("What would you like the shops name to be?"))
        print(f"1. {sh1.shopName}")
        print(f"2. {sh2.shopName}")
        print(f"3. {sh3.shopName}")
        print(f"4. {sh4.shopName}")
        print("0. to go back to main menu")

    elif myinput == 0:
        main()

    else:
        print("")
        print("--------Invalid Input--------")
        change_shop_name()

def change_shop_location(): #This is the change shop function, it displays the shops name and location
    print("")               #This also allows you to change the location with user input
    print("Change shop location")
    print("")
    print("Select a shop")
    print("")
    print(f"1. {sh1.shopName} , {sh1.shopLocation}")
    print(f"2. {sh2.shopName} , {sh2.shopLocation}")
    print(f"3. {sh3.shopName} , {sh3.shopLocation}")
    print(f"4. {sh4.shopName} , {sh4.shopLocation}")
    print("0. To go back to main menu")
    while True:
        try:
            myinput = int(input("select an option"))
        except ValueError:
            print("--------Invalid Input--------")
            change_shop_location()
            continue
        else:
            break
    if myinput == 1: #This is shop location number 1
        myinput = str(input("Enter a location: Free State, Gauteng, KZN, Limpopo: "))
        if myinput == "Free State":
            sh1.shopLocation = myinput
            print(f"1. {sh1.shopName} , {sh1.shopLocation}")
            print(f"2. {sh2.shopName} , {sh2.shopLocation}")
            print(f"3. {sh3.shopName} , {sh3.shopLocation}")
            print(f"4. {sh4.shopName} , {sh4.shopLocation}")

        elif myinput == "Gauteng":
            sh1.shopLocation = myinput
            print(f"1. {sh1.shopName} , {sh1.shopLocation}")
            print(f"2. {sh2.shopName} , {sh2.shopLocation}")
            print(f"3. {sh3.shopName} , {sh3.shopLocation}")
            print(f"4. {sh4.shopName} , {sh4.shopLocation}")

        elif myinput == "KZN":
            sh1.shopLocation = myinput
            print(f"1. {sh1.shopName} , {sh1.shopLocation}")
            print(f"2. {sh2.shopName} , {sh2.shopLocation}")
            print(f"3. {sh3.shopName} , {sh3.shopLocation}")
            print(f"4. {sh4.shopName} , {sh4.shopLocation}")

        elif myinput == "Limpopo":
            sh1.shopLocation = myinput
            print(f"1. {sh1.shopName} , {sh1.shopLocation}")
            print(f"2. {sh2.shopName} , {sh2.shopLocation}")
            print(f"3. {sh3.shopName} , {sh3.shopLocation}")
            print(f"4. {sh4.shopName} , {sh4.shopLocation}")

        else:
            print("")
            print("--------Invalid input--------")
            change_shop_location()

        #sh1.shopLocation = str(input("What would you like the shops name to be?"))

    elif myinput == 2: #This is shop location number 2
        myinput = str(input("Enter a location: Free State, Gauteng, KZN, Limpopo: "))
        if myinput == "Free State":
            sh2.shopLocation = myinput
            print(f"1. {sh1.shopName} , {sh1.shopLocation}")
            print(f"2. {sh2.shopName} , {sh2.shopLocation}")
            print(f"3. {sh3.shopName} , {sh3.shopLocation}")
            print(f"4. {sh4.shopName} , {sh4.shopLocation}")

        elif myinput == "Gauteng":
            sh2.shopLocation = myinput
            print(f"1. {sh1.shopName} , {sh1.shopLocation}")
            print(f"2. {sh2.shopName} , {sh2.shopLocation}")
            print(f"3. {sh3.shopName} , {sh3.shopLocation}")
            print(f"4. {sh4.shopName} , {sh4.shopLocation}")

        elif myinput == "KZN":
            sh2.shopLocation = myinput
            print(f"1. {sh1.shopName} , {sh1.shopLocation}")
            print(f"2. {sh2.shopName} , {sh2.shopLocation}")
            print(f"3. {sh3.shopName} , {sh3.shopLocation}")
            print(f"4. {sh4.shopName} , {sh4.shopLocation}")

        elif myinput == "Limpopo":
            sh2.shopLocation = myinput
            print(f"1. {sh1.shopName} , {sh1.shopLocation}")
            print(f"2. {sh2.shopName} , {sh2.shopLocation}")
            print(f"3. {sh3.shopName} , {sh3.shopLocation}")
            print(f"4. {sh4.shopName} , {sh4.shopLocation}")

        else:
            print("")
            print("--------Invalid input--------")
            change_shop_location()
    
    elif myinput == 3: #This is shop location number 3
        myinput = str(input("Enter a location: Free State, Gauteng, KZN, Limpopo: "))
        if myinput == "Free State":
            sh3.shopLocation = myinput
            print(f"1. {sh1.shopName} , {sh1.shopLocation}")
            print(f"2. {sh2.shopName} , {sh2.shopLocation}")
            print(f"3. {sh3.shopName} , {sh3.shopLocation}")
            print(f"4. {sh4.shopName} , {sh4.shopLocation}")

        elif myinput == "Gauteng":
            sh3.shopLocation = myinput
            print(f"1. {sh1.shopName} , {sh1.shopLocation}")
            print(f"2. {sh2.shopName} , {sh2.shopLocation}")
            print(f"3. {sh3.shopName} , {sh3.shopLocation}")
            print(f"4. {sh4.shopName} , {sh4.shopLocation}")

        elif myinput == "KZN":
            sh3.shopLocation = myinput
            print(f"1. {sh1.shopName} , {sh1.shopLocation}")
            print(f"2. {sh2.shopName} , {sh2.shopLocation}")
            print(f"3. {sh3.shopName} , {sh3.shopLocation}")
            print(f"4. {sh4.shopName} , {sh4.shopLocation}")

        elif myinput == "Limpopo":
            sh3.shopLocation = myinput
            print(f"1. {sh1.shopName} , {sh1.shopLocation}")
            print(f"2. {sh2.shopName} , {sh2.shopLocation}")
            print(f"3. {sh3.shopName} , {sh3.shopLocation}")
            print(f"4. {sh4.shopName} , {sh4.shopLocation}")



        else:
            print("Invalid input")
            change_shop_location()



    elif myinput == 4:#This is shop location number 4
        myinput = str(input("Enter a location: Free State, Gauteng, KZN, Limpopo: "))
        if myinput == "Free State":
            sh4.shopLocation = myinput
            print(f"1. {sh1.shopName} , {sh1.shopLocation}")
            print(f"2. {sh2.shopName} , {sh2.shopLocation}")
            print(f"3. {sh3.shopName} , {sh3.shopLocation}")
            print(f"4. {sh4.shopName} , {sh4.shopLocation}")

        elif myinput == "Gauteng":
            sh4.shopLocation = myinput
            print(f"1. {sh1.shopName} , {sh1.shopLocation}")
            print(f"2. {sh2.shopName} , {sh2.shopLocation}")
            print(f"3. {sh3.shopName} , {sh3.shopLocation}")
            print(f"4. {sh4.shopName} , {sh4.shopLocation}")

        elif myinput == "KZN":
            sh4.shopLocation = myinput
            print(f"1. {sh1.shopName} , {sh1.shopLocation}")
            print(f"2. {sh2.shopName} , {sh2.shopLocation}")
            print(f"3. {sh3.shopName} , {sh3.shopLocation}")
            print(f"4. {sh4.shopName} , {sh4.shopLocation}")

        elif myinput == "Limpopo":
            sh4.shopLocation = myinput
            print(f"1. {sh1.shopName} , {sh1.shopLocation}")
            print(f"2. {sh2.shopName} , {sh2.shopLocation}")
            print(f"3. {sh3.shopName} , {sh3.shopLocation}")
            print(f"4. {sh4.shopName} , {sh4.shopLocation}")

        else:
            print("Invalid input")
            change_shop_location()
    
    elif myinput == 0:
        main()
         
   
def display_current_shops(): #this function displays the current shops
    print("Current shops")
    print("")
    print(f"1. {sh1.shopName} , {sh1.shopLocation}")
    print(f"2. {sh2.shopName} , {sh2.shopLocation}")
    print(f"3. {sh3.shopName} , {sh3.shopLocation}")
    print(f"4. {sh4.shopName} , {sh4.shopLocation}")

def display_all_shops_info():#This function displays all shops information
    print("-----------------------------------")
    print("")
    print(f"Shop Name: {sh1.shopName}")
    print(f"Shop Location: {sh1.shopLocation}")
    print(f"Number of Customers: {sh1.customers}")
    print(f"Current Sales: {sh1.sales}")
    print(f"Returns: {sh1.returns}")
    print("")
    print("-----------------------------------")

    print("-----------------------------------")
    print("")
    print(f"Shop Name: {sh2.shopName}")
    print(f"Shop Location: {sh2.shopLocation}")
    print(f"Number of Customers: {sh2.customers}")
    print(f"Current Sales: {sh2.sales}")
    print(f"Returns: {sh2.returns}")
    print("")
    print("-----------------------------------")

    print("-----------------------------------")
    print("")
    print(f"Shop Name: {sh3.shopName}")
    print(f"Shop Location: {sh3.shopLocation}")
    print(f"Number of Customers: {sh3.customers}")
    print(f"Current Sales: {sh3.sales}")
    print(f"Returns: {sh3.returns}")
    print("")
    print("-----------------------------------")

    print("-----------------------------------")
    print("")
    print(f"Shop Name: {sh4.shopName}")
    print(f"Shop Location: {sh4.shopLocation}")
    print(f"Number of Customers: {sh4.customers}")
    print(f"Current Sales: {sh4.sales}")
    print(f"Returns: {sh4.returns}")
    print("")
    print("-----------------------------------")


sh1 = ctuStock("Default", "Default", 0, 0, 0) #these are the 4 objects
sh2 = ctuStock("Default", "Default", 0, 0, 0)
sh3 = ctuStock("Default", "Default", 0, 0, 0)
sh4 = ctuStock("Default", "Default", 0, 0, 0)



def main():
    start_menu() #This is the main menu that displays the first few options
    while True:
        try:            
            myinput = int(input("Select an option or 99 to exit"))
        except ValueError: #This is a try catch for when a value error occurs
            start_menu()
            print("--------Invalid Input--------")
            continue
        else:
            break   
    if myinput == 1:
        shop_management() #This is the Shop Management menu
        while True:
            try:
                myinput = int(input("select an option"))
            except ValueError:
                shop_management()
                print("--------Invalid Input--------")
                continue
            else:
                break
        if myinput == 1: 
            change_shop_name()  #This calls the change shop name function
            change_shop_name()
            change_shop_name()
            change_shop_name()
            change_shop_name()
            change_shop_name()

            myinput = int(input("Do you want to go back to start menu? (0) is yes (1) is Exit program"))
            if myinput == 0:
                main() #This function loops back to the Start menu
            else:
                exit() #This function exits the program


        elif myinput == 2:
            change_shop_location() #This calls the change shop location function
            change_shop_location()
            change_shop_location()
            change_shop_location()
            change_shop_location()
            change_shop_location()

            myinput = int(input("Do you want to go back to start menu? (0) is yes (1) is Exit program"))
            if myinput == 0:
                main()
            else:
                exit()
           

        elif myinput == 3:
            display_current_shops()
            myinput = int(input("Do you want to go back to start menu? (0) is yes (1) is Exit program"))
            if myinput == 0:
                main()
            else:
                exit()

        elif myinput == 4:
            display_all_shops_info()
            myinput = int(input("Do you want to go back to start menu? (0) is yes (1) is Exit program"))
            if myinput == 0:
                main()
            else:
                exit()

        elif myinput == 0:
            main()

        else:
            print("--------Invalid Input--------")
            main()

    elif myinput == 2:
        shop_sales()
        while True:
            try:
                myinput = int(input("select (0) to go back to main menu or (1) to end program"))
            except ValueError:
                shop_sales()
                print("--------Invalid Input--------")
                continue
            else:
                break
        if myinput == 0:
            main()
        else:
            exit()

    elif myinput == 3:
        shop_returns()
        while True:
            try:
                myinput = int(input("Do you want to go back to start menu? (0) is yes (1) is Exit program"))
            except ValueError:
                shop_returns()
                print("--------Invalid Input--------")
                continue
            else:
                break
        if myinput == 0:
            main()
        else:
            exit()
            
    elif myinput == 99:
        exit()

    else:
        print("")
        print("--------Invalid Input--------")
        main()


main() #main starts the program
    

