

temperature = int(input("What is the temperature? "))
window = "whatever"

cooling_system = "off"
heating_system = "off"

if temperature < 18:
    heating_system = "on"
    print("close the window. ")
    window = "close"

if temperature > 25:
    cooling_system = "on"
    print("close the window. ")
    window = "close"

if 25 > temperature > 18:
    print("temperature is good!")



print("\n\ntemperature = " + str(temperature))
print("window = " + str(window))
print("cooling_system = " + str(cooling_system))
print("heating_system = " + str(heating_system))