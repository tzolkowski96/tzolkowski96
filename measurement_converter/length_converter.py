# Import the fuzzywuzzy package for fuzzy string matching
from fuzzywuzzy import process

# Define a class for converting lengths between different units
class LengthConverter:
    def __init__(self):
        # Initialize a dictionary to store conversion rates to meters for different units
        self.to_meters = {
            'inches': 0.0254,
            'feet': 0.3048,
            'yards': 0.9144,
            'meters': 1,
            'centimeters': 0.01,
            'millimeters': 0.001
        }
        # Initialize a cache to store results of fuzzy matching to improve performance
        self.unit_cache = {}

    # Method to perform fuzzy matching of unit names, using a cache to improve efficiency
    def fuzzy_match_unit(self, unit):
        # Check if the unit is already in the cache
        if unit in self.unit_cache:
            return self.unit_cache[unit]
        # Perform fuzzy matching and store the result in the cache
        matched_unit = process.extractOne(unit, self.to_meters.keys())[0]
        self.unit_cache[unit] = matched_unit
        return matched_unit

    # Method to convert a value from one unit to another
    def convert(self, value, from_unit, to_unit):
        # Fuzzy match the 'from' and 'to' units to handle typos or variations
        from_unit_matched = self.fuzzy_match_unit(from_unit)
        to_unit_matched = self.fuzzy_match_unit(to_unit)

        try:
            # Convert the value to meters using the 'from' unit, then to the target unit
            value_in_meters = value * self.to_meters[from_unit_matched]
            converted_value = value_in_meters / self.to_meters[to_unit_matched]
            return converted_value, from_unit_matched, to_unit_matched
        except KeyError:
            # Return None if there's an error in conversion (e.g., unit not found)
            return None, None, None

# Main function to interact with the user and perform conversions
def main():
    # Create an instance of the LengthConverter class
    converter = LengthConverter()
    # Prompt the user for the units to convert from and to, and the value to convert
    convert_from = input("Convert from (e.g., inches, feet, yards, meters, centimeters, millimeters): ").lower()
    convert_to = input("Convert to (e.g., inches, feet, yards, meters, centimeters, millimeters): ").lower()
    value_str = input(f"Enter number of {convert_from}: ")

    try:
        # Attempt to convert the input string to a float
        value = float(value_str)
        # Perform the conversion using the converter instance
        converted_value, from_unit_matched, to_unit_matched = converter.convert(value, convert_from, convert_to)
        if converted_value is not None:
            # If conversion is successful, print the result
            print(f"{value} {from_unit_matched} is {converted_value:.2f} {to_unit_matched}.")
        else:
            # If conversion fails, notify the user
            print("Conversion failed. Please check the units provided.")
    except ValueError:
        # Handle the case where the input value is not a valid number
        print("Please enter a valid number.")

if __name__ == '__main__':
    main()