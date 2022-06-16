#Speed Tracker
file = open("carCrimes.csv","a")

time1 = float(input("Enter the time in hours passing cam1 : "))
time2 = float(input("Enter the time in hours passing cam2 : "))
distance = float(input("Enter the distance in miles between cam1 and cam2 : "))
numPlate = input("Enter the number plate : ")

timePassed = time2 - time1
speed = distance / timePassed

plateType = []

for char in numPlate:
    plateType.append(char.isalpha())

if (plateType[0] == True) and (plateType[1] == True) and (plateType[2] == False) and (plateType[3] == False) and (plateType[4] == True) and (plateType[5] == True) and (plateType[6] == True):
    check = "Valid"
    print("That is a valid number plate")
else:
    print("That number plate is invalid")
    check = "Invalid"

print(f"\nThe car travelled at {speed} miles per hour.")

if speed > 70:
    file.write((numPlate+","+str(speed)+","+str(check)))
elif check == "Invalid":
    file.write((numPlate+","+str(speed)+","+str(check)))

file.close()
