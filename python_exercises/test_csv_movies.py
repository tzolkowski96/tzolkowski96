import csv
import unittest
from csv_movies import write_movies_to_csv
import os

class TestCsvMovies(unittest.TestCase):

    def setUp(self):
        self.movie_lists = [
            ["Top Gun", "Risky Business", "Minority Report"],
            ["Titanic", "The Revenant", "Inception"],
            ["Training Day", "Man on Fire", "Flight"]
        ]
        self.file_name = "test_movies.csv"

    def tearDown(self):
        if os.path.exists(self.file_name):
            os.remove(self.file_name)

    def test_write_movies_to_csv(self):
        write_movies_to_csv(self.movie_lists, self.file_name)
        self.assertTrue(os.path.exists(self.file_name))

        with open(self.file_name, "r") as file:
            reader = csv.reader(file)
            rows = list(reader)
            self.assertEqual(len(rows), len(self.movie_lists))
            for i, row in enumerate(rows):
                self.assertEqual(row, self.movie_lists[i])

if __name__ == "__main__":
    unittest.main()
