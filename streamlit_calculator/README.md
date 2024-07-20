# Streamlit Calculator

## Overview

The Streamlit Calculator is a user-friendly, web-based application designed to perform basic arithmetic operations. Built using Streamlit, this calculator supports addition, subtraction, multiplication, division, exponentiation, and square root calculations. It also features a history of calculations performed during the current session and a reset functionality to clear the history.

## Features

- **Addition**: Adds two numbers.
- **Subtraction**: Subtracts the second number from the first number.
- **Multiplication**: Multiplies two numbers.
- **Division**: Divides the first number by the second number, with error handling for division by zero.
- **Exponentiation**: Raises the first number to the power of the second number.
- **Square Root**: Calculates the square root of a number, with error handling for negative numbers.
- **Calculation History**: Displays a history of all calculations performed in the current session.
- **Reset Functionality**: Clears the calculation history and resets the session.

## Installation

To run this calculator locally, you need to have Python and Streamlit installed. Follow the steps below to get started:

1. **Clone the repository:**
    ```bash
    git clone https://github.com/your-repo/streamlit-calculator.git
    cd streamlit-calculator
    ```

2. **Create and activate a virtual environment** (optional but recommended):
    ```bash
    python -m venv venv
    source venv/bin/activate   # On Windows, use `venv\Scripts\activate`
    ```

3. **Install the required packages:**
    ```bash
    pip install streamlit
    ```

## Usage

1. **Run the Streamlit application:**
    ```bash
    streamlit run calculator_app.py
    ```

2. **Open your web browser** and navigate to the local URL provided by Streamlit (usually `http://localhost:8501`).

3. **Interact with the application**:
    - Select an operation from the dropdown menu.
    - Input the numbers.
    - Click the "Calculate" button to see the result.
    - Use the "Reset" button to clear the history and start a new session.

## Script Explanation

The calculator script is organized into several functions:

- **`introduction()`**: Displays the introduction message and instructions.
- **`get_number(prompt)`**: Prompts the user to input a number.
- **`get_operation_choice()`**: Provides a dropdown menu for selecting the desired operation.
- **`perform_calculation(choice, num1, num2=None)`**: Performs the calculation based on the user's choice and handles any errors (e.g., division by zero, square root of a negative number).
- **`main()`**: The main function that ties all the components together, manages session state, and handles user interactions.

## Example

Here is a brief example of how the application might be used:

1. Open the calculator in your browser.
2. Choose "Addition" from the dropdown menu.
3. Enter `5` as the first number.
4. Enter `3` as the second number.
5. Click "Calculate" to see the result (`8`).
6. The calculation history will display "Addition of 5 and 3 = 8".
7. Click "Reset" to clear the history and start a new session.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Contact

For any questions or suggestions, please open an issue or contact the repository owner.

