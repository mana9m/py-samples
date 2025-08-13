

temperature = int(input("What is the temperature? "))
window = "whatever"

coolingـsystem = "off"
heatingـsystem = "off"

if temperature < 18:
    heatingـsystem = "on"
    print("close the window. ")
    window = "close"

if temperature > 25:
    coolingـsystem = "on"
    print("close the window. ")
    window = "close"

if 25 > temperature > 18:
    print("temperature is good!")



print("\n\ntemperature = " + str(temperature))
print("window = " + str(window))
print("coolingـsystem = " + str(coolingـsystem))
print("heatingـsystem = " + str(heatingـsystem))