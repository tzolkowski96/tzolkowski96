# Length Converter

The Length Converter is a Python-based utility designed to facilitate the conversion of lengths between various units. It leverages fuzzy matching to accommodate minor typos or variations in unit names, enhancing user experience by providing flexibility in input. This document outlines the features, installation guide, usage instructions, and how to contribute to the project.

## Features

- **Support for Multiple Units:** Converts between inches, feet, yards, meters, centimeters, and millimeters.
- **Fuzzy Matching:** Utilizes fuzzy matching to identify and correct minor typos in unit names, reducing input errors.
- **Caching Mechanism:** Improves performance by caching the results of fuzzy matching, minimizing redundant computations.
- **User-friendly Interface:** Provides a simple command-line interface for easy interaction.

## Installation

To use the Length Converter, ensure you have Python 3.x installed on your system. Follow these steps:

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/tzolkowski96/length-converter.git
   ```
2. **Navigate to the Project Directory:**
   ```bash
   cd length-converter
   ```
3. **Install Dependencies:**
   The project requires the `fuzzywuzzy` package. Install it using pip:
   ```bash
   pip install fuzzywuzzy
   ```

## Usage

To start the Length Converter, run the following command in the terminal:

```bash
python length_converter.py
```

Follow the on-screen prompts to input the unit you are converting from, the unit you wish to convert to, and the value to be converted.

### Example

```plaintext
Convert from (e.g., inches, feet, yards, meters, centimeters, millimeters): inches
Convert to (e.g., inches, feet, yards, meters, centimeters, millimeters): meters
Enter number of inches: 12
12 inches is 0.30 meters.
```

## Contributing

Contributions to the Length Converter are welcome! Here's how you can contribute:

- **Report Bugs:** Use the Issues section to report any bugs found.
- **Suggest Enhancements:** Have ideas on how to make the Length Converter better? Share them in the Issues section.
- **Submit Pull Requests:** Feel free to fork the repository and submit pull requests with bug fixes or feature additions.

Before contributing, please read through the project's contribution guidelines (if available).

## Acknowledgments

- Thanks to the `fuzzywuzzy` library for providing the fuzzy matching functionality.