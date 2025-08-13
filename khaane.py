

temperature = int(input("What is the temperature? "))
window = input("window is 0(close) or 1(open)? ")
#0 = off and 1 = on
coolingـsystem = 0
heatingـsystem = 0

if temperature < 18 and window == 0:
    heatingـsystem = 1
elif temperature > 25 and window == 0:
    coolingـsystem = 1
else:
    print("temperature is good!")
    
print()
print("#0 = off and 1 = on")
print("temperature = " + str(temperature))
print("window = " + str(window))
print("coolingـsystem = " + str(coolingـsystem))
print("heatingـsystem = " + str(heatingـsystem))