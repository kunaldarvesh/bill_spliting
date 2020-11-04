#!/usr/bin/python3

# Program to be used to calculate the amount the needs to be paid for a restaurant bill based on individual
# consumption.

total_bill = float(input("What is the total bill amount? "))
print("Total Bill amount is ${}".format(total_bill))

tax = float(input("What is the total tax? "))
#print(tax)
serv_chrg = float(input("What is the total service charge? "))
#print(serv_chrg)

num_ppl = int(input("How many people are spliting? "))
print("{} are spliting".format(num_ppl))

names = {}

while num_ppl > 0:
    person = str(input("Please enter your Name: "))
    items = int(input("How many items did you eat? "))
    amt_1 = []
    while items > 0:
        cst = float(input("How much was the cost per item for you? "))
        amt_1.append(cst)
        print(amt_1)
        items -= 1
    names[person] = sum(amt_1)
    print(person)
    num_ppl -= 1
#print(names)

tax_pp = (tax/len(names))
#print(tax_pp)
serv_chrg_pp = (serv_chrg/len(names))
#print(serv_chrg_pp)

for person in names:
    tot_bill_pp = names[person] + tax_pp + serv_chrg_pp
    names[person] = tot_bill_pp
print(names)

su = sum(names.values())
if int(su) != int(total_bill):
    print("There is an error in your calculations!")
else:
    print("The amount is correct, please pay as per your names as indicated")
