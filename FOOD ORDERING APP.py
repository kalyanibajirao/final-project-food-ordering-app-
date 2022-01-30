#!/usr/bin/env python
# coding: utf-8

# # FOOD ORDERING APP

# In[ ]:


import random
class Restaurant:
    def __init__(self):
        pass
    
    
class Admin():
    
    def __init__(self):
        pass
   
    def Admin_log_in(self):
        id = input("Enter your id:")
        password = input("Enter your password:")
        if password == password:
            print("***Hello Admin***")
        else:
            print("Wrong password")
    
    
    def Edit_food_items(self):
        food_items = [{'Name':'Tandoori Chicken','Price':'INR 240','Food Id':0,'Qty':'4 Piece'},
                      {'Name': 'Vegan Burger','Price':'INR 320','Food Id':1,'Qty':'1 Piece'},
                      {'Name':'Truffle Cake','Price':'INR 900','Food Id':2,'Qty':'500gm'}]
    
        print(food_items)
 
        choice = int(input(" 1. Add new food item \n 2. Edit food item \n 3. Delete food item \n 0. Exit \n Enter your choice here:"))
        if choice == 1:
            Add_new_food_item = input("Enter new food item {}:")
            food_items.append(Add_new_food_item )
            print(food_items)
        elif choice == 2:
            Edit_food_item = input("Enter food id:")
            Name = input("Enter food name:")
            Price = int(input("Enter Price:"))
            return food_items
        elif choice == 3:
            Delete_food_item = food_items.pop(int(input("Please enter food id:")))
            print(food_items)
        else:
            print("Invalid choice Please choose option from below:")
            
            
class User():
    def __init__(self):
        pass
        
    def user_registration(self):
        Full_Name = input("Enter your full name:")
        Phone_Number = int(input("Enter your phone number:"))
        Email = input("Enter your Email:")
        Address = input("Enter your Address:")
        Password = input("Enter your password:")
        
    
    def user_log_in(self):
        otp_on_system = str(random.randint(1000,2000))
        print('Mobile Phone Messege ='+ otp_on_system)
        otp_from_user = input('Enter otp')
        if otp_from_user == otp_on_system:
            self.loggedin = True
            print('Successfully Logged in') 
            print('***WELCOME_TO_FOOD_ORDERING_APP***')
        else:
            print('Wrong otp')

    
    def Place_New_Order(self):
        food_items = [{'Name':'Tandoori Chicken','Price':'INR 240','Food Id':0,'Qty':'4 Piece'},
                      {'Name': 'Vegan Burger','Price':'INR 320','Food Id':1,'Qty':'1 Piece'},
                      {'Name':'Truffle Cake','Price':'INR 900','Food Id':2,'Qty':'500gm'}]
        print(food_items)
        Choose_Order = int(input("Enter food id:"))
        if Choose_Order == 0:
            print("{'Name':'Tandoori Chicken','Price':'INR 240','Food Id':0,'Qty':'4 Piece'}")
        elif Choose_Order == 1:
            print("{'Name': 'Vegan Burger','Price':'INR 320','Food Id':1,'Qty':'1 Piece'}")
        elif Choose_Order == 2:
            print("{'Name':'Truffle Cake','Price':'INR 900','Food Id':2,'Qty':'500gm'}")
        place_order = int(input(" 1. Yes \n 2. No \n Placed_order \n Enter your choice here:"))
        if place_order == 1:
            address = input("Please confirm your address: ")
            
            Payment_Details = int(input(" 1.CASH ON DELIVERY \n 2. CREDIT/DEBIT CARD \n 3. PHONEPAY/GOOGLE PAY/BHIM UPI \n 4. NET BANKING \n Enter your choice here:"))
            print("Your order will be delivered in 30 mins.")
            
        else:
            print("Order cancelled.")
    def Order_History(self):     
        Order_History =[] 
        Choose_Order = int(input("Enter food id which you orderd:"))
        if Choose_Order == 0:
            print("{'Name':'Tandoori Chicken','Price':'INR 240','Food Id':0,'Qty':'4 Piece'}")
        elif Choose_Order == 1:
            print("{'Name': 'Vegan Burger','Price':'INR 320','Food Id':1,'Qty':'1 Piece'}")
        elif Choose_Order == 2:
            print("{'Name':'Truffle Cake','Price':'INR 900','Food Id':2,'Qty':'500gm'}")
            
            Order_History.append(Choose_Order)
            print(Order_History)
            
        else:
            print("Your Order History will display here")
            
            
    def Update_Profile(self):
        choice = int(input("1. Edit Name \n 2. Edit Number \n 3. Edit Email Address \n 4. Edit Address \n 0 Exit \n Enter your choice here"))
        if choice == 1:
            Edit_name = input("Please Enter your name:")
        elif choice == 2:
            Edit_Number = int(input("Please Enter your number:"))
        elif choice == 3:
            Edit_Email_Address = input("Please Enter your Email Address:")
        elif choice == 4:
            Edit_Address = input("Please Enter your Address:")
        else:
            print("Invalid choice Please choose option from below:")
            
    
    
    

AdminObj = Admin()
UserObj = User()


while True:    
    choice = int(input(" 1. Admin \n 2. User \n 3. Which one are you:"))
    if choice == 1:
        AdminObj.Admin_log_in()
        AdminObj.Edit_food_items()

    else:
        choice == 2
        print("Please Register yourself")
        UserObj.user_registration()
        UserObj.user_log_in()
        choice = int(input(" 1.Place_New_Order \n 2.Order_History \n 3.Update_Profile \n 0.Exit \n  Enter your choice here:"))
        if choice == 1:
            UserObj.Place_New_Order()
        elif choice == 2:
            UserObj.Order_History()
        elif choice == 3:
            UserObj.Update_Profile()
        elif choice == 0:
            print("Thank You for Visiting!!! See You Soon!!!")
            break
        else:
            print("Invalid choice Please choose option from below:")          

    
   
    


# In[ ]:




