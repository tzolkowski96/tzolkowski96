import streamlit as st

def introduction():
    """Display an introduction message with instructions."""
    st.title("Welcome to the Calculator")
    st.write("This calculator can add, subtract, multiply, divide numbers, and perform other advanced operations.")
    st.write("Select your operation from the dropdown menu.")

def get_number(prompt):
    """Get a number from the user."""
    number = st.number_input(prompt)
    return number

def get_operation_choice():
    """Get and validate the user's choice of operation."""
    choice = st.selectbox("Choose operation", ['Addition', 'Subtraction', 'Multiplication', 'Division', 'Exponentiation', 'Square Root'], index=0)
    return choice

def perform_calculation(choice, num1, num2=None):
    """Perform the calculation based on the user's choice and handle division by zero."""
    if choice == 'Addition':
        result = num1 + num2
    elif choice == 'Subtraction':
        result = num1 - num2
    elif choice == 'Multiplication':
        result = num1 * num2
    elif choice == 'Division':
        if num2 == 0:
            st.error("Error: Division by zero is not allowed.")
            return None
        result = num1 / num2
    elif choice == 'Exponentiation':
        result = num1 ** num2
    elif choice == 'Square Root':
        if num1 < 0:
            st.error("Error: Square root of negative number is not allowed.")
            return None
        result = num1 ** 0.5
    return result

def main():
    """Main function to run the calculator program."""
    introduction()
    choice = get_operation_choice()
    
    if choice == 'Square Root':
        num1 = get_number("Enter the number: ")
        num2 = None
    else:
        num1 = get_number("Enter first number: ")
        num2 = get_number("Enter second number: ")
    
    if 'history' not in st.session_state:
        st.session_state.history = []

    if st.button("Calculate"):
        result = perform_calculation(choice, num1, num2)
        if result is not None:
            st.success(f"Result: {result}")
            st.session_state.history.append(f"{choice} of {num1} and {num2} = {result}")

    if st.button("Reset"):
        st.session_state.history = []
        st.experimental_rerun()
    
    if st.session_state.history:
        st.write("Calculation History:")
        for record in st.session_state.history:
            st.write(record)

if __name__ == '__main__':
    main()
