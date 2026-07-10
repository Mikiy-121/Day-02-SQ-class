bill_total = float(input("total bill: "))
people = int(input("number of people: "))

customer  = [input(f"Enter the name of person {i+1}: ") for i in range(people)]

def split_bill(total, people, tip_rate=0.10):
    total_with_tip = total + (total * tip_rate)
    return total_with_tip / people

share = split_bill(bill_total, people)

for name in customer:
    print(f"{name} has to pay ETB {share:.2f}")