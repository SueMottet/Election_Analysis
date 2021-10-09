#Add our dependencies
import csv
import os

# Assign a variable for the file to load and the path
file_to_load = os.path.join('Resources', 'election_results.csv')
#create a filename variable to a direct or indirect path to the file
file_to_save = os.path.join('analysis', 'election_analysis.txt')

#initialize a total vote counter
total_votes = 0

#Declare a new list
candidate_options = []

# Declare empty dictionary for votes
candidate_votes = {}

# Declare a variable that holds an empty string value for the winning candidate
winning_candidate = ""
# Declare a variable for the "winning count" equal to zero
winning_count = 0
# Declare a variable for the "winning percentage" equal to zero
winning_percentage = 0 

# Open the election results and read the file.
election_data = open(file_to_load, 'r')
with  open(file_to_load, 'r') as election_data:
    # read the file object with the reader function
    file_reader = csv.reader(election_data)
    
    #print the header row
    headers = next(file_reader)
    #print(headers)

    for row in file_reader:
       
        
        #2. add to the total vote count
        total_votes += 1
        
        # print the candidate name for each row
        candidate_name = row[2]
  
        
        # add the candidate name to the candidate list if the candidate name not in the list
           
        if candidate_name not in candidate_options:
                        #Add it to the list of candidates
            candidate_options.append(candidate_name)
            
            # reset counter for new candidate
            candidate_votes[candidate_name] = 0
        
        # Add a vote to that candidate's count
        candidate_votes[candidate_name] += 1             
    
with open(file_to_save, "w") as file_to_save:       
    # print the final vote count to the terminal
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    
    print (election_results, end="")
    
    file_to_save.write(election_results)

    #Determine the percentage of votes for each candidate by looping through counts
    #1 iterated through the candidate list
    for candidate_name in candidate_votes:
      
     # 2. retrieve vote count of a candidate
        votes = candidate_votes[candidate_name]
            
     # 3. calculate the percentage of votes
        vote_percentage = float(votes) / float(total_votes) * 100
            
    # 4. print the candidate name and percentage of votes
    #print(f"{candidate_name}: received {round(vote_percentage, 1)}% of the vote.")          
    # to doL print out each candidatel name, vote percentage and vote count

        candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

        print(candidate_results)

        file_to_save.write(candidate_results)
   
    
    # 1. Determine winning vote count and candidate
    if (votes > winning_count) and (vote_percentage > winning_percentage):
        # 2. if true then set winning_count = votes and winning_percent = vote_percentage
        winning_count = votes
        winning_percentage = vote_percentage
        # 3. Set the winning_candidate equal to the candidate's name
        winning_candidate = candidate_name
    
        winning_candidate_summary = (
            f"-------------------------\n"
            f"Winner: {winning_candidate}\n"
            f"Winning Vote Count: {winning_count:,}\n"
            f"Winning Percentage: {winning_percentage:.1f}%\n"
            f"-------------------------\n")
        print(winning_candidate_summary)
        file_to_save.write(winning_candidate_summary)    
#3. Print the total votes
#print(total_votes)

# print the candidate list
#print (candidate_options)

#print the candidate vote dictionary
#print(candidate_votes)  

#close the file.
election_data.close
#election_analysis.close()