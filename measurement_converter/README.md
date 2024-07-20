# Length Unit Converter

This is a length unit converter application built using Python and Shiny for Python. The application allows users to convert values between various length units such as inches, feet, yards, meters, centimeters, millimeters, kilometers, miles, and nautical miles.

## Features

- **Unit Conversion**: Converts lengths between different units.
- **Validation**: Ensures non-negative input values.
- **User-Friendly Interface**: Provides dropdowns for unit selection and a numeric input for the value.
- **Real-Time Results**: Displays the conversion result instantly.

## Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/tzolkowski96/length-converter.git
    cd length-converter
    ```

2. **Create and activate a virtual environment** (optional but recommended):
    ```bash
    python -m venv venv
    source venv/bin/activate   # On Windows, use `venv\Scripts\activate`
    ```

3. **Install the required dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. **Run the application**:
    ```bash
    python app.py
    ```

2. **Open a web browser** and navigate to the URL provided by Shiny (typically `http://127.0.0.1:8000`).

3. **Interact with the application**:
    - Use the dropdown menus to select the units to convert from and to.
    - Enter the value to be converted.
    - The result will be displayed below.

## Code Overview

- **`app.py`**: The main script containing the Shiny app and the `LengthConverter` class.
- **`length_converter.py`**: Contains the `LengthConverter` class which handles the conversion logic.

## License

This project is licensed under the MIT License.
