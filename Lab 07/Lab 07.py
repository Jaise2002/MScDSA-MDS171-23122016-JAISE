import random#importing random function
menu=[["coffi",10],["chaya",20],["apple",30],["banana",40],["rice",50]]
orders=[]
print(menu)
def neworder():
    entry=int(input("enter your number of iteam you like to order :"))
    order={}
    orderid=''.join(str(random.randint(0,9))for i in range(5))
    #return int(orderid)
    
    order["OrderId"] = orderid
    orderid["iteams"]=[]
    for i in range(entry):
        print(menu)
        choice= input("Enter the Item Number from the provided list for Order Collection[Rice-0, Biriyani-1, Tea-2, Coffee-3]:\n ")
        Quantity= input("Enter the Quantity for the Placed Item:\n ")
        order["Items"].append({"Item_Number": choice, "Quantity": Quantity})
    
    orders.append(order)

def TotalBill():
    for order in orders:
        total = 0
        count = 0
        for item in order['Items']:
            total += int(item["Quantity"])*menu[int(item['Item_Number'])][1]
        print(order)
        print("*"*100)
        print("The Order provided is: ",orders)
        print("The total Price for the Order is: \n",total)
        print("*"*100)
    

while True:
    print("\nThe Restaurant Management\n")
    print("1. Select this option to create a New Order\n")
    print("2. Select this option to View Orders\n")
    print("3. Select this option to Exit\n")
    
    user_input = int(input("Enter the Option:"))
    
    if user_input == 1:
        neworder()
    elif user_input == 2:
        TotalBill()
    elif user_input == 3:
        exit()
    else:
        print("Please Enter a Valid Input!!!\n")

          
