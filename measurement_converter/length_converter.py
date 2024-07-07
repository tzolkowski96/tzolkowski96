from fuzzywuzzy import process

def convert_length(value, from_unit, to_unit):
    """
    Converts a length from one unit to another, now including metric units and handling typos in unit names.

    Parameters:
    value (float): The length value to be converted.
    from_unit (str): The unit of the input value.
    to_unit (str): The unit of the converted value.

    Returns:
    float: The converted value, or None if conversion is not possible.
    """
    # Conversion factors to meters from other units
    to_meters = {
        'inches': 0.0254,
        'feet': 0.3048,
        'yards': 0.9144,
        'meters': 1,
        'centimeters': 0.01,
        'millimeters': 0.001
    }

    # Fuzzy match the units to handle typos and abbreviations
    from_unit_matched = process.extractOne(from_unit, to_meters.keys())[0]
    to_unit_matched = process.extractOne(to_unit, to_meters.keys())[0]

    try:
        # Convert from the initial unit to meters
        value_in_meters = value * to_meters[from_unit_matched]
        # Convert from meters to the target unit
        converted_value = value_in_meters / to_meters[to_unit_matched]
        return converted_value, from_unit_matched, to_unit_matched
    except KeyError:
        # Return None if either unit is invalid
        return None, None, None

def main():
    # User input for conversion parameters
    convert_from = input("Convert from (e.g., inches, feet, yards, meters, centimeters, millimeters): ").lower()
    convert_to = input("Convert to (e.g., inches, feet, yards, meters, centimeters, millimeters): ").lower()
    try:
        value_str = input(f"Enter number of {convert_from}: ")
        # Attempt to convert the input string to float
        try:
            value = float(value_str)
        except ValueError:
            print("Please enter a valid number.")
            return

        # Perform conversion
        converted_value, from_unit_matched, to_unit_matched = convert_length(value, convert_from, convert_to)
        # Output result or error message
        if converted_value is not None:
            print(f"{value} {from_unit_matched} is {converted_value:.2f} {to_unit_matched}.")
        else:
            print("Invalid unit.")
    except ValueError:
        print("Please enter a valid number.")

if __name__ == '__main__':
    main()