#!/usr/bin/python3

# Program to be used to calculate the amount the needs to be paid for a restaurant bill based on individual
# consumption.

opt_var = input("How would you like to split? Type '1' for item per person, Type '2' for Drinks and Food(shared) separate: ")

def per_item():

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
            items -= 1
        names[person] = sum(amt_1)
        num_ppl -= 1


    tax_pp = (tax/len(names))
    serv_chrg_pp = (serv_chrg/len(names))

    for person in names:
        tot_bill_pp = names[person] + tax_pp + serv_chrg_pp
        names[person] = tot_bill_pp

        su = sum(names.values())
    if int(su) != int(total_bill):
        print("There is an error in your calculations!")
    else:
        print("The amount is correct, please pay as per your names as indicated")
    return print(names)

def food_drink_sep():
    total_bill = float(input("What is the total bill amount? "))
    food_bill = int(input("How much was the food bill? "))
    drink_bill = int(input("How much was the drinks bill? "))

    tax = float(input("What is the total tax? "))
    #print(tax)
    serv_chrg = float(input("What is the total service charge? "))
    #print(serv_chrg)

    non_alc = int(input("How many people didnt drink? "))
    alc = int(input("How many people did drink? "))

    alc_bill = (drink_bill+food_bill)/alc
    non_alc_bill = (alc_bill - (food_bill+drink_bill))/non_alc

    tax_pp = tax/(alc+non_alc)
    serv_chrg_pp = serv_chrg /(alc+non_alc)

    alc_amt =  alc_bill + tax_pp + serv_chrg_pp
    non_alc_amt = non_alc_bill + tax_pp + serv_chrg_pp

    if (alc_amt + non_alc_amt) != total_bill:
        return print("Please check calculations")
    return print("The bill for the drinkers(who also ate) is {} and the bill of the tee-totalers is {}".format(alc_amt, non_alc_amt))

if opt_var == '1':
    per_item()
elif opt_var == '2':
    food_drink_sep()
else:
    print("Put in a valid option please, either 1 or 2")
