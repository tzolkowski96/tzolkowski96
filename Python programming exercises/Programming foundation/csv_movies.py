import csv 

# Define a list of movie lists
movie_lists = [["Top Gun", "Risky Business", "Minority Report"], 
               ["Titanic", "The Revenant", "Inception"], 
               ["Training Day", "Man on Fire", "Flight"]]

# Define the name of the output file
file_name = "movies.csv" 

# Open the output file in write mode and write the movie lists to it using the csv module
with open(file_name, "w") as file: 
    writer = csv.writer(file, delimiter = ",")
    for movie_list in movie_lists:
        writer.writerow(movie_list) 

# Print a message to indicate that the operation is complete
print("Done!") 