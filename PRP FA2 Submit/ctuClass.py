class ctuStock: #this is the Class
    def __init__(self, shopName, shopLocation, customers, sales, returns):
        self.shopName = shopName
        self.shopLocation = shopLocation
        self.customers = customers
        self.sales = sales
        self.returns = returns 

    def __str__(self):
        return '\nShop Name: ' + \
        self.shopName + '\nShop Location ' + \
        self.shopLocation + '\ncustomers' + \
        self.customers + '\nSales' + \
        self.sales + '\nReturns' + \
        self.returns
    
    #def update_choice(self, shop_Name):
    #    sh1.shopName = shop_Name
    #update_choice("jer")

sh1 = ctuStock("Default", "Default", 0, 0, 0) #These are the 4 objects
sh2 = ctuStock("Default", "Default", 0, 0, 0)
sh3 = ctuStock("Default", "Default", 0, 0, 0)
sh4 = ctuStock("Default", "Default", 0, 0, 0)

#sh1.shopName = str(input("shops name"))
#print(sh1.shopName)



