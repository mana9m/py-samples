


s_base = float(input("Please write the small base: (m) "))
b_base = float(input("Please write the big base: (m) "))
high = float(input("Please write the high: (m) "))

area = (s_base + b_base) * high / 2

print("The area of that trapezoid is: " + str(area) + " (m)")


unit_price = 100

total_cost = area * unit_price

print("The cost you have to pay for tiling: " + str(total_cost) + " thousand tomans.")