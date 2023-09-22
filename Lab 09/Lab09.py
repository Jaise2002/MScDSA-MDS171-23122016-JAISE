class ExpenseTracker:  
    def __init__(self):  
        self.transactiondetails = {"details": []}

    def transactiondetail(self):  
        for i in open("D:\\github\\MScDSA-MDS171-23122016-JAISE\\Lab 09\\expenses and income.csv", "r+").readlines():
            line = i.strip().split(",")  
            if line[0]!="Expense Category":
                transaction = {"details":[]}
                    
                self.transactiondetails["details"].append(transaction)

    def total(self):
        total_income = 0
        total_expense = 0
        for value in self.transactiondetails["details"]:
            if value["type"] == "Income":
                total_income += value["amount"]
            elif value["type"] == "Expense": 
                total_expense += value["amount"]
        print("Total income:", total_income, "Total expense:", total_expense)
        return total_income, total_expense

    def addtransaction(self):  
        type = input("Enter the type (Expense/Income): ")
        expense_category = input("Expense Category: ")
        amount = int(input("Amount: "))  
        date = input("Enter date (dd/mm/yy): ")
        description = input("Enter the description: ")
        transaction = {
            "type": type,
            "category": expense_category,
            "amount": amount,
            "description": description,
            "date": date
        }
        self.transactiondetails["details"].append(transaction)

order = ExpenseTracker()
order.transactiondetail()

while True:
    print("1. Add New Transaction\n2. Calculate Total Income and Expense\n3. Exit")
    choice = int(input("Select your action: "))
    if choice == 1:
        order.addtransaction() 
    elif choice == 2:
        order.total()
    elif choice == 3:
        break
