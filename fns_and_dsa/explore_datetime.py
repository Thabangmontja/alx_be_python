from datetime import datetime, timedelta

def display_current_datetime():
    """Display the current date and time in 'YYYY-MM-DD HH:MM:SS' format."""
    # Get the current date and time
    current_date = datetime.now()
    # Format the date and time
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {formatted_date}")

def calculate_future_date():
    """Calculate and display a future date based on user input."""
    # Prompt the user for the number of days
    days_to_add = int(input("Enter the number of days to add to the current date: "))
    # Calculate the future date
    future_date = datetime.now() + timedelta(days=days_to_add)
    # Format the future date
    formatted_future_date = future_date.strftime("%Y-%m-%d")
    print(f"Future date: {formatted_future_date}")

if __name__ == "__main__":
    display_current_datetime()  # Display the current date and time
    calculate_future_date()      # Calculate and display the future date
