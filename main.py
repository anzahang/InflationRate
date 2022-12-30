#Date: October 5, 2022
#CompSci 1026A-003 - Assignment #1
#Name: Andrew Zhang
#This is a program that accepts all the expenditures of the current and previous year as input and calculates the personal
#Inflation rate between the two years as well as determines the type of inflation and outputs these to console.

#Get input for current year.
year = input("Please enter the year that you want to calculate the personal interest rate for: ")

#Get input for number of expenditures.
numExpenditures = int(input("Please enter the number of expenditure categories: "))

#Declare accumulators for previous current year expenditures.
previous = 0
current = 0

#Prompt for expenditures of previous and current year for numExpenditure times.
for i in range(numExpenditures):
    inputPrevious = int(input("Please enter expenses for previous year: "))
    #Accumulate expenditures of previous year.
    previous = previous + inputPrevious
    inputCurrent = int(input("Please enter the expenses for year of interest: "))
    # Accumulate expenditures of current year.
    current = current + inputCurrent

#Implement personal inflation rate formula.
inflationRate = (current - previous) / current * 100

#Catch the case such that current year expenses is lower than previous year expenses(inflationRate is negative).
if(inflationRate < 0):
    inflationRate = 0
else:
    #Output the year and inflation rate of that year.
    print("Personal inflation rate for " + year + " is " + str(inflationRate) + "%")

#Declare type of inflation.
typeOfInflation = ""

#Determine which type of inflation.
if(inflationRate<3):
    typeOfInflation = "Low"
elif(inflationRate>=3 and inflationRate < 5):
    typeOfInflation = "Moderate"
elif(inflationRate>=5 and inflationRate < 10):
    typeOfInflation = "High"
else:
    typeOfInflation = "Hyper"

#Output the type of inflation.
print("Type of Inflation: " + typeOfInflation)
