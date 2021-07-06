import os
import csv

election_csv = os.path.join('Resources', 'election_data.csv')

total_votes = [] 
khan_votes = 0
correy_votes = 0
li_votes = 0
o_votes = 0


with open(election_csv, 'r') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader)

    for row in csvreader:

        total_votes.append(row[0])

        vote_count = len(total_votes)
        
        if row[2] == "Khan": 
            khan_votes +=1
        elif row[2] == "Correy":
            correy_votes +=1
        elif row[2] == "Li": 
            li_votes +=1
        elif row[2] == "O'Tooley":
            o_votes +=1

        

khan_percent = round((float(khan_votes)/vote_count) * 100)
correy_percent = round((float(correy_votes)/vote_count) * 100)
li_percent = round((float(li_votes)/vote_count) * 100)
o_percent = round((float(o_votes)/vote_count) * 100)

candidates = ["Khan", "Correy", "Li", "O'Tooley"]
votes = [khan_votes, correy_votes, li_votes, o_votes]

candidates_and_votes = dict(zip(candidates,votes))
winner = max(candidates_and_votes, key = candidates_and_votes.get)

print("Election Results")
print("---------------------------------------------------------------")
print("Total Votes: " + str(vote_count))
print("---------------------------------------------------------------")
print("Khan: " + str(khan_percent) + "% " + "(" + str(khan_votes) + ")")
print("Correy: " + str(correy_percent) + "% " + "(" + str(correy_votes) + ")")
print("Li: " + str(li_percent) + "% " + "(" + str(li_votes) + ")")
print("O'Tooley: " + str(o_percent) + "% " + "(" + str(o_votes) + ")")
print("---------------------------------------------------------------")
print("Winner: " + str(winner) )
print("---------------------------------------------------------------")


output_path = os.path.join("analysis", "analysis.txt")

with open(output_path, 'w') as txtfile:

    txtfile.write("Election Results" + "\n")
    txtfile.write("---------------------------------------------------------------" + "\n")
    txtfile.write("Total Votes: " + str(vote_count) + "\n")
    txtfile.write("Khan: " + str(khan_percent) + "% " + "(" + str(khan_votes) + ")" + "\n")
    txtfile.write("Correy: " + str(correy_percent) + "% " + "(" + str(correy_votes) + ")" + "\n")
    txtfile.write("Li: " + str(li_percent) + "% " + "(" + str(li_votes) + ")" + "\n")
    txtfile.write("O'Tooley: " + str(o_percent) + "% " + "(" + str(o_votes) + ")" + "\n")
    txtfile.write("---------------------------------------------------------------" + "\n")
    txtfile.write("Winner: " + str(winner) + "\n")
    txtfile.write("---------------------------------------------------------------" + "\n")