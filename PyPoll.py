# import the csv and os modules.
import csv
import os
# dir (csv)

# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")
print(file_to_load)
exit()

file_to_load = "Resources/election_results.csv"

# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")
# Using the with statement open the file as a text file.
with open(file_to_save, "w") as txt_file:

# Write three counties to the file.
     txt_file.write("Counties in the Election\n--------------\nArapahoe\nDenver\nJefferson")


    # Write some data to the file.
    # txt_file.write("Hello World")




# Use the open statement to open the file as a text file.
# outfile = open(file_to_save, "w")
# Write some data to the file.
# outfile.write("Hello World")
# Close the file
# outfile.close()

# Using the open() function with the "w" mode we will write data to the file.
# open(file_to_save, "w")

# Open the election results and read the file.
# with open(file_to_load) as election_data:

    # Print the file object.
    # print(election_data)

# election_data = open(file_to_load, 'r')

# To do: perform analysis.

# Close the file.
# election_data.close()








# import os
# # dir (csv)
# # Assign a variable for the file to load and the path.
# file_to_load = os.path.join("Resources", "election_results.csv")

# # Create a filename variable to a direct or indirect path to the file.
# file_to_save = os.path.join("analysis", "election_analysis.txt")
# #initialize total vote counter
# total_votes = 0
# # initilizing  a list for candidates
# candidate_options = []
# candidate_votes = {}
# # Winning Candidate and Winning Count Tracker
# winning_candidate = ""
# winning_count = 0
# winning_percentage = 0
# # Open the election results and read the file.
# with open(file_to_load) as election_data:
#     # Read the file object with the reader function.
#     file_reader = csv.reader(election_data)
#   # Print each row in the CSV file.
#    # for row in file_reader:
#     #    print(row)
# #print the header row
#     headers = next(file_reader)
#     #print (headers)
#     # Print each row in the CSV file.
#     for row in file_reader:
#         total_votes = total_votes + 1
#         candidate_name = row[2]
#         if candidate_name not in candidate_options :
#             candidate_options.append(candidate_name)
#             candidate_votes[candidate_name] = 0
#         candidate_votes[candidate_name] += 1
# # Save the results to our text file.
# with open(file_to_save, "w") as txt_file:
#     # Print the final vote count to the terminal.
#     election_results = (
#         f"\nElection Results\n"
#         f"-------------------------\n"
#         f"Total Votes: {total_votes:,}\n"
#         f"-------------------------\n")
#     print(election_results, end="")
#     # Save the final vote count to the text file.
#     txt_file.write(election_results)
#     #print(candidate_votes)
#     #print(total_votes)
#     #print(candidate_options)
#     # Determine the percentage of votes for each candidate by looping through the counts.
#     # 1. Iterate through the candidate list.
#     for candidate_name in candidate_votes:
#         # 2. Retrieve vote count of a candidate.
#         votes = candidate_votes[candidate_name]
#         # 3. Calculate the percentage of votes.
#         vote_percentage = float(votes) / float(total_votes) * 100
#         candidate_results = (
#             f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
#         # Print each candidate's voter count and percentage to the terminal.
#         print(candidate_results)
#         #  Save the candidate results to our text file.
#         txt_file.write(candidate_results)
#         # 4. Print the candidate name and percentage of votes.
#         #print(f"{candidate_name}: received {vote_percentage:.2f}% of the vote.")
#         #To do: print out each candidate's name, vote count, and percentage of votes to the terminal.
#         # Determine winning vote count and candidate
#         # Determine if the votes is greater than the winning count.
#         if (votes > winning_count) and (vote_percentage > winning_percentage):
#             # If true then set winning_count = votes and winning_percent =
#             # vote_percentage.
#             winning_count = votes
#             winning_percentage = vote_percentage
#             # And, set the winning_candidate equal to the candidate's name.
#             winning_candidate = candidate_name

#     #  To do: print out the winning candidate, vote count and percentage to
#     #   terminal.
#     # print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

#         winning_candidate_summary = (
#         f"-------------------------\n"
#         f"Winner: {winning_candidate}\n"
#         f"Winning Vote Count: {winning_count:,}\n"
#         f"Winning Percentage: {winning_percentage:.1f}%\n"
#         f"-------------------------\n")
#     print(winning_candidate_summary)
#         # Save the winning candidate's name to the text file.
#     txt_file.write(winning_candidate_summary)   