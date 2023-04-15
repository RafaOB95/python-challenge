import pandas as pd #import pandas
df = pd.read_csv('Resources/election_data.csv') #save my csv

votos = df['Candidate'].value_counts() #save all the values od the column Candidate in my variable

voto_max = votos.max() #Serach de max value of the votes
votos[votos==voto_max] #Searh the person that has the max amount of votes.

a=round((votos[0]/(len(df)-1) *100),2) #Calculate de percentage of votes.
b=round((votos[1]/(len(df)-1) *100),2)
c=round((votos[2]/(len(df)-1) *100),2)

#Print
print('Election results:')
print("------------------------------------------")
print("Total Votes:" + str(len(df)-1))
print("------------------------------------------")
print("Candidate ---------------- votes")
print("")
print(votos)
print("------------------------------------------")
print("Percentage votes")
print(str(votos[0]) +" ------> " + str(a) + "%" + '\n')
print(str(votos[1]) +" ------> " + str(b) + "%" + '\n')
print(str(votos[2]) +" ------> " + str(c) + "%" + '\n')
print("------------------------------------------")
print("Winner:")
print(votos[votos==voto_max])



#creating a text file with the command function "w"
f = open("analysis/Results_PyPoll.txt", "w")
#This "w" command can also be used create a new file but unlike the the "x" command the "w" command 
# will overwrite any existing file found with the same file name.

f.write('Election results:\n')
f.write("------------------------------------------ \n")
f.write("Total Votes:" + str(len(df)-1) + '\n')
f.write("------------------------------------------\n")
f.write(str(votos) + '\n')
f.write("------------------------------------------\n")
f.write("Percentage votes\n")
f.write(str(votos[0]) +" ------> " + str(a) + "%" + '\n')
f.write(str(votos[1]) +" ------> " + str(b) + "%" + '\n')
f.write(str(votos[2]) +" ------> " + str(c) + "%" + '\n')
f.write("------------------------------------------ \n")
f.write("Winner: \n")
f.write(str(votos[votos==voto_max]) + "\n")
f.write("------------------------------------------ \n")

