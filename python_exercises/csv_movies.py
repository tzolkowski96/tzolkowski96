import csv
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def write_movies_to_csv(movie_lists, file_name):
    """
    Writes a list of movie lists to a CSV file.

    Parameters:
    movie_lists (list of list of str): A list containing lists of movie titles.
    file_name (str): The name of the output CSV file.

    Returns:
    None
    """
    try:
        with open(file_name, "w", newline='') as file:
            writer = csv.writer(file, delimiter=",")
            for movie_list in movie_lists:
                writer.writerow(movie_list)
        logging.info(f"Movies successfully written to {file_name}")
    except IOError as e:
        logging.error(f"An error occurred while writing to the file: {e}")

def main():
    """
    Main function to execute the script.
    
    Returns:
    None
    """
    # Define a list of movie lists
    movie_lists = [
        ["Top Gun", "Risky Business", "Minority Report"],
        ["Titanic", "The Revenant", "Inception"],
        ["Training Day", "Man on Fire", "Flight"]
    ]

    # Define the name of the output file
    file_name = "movies.csv"

    # Write the movie lists to the CSV file
    write_movies_to_csv(movie_lists, file_name)

if __name__ == "__main__":
    main()
