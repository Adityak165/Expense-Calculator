totalamt=float(input("Enter the total amount you want to spend : "))
totalcat=int(input("Enter how many categories you want: "))
categories={}
allocated_sum=0
for i in range(totalcat):
    name = input(f"Enetr the {i+1} categorie: ")
    amount = int(input(f"enter the amount you want to allot to {i+1} categorie: "))
    allocated_sum += amount
    categories[name]= amount

print("All the categories is alloted with amount")
print("here is your list:")
remainingamt=totalamt-allocated_sum
categories["remaining amount"]= remainingamt
for cat,amt in categories.items():
    print(f"{cat}:{amt}$")
print(f"total alloted amount is : {allocated_sum}")

expenses=[]
while True:
    categorie =input("Enter the categorie from which you spend or wirte done to stop: ").lower()
    if(categorie == "done"):
        break
    if categorie not in categories:
        print("entered catories is invalid")
        continue
    amount=float(input("enter the amount you spent: "))
    item=input("what did you buy : ")
    categories[categorie] -= amount

    expenses.append({"category" : categorie,
                    "amount ": amount,
                    "items": item})
    print(f" recored ${amount} is spent on {item} from {categorie} catorie ")

print("Here is your remaining balance ")
for cat,amt in categories.items():
    print(f"{cat} : {amt}$")

while True:
    cat_to_trasfer = input("Enter the category from which you want to transfer money (or 'no' to stop): ").lower()

    if cat_to_trasfer == 'no':
        break
    where = input("Where do you want to transfer it? ").lower()
    if cat_to_trasfer and where in categories:
        amtt = float(input("Enter how much amount: ₹"))

        amount_left = categories[cat_to_trasfer]

        if amount_left > 0 or where in categories:
            amount_left -= amtt
            categories[where] += amtt
            categories[cat_to_trasfer] = amount_left

            print(f"✅ ₹{amtt} is transferred from {cat_to_trasfer} to {where}")
    else:
        print("❌ Wrong category entered.")

print("Here is your remaining balance: ")
for cat,amt in categories.items():
    print(f" {cat} : ${amt}")