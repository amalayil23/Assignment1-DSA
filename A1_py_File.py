#!/usr/bin/env python
# coding: utf-8




class Products():
    def __init__(self):
        self.data = open("product_data.txt","r")
        self.products = []
        for i in self.data.readlines():
            self.products.append(i.strip().split(", "))
        self.data.close()
        
    #Function to print all the products added in the array.
    #Time complexity O(n)
    def printProducts(self):
        for k in self.products:
            print("\n", k)
    
    def printHead(self, n = 5):
        for i in range(n):
            print("\n",self.products[i])
    
    #Function to remove a product from the array. Takes the product ID as argument. 
    #Time complexity O(n)
    def removeProduct(self, ID):
        for i in self.products:
            if i[0] == ID:
                self.products.remove(i)
                return print("Item {} removed".format(i))
    
    #Function to add a new product to the array. Function checks the new item provided as the
    #arguments had exactly 4 attributes. 
    #Time complexity O(1)
    def addProduct(self, itemDetail):
        if len(itemDetail) != 4:
            print("Please provide all product details")
        else:
            self.products.append(itemDetail)
        print("Product added: {}.".format(self.products[len(self.products)-1]))
            
    #Function to update product detail.Functions needs ID to be passed as argument with a array of 
    #new attributes for the item
    #Time complexity O(n)
    def updateProduct(self, ID , new):
        if len(new)!= 4:
            print("Please provide all product details")
        else:            
            for i in range(0,len(self.products)):
                if self.products[i][0] == ID:
                    self.products[i] = new
                    return print("Product {} updated!".format(self.products[i][0]))
            print("Provided product ID doesn't exist")
    
    #Time complexity O(n)
    def searchProduct(self, item):
        for i in self.products:
            if str(item) in i[:-2]:
                return print("Product found {}".format(i))
        return print("Product not found. Please use a valid name or ID for searching.")

    
    #Bubble sort algorithm, Time complexity O(n^2)
    def sortBubble(self):
        n= len(self.products)
        for i in range(0,n-1):
            for j in range(0,n-i-1):
                if (float(self.products[j][2])) > (float(self.products[j+1][2])):
                    temp = self.products[j]
                    self.products[j] = self.products[j+1]
                    self.products[j+1] = temp
        return self.products
                        
    def sortBubbleDes(self):
        n= len(self.products)
        for i in range(0,n-1):
            for j in range(0,n-i-1):
                if (float(self.products[j][2])) < (float(self.products[j+1][2])):
                    temp = self.products[j+1]
                    self.products[j+1] = self.products[j]
                    self.products[j] = temp
        return self.products
                
product = Products()

product.printHead()

#inserting a new product
product.addProduct(["18086","Laptop XCFG", "1200",'Electronics'])


#Updating the product
product.updateProduct('18086',["18086","Laptop ABC", "1000",'Electronics'])


#Removing product
product.removeProduct('18086')


#Searching product that was removed on previous step. Making sure it is removed.
product.searchProduct('LaptopABC')


#Search using product name
product.searchProduct('Camera SBBHC')


#Search using ID
product.searchProduct(16041)


# Here i am adding some additional products to the array to make the time analysis more visible. 
import random
n = 1773
for i in range(5000):
    product.addProduct([n,"B",random.randint(100,1000),"C"])
    n+=1

import time
start = time.process_time()
product.sortBubble()
end = time.process_time()
timetaken = end-start
product.printHead()

print("\nTime taken to sort the orginal array is {} seconds.".format(timetaken))
print("\nThis can be considered average case")


product.sortBubbleDes() #Array is sorted in reverse order
print("Array reversed:")
product.printHead()
#Now the array is reverse sorted. 
start = time.process_time()
product.sortBubble()
end = time.process_time()
timetaken = end-start
print("\nArray now:")
product.printHead()

print("\n \n It took {} seconds for the algorithm to sort an reverse sorted array. This can be considered the worst case scenario".format(timetaken))


start = time.process_time()
product.sortBubble()
end = time.process_time()
timetaken = end-start
product.printHead()


print("\n\nIt took {} seconds, and this is the best case scenario".format(timetaken))


x = input("Press any key to exit..")

