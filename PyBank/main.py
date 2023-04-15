#Import de csv.file
import csv

with open ("Resources/budget_data.csv") as file:
    csv_reader = csv.reader(file) #Save the file as a variable
    notes=list(csv_reader) #Save the file as as list
    #print(notes)


#def getData(notes):
#Define variables
sum = 0
dif1 = 0
dif2 = 0
g_dec=0
g_in=0
for i in range(1,len(notes)-1):
    sum = int((notes[i][1])) + sum
    if int((notes[i][1])) > int((notes[i+1][1])): #The if conditonals will help me to find the greatest increase/decrease
        if int((notes[i+1][1])) >= 0: #Find if the value is greater than zero or lower, that is beacuse the maths will change.
            dif1 = (int((notes[i][1])) - int((notes[i+1][1])))*(-1)
        else:
            if int((notes[i][1])) >= 0:
                dif1 = ((int((notes[i][1]))) + (int((notes[i+1][1])))*(-1))*(-1)
            else:
                dif1 = ((int((notes[i][1])))*(-1) + int((notes[i+1][1])))
    else:
        if int((notes[i+1][1])) >= 0: 
            dif1 = (int((notes[i][1])) - int((notes[i+1][1])))*(-1)
        else:
            if int((notes[i][1])) >= 0:
                dif1 = ((int((notes[i][1]))) + (int((notes[i+1][1])))*(-1))*(-1)
            else:
                dif1 = ((int((notes[i][1])))*(-1) + int((notes[i+1][1])))
    #calculate de differences of values
    if g_dec < dif1:
        g_dec=dif1
        month_dec = (notes[i+1][0]) 

    elif g_in > dif1:
        g_in = dif1
        month_in = (notes[i+1][0])

    dif2 = dif1 + dif2
    #print(type(int(notes[i][1])))

#print(str(average))
print(type(len(notes)))
#Calculate the average of changes between the values.
average = dif2/(len(notes)-2)
#print(month_dec)


print("Financial Analysis")
print("--------------------------")
print("Total Months: " + str(len(notes)-1)) #The total number of months included in the dataset
print("Total:" + str(sum))
print("Average Change:" + str(round(average,2)))
print("Greatest Decrease in Profits: " + month_dec + "($" + str(g_dec) + ")")
print("Greatest Increase in Profits: " + month_in + "($" + str(g_in) + ")")


#creating a text file with the command function "w"
f = open("analysis/Results_PyBank.txt", "w")
#This "w" command can also be used create a new file but unlike the the "x" command the "w" command 
# will overwrite any existing file found with the same file name.

f.write("Financial Analysis \n")
f.write("--------------------------\n")
f.write("Total Months: " + str(len(notes)-1) + "\n") #The total number of months included in the dataset
f.write("Total:" + str(sum)+ "\n")
f.write("Average Change:" + str(round(average,2))+ "\n")
f.write("Greatest Decrease in Profits: " + month_dec + "($" + str(g_dec) + ")\n")
f.write("Greatest Increase in Profits: " + month_in + "($" + str(g_in) + ") \n")