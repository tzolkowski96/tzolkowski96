# Length Unit Converter

This is a length unit converter application built using Python and Shiny for Python. The application allows users to convert values between various length units such as inches, feet, yards, meters, centimeters, millimeters, kilometers, miles, and nautical miles.

## Features

- Converts lengths between different units.
- Ensures non-negative input values.
- Provides a user-friendly interface with dropdowns for unit selection and a numeric input for the value.
- Displays the conversion result in a text output.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/tzolkowski96/length-converter.git
    cd length-unit-converter
    ```

2. Create and activate a virtual environment (optional but recommended):
    ```bash
    python -m venv venv
    source venv/bin/activate   # On Windows, use `venv\Scripts\activate`
    ```

3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Run the application:
    ```bash
    python app.py
    ```

2. Open a web browser and navigate to the URL provided by Shiny (typically `http://127.0.0.1:8000`).

3. Use the dropdown menus to select the units to convert from and to, and enter the value to be converted. The result will be displayed below.

## Code Overview

- `app.py`: The main script containing the Shiny app and the `LengthConverter` class.

## License

This project is licensed under the MIT License.
