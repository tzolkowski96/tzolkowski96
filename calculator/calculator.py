import streamlit as st

def introduction():
    """Display an introduction message with instructions."""
    st.title("Welcome to the Enhanced Calculator")
    st.write("This calculator can add, subtract, multiply, and divide numbers.")
    st.write("Select your operation from the dropdown menu.")

def get_number(prompt, key):
    """Safely get a number from the user."""
    number = st.text_input(prompt, key=key)
    return number

def get_operation_choice():
    """Get and validate the user's choice of operation."""
    choice = st.selectbox("Choose operation", ['Addition', 'Subtraction', 'Multiplication', 'Division'], index=0)
    return choice[0].upper()

def perform_calculation(choice, num1, num2):
    """Perform the calculation based on the user's choice and handle division by zero."""
    if choice == 'A':
        result = num1 + num2
    elif choice == 'S':
        result = num1 - num2
    elif choice == 'M':
        result = num1 * num2
    elif choice == 'D':
        if num2 == 0:
            st.error("Error: Division by zero is not allowed.")
            return None
        result = num1 / num2
    return result

def main():
    """Main function to run the calculator program."""
    introduction()
    choice = get_operation_choice()
    
    num1_key = 'num1'
    num2_key = 'num2'
    
    # Initialize session state variables if not already done
    if num1_key not in st.session_state:
        st.session_state[num1_key] = ""
    if num2_key not in st.session_state:
        st.session_state[num2_key] = ""
    
    num1_str = get_number("Enter first number: ", num1_key)
    num2_str = get_number("Enter second number: ", num2_key)
    
    if st.button("Calculate"):
        try:
            num1 = float(st.session_state[num1_key])
        except ValueError:
            st.error("Invalid input for the first number. Please enter a numeric value.")
            return
        
        try:
            num2 = float(st.session_state[num2_key])
        except ValueError:
            st.error("Invalid input for the second number. Please enter a numeric value.")
            return
        
        result = perform_calculation(choice, num1, num2)
        if result is not None:
            st.success(f"Result: {result}")

if __name__ == '__main__':
    main()
