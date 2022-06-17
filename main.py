fc = "First Class"
ch = "Coach"
fcRow1 = "Row FCA"
fcRow2 = "Row FCB"
row1 = "Row A"
row2 = "Row B"
row3 = "Row C"
row4 = "Row D"
opA = "A Open"
opB = "B Open"
opC = "C Open"
opD = "D Open"

fh = open('airlineseats.txt', 'w')
fh.write(
    "========== %s ========== \n        | %-7s | %-7s |\n" % (fc, fcRow1 , fcRow2 ))

fh = open('airlineseats.txt', 'a')
for i in range(4):
    fh.write("%-7s | %-7s | %-7s |\n" % (("seats %d" % (i)), opA, opB))

h = open('airlineseats.txt', 'a')
fh.write("========== %s ========== \n        | %-7s | %-7s | %-7s | %-7s |\n" %
         (ch, row1, row2, row3, row4))

fh = open('airlineseats.txt', 'a')
for i in range(10):
    fh.write("%-7s | %-7s | %-7s | %-7s | %-7s |\n" % (
        ("seats %d" % (i)), opA, opB, opC, opD))
fh.close()
#smm

# This is where we declare the values for the tickets and discounts
coachTic = float(199)
firstClassTic = float(500)
discount = .20
seniorAge = 65
kidAge = 7
totalPrice = 0

# This is where we need to do the inputs for passenger and ticket info into an array

#travel data SMM
## year = 0
## minMonth = 1
## maxMonth = 12
# we need to fix this so that the minDay stays as 1, but the maxDay changes based on the month
## minDay = 1
## maxDay = 31
numTravelers = 0
maxSeats = 5
minSeats = 0
i = 1
prefClass = ("", "First Class", "Coach")
remainingSeats = maxSeats
## travDestination = ("", "FL", "CA", "NY", "TX", "VA")

#date and number of traveilers
numTravelers = input("Hello and welcome to Chaffey Airlines.\n Please enter number of travelers or type 'q' to quit: ")
while numTravelers != "q":
  while True:
    try:
      seats = int(numTravelers)
      if(seats > minSeats) and (seats <= remainingSeats):
        break
      else:
        numTravelers = input(" Please enter a two digit whole number between 1 and 48: ")
    except ValueError:
      numTravelers = input(" Please enter a two digit whole number between 1 and 48: ")
      
# OPTIONAL
## year = int(input("\nEnter the four digit travel year: "))
# Input limit on year to 2019 or 2020
## month = int(input("Enter the two digit travel month: "))
# create list of months
## day = int(input("Enter two digit travel day: "))
# create a list that matches to the list of months with the correct amount of days i.e. 28 days, 30 days, or 31 days.
# create list of all 50 states two letter codes
## travelDes = int(input("Travel destination- 1-FL, 2-CA, 3-NY, 4-TX, 5-VA: "))
# this is where we take the info for each traveller based on the number of travelers
  numTravelers = int(numTravelers)
#this is the loop for getting the costs for the tickets.
  while i <= numTravelers:
      travName = str(input("\nWhat is the traveler's Name: "))
      travAge = int(input("Age of traveler: "))
      youPrefClass = int(input("Preferred Class- 1 First Class or 2 Coach: "))
      i = i + 1
      while True:
        if youPrefClass == prefClass(1):
            priceTic = firstClassTic
            if travAge <= kidAge or travAge >= seniorAge:
                priceAge = priceTic - (priceTic * discount)
                print(">>Discount applied.")
                break
            elif travAge > kidAge and travAge < seniorAge:
                priceAge = priceTic
                break
        elif youPrefClass == prefClass(2):
            priceTic = coachTic
            if travAge <= kidAge or travAge >= seniorAge:
                priceAge = priceTic - (priceTic * discount)
                print(">>Discount applied.")
                break
            elif travAge > kidAge and travAge < seniorAge:
                priceAge = priceTic
                break
        else:
          prefClass1 = int(input("Please choose Preferred Class- 1 First Class or 2 Coach: "))
      print(" Traveler", travName)
      print(" Traveling", prefClass[prefClass1])
      print(" General Ticket price: $%6.2f" % (priceAge))
      totalPrice = totalPrice + priceAge
      remainingSeats = remainingSeats - 1
    ## travDate = str(print("\nTravel Date is: ", month, "/", day, "/", year))
    ## print("Traveling to", travDestination[travelDes])
  print("Total cost of ticket(s) will be $%6.2f." % (totalPrice))
  if remainingSeats > minSeats:
    numTravelers = input("\nHello and welcome to Chaffey Airlines.\n Please enter number of travelers or type 'q' to quit: ")
    i = 1
    totalPrice = 0
  else:
    numTravelers = "q"
#SMM
if remainingSeats <= minSeats:
  print("\nFlight full")
# This is the table that needs to be somehow put into an array

# here is where we manipulate the array

# This is where we let passengers make changes to array

# This is where we give totals for ticket prices and verification of seats that might loop back to making changes

#This is where we checkout and make change based on total

# link to how to keep variables persistent in memory https://stackoverflow.com/questions/6687660/keep-persistent-variables-in-memory-between-runs-of-python-script