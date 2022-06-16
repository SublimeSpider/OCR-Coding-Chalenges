print("""Metres to feet - 0
Feet to metres - 1
Grams to ounces - 2
Ounces to grams - 3
Kilograms to stones - 4
Stones to kilograms - 5
Litres to gallons - 6
Gallons to litres - 7\n""")

unit = int(input("Which conversion do you wish to use (0-7) : "))
Value = float(input("What number do you wish to convert : "))

if unit == 0:
    ans = Value * 3.28084
elif unit == 1:
    ans = Value / 3.28084
elif units == 2:
    ans = Value * 0.035274
elif units == 3:
    ans = Value / 0.035274
elif units == 4:
    ans = Value * 0.157473214283943
elif units == 5:
    ans = Value / 0.157473214283943
elif units == 6:
    ans = Value * 0.219969
elif units == 7:
    ans = Value / 0.219969

print(ans)
