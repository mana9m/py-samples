


bread = 10
tomato = 5
cheese = 15
meat = 1

s = input("Do you want to make a sandwich? ")
if s == "yes" :
    print("Ok, let`s make it!")
    b = int(input("How many loaves of bread do you want? "))
    br = b * bread
    t = int(input("How many tomatoes do you want? "))
    to = t * tomato
    ch = int(input("How many slices of cheese do you want? "))
    che = ch * cheese
    m = int(input("How many grams of meat do you want? "))
    me = m * meat
    sa = br + to + che + me
    print("You have to pay " + str(sa) + " thousand tomans for this sandwich.")
else:
    print("Ok, bye")