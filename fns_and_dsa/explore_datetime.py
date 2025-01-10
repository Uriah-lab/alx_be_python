from datetime import datetime, timedelta

def display_current_datetime():
    """
    Display the current date and time in a readable format.
    """
    current_date = datetime.now()
    print("Current date and time:", current_date.strftime("%Y-%m-%d %H:%M:%S"))

def calculate_future_date():
    """
    Prompt the user to enter a number of days and calculate the future date.
    """
    try:
        number_of_days = int(input("Enter the number of days to add to the current date: "))
        current_date = datetime.now()
        future_date = current_date + timedelta(days=number_of_days)
        print("Future date:", future_date.strftime("%Y-%m-%d"))
    except ValueError:
        print("Please enter a valid integer for the number of days.")

def main():
    display_current_datetime()
    calculate_future_date()

if __name__ == "__main__":
    main()
