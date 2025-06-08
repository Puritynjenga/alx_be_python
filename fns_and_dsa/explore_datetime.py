
'''1. datetime.datetime: Combines date and time information.
   2.datetime.date: Represents a date (year, month, day).
   3.datetime.time: Represents a time (hour, minute, second, microsecond).
   4.datetime.timedelta: Represents the difference between two dates or times.
   5.strftime(): Formats a datetime object into a string based on a specified format code.'''


import datetime
from datetime import timedelta

def display_current_datetime():
    """
    Part 1: Displays the current date and time in a specified format.
    Also encapsulates the future date calculation as an inner function.
    """
    # Obtain the current date and time
    current_date = datetime.datetime.now()

    # Format and print the current date and time
    # Format: "YYYY-MM-DD HH:MM:SS"
    formatted_current_datetime = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {formatted_current_datetime}")

    # --- Inner function: calculate_future_date ---
    def calculate_future_date():
        """
        Part 2: Prompts the user for a number of days, calculates a future date,
        and prints it in "YYYY-MM-DD" format.
        This is an inner function, scoped within display_current_datetime.
        """

        # Prompt the user to enter a number of days
        while True:
            try:
                number_of_days = int(input("Enter the number of days to add to the current date: "))

                if number_of_days < 0:
                    print("Please enter a posive number of days.")
                else:
                    break # Valid input, exit the loop
            except ValueError:
                print("Invalid input. Please enter an integer.")

        # The 'current_date' from the outer function's scope is accessible here
        # No need to call datetime.datetime.now() again
        time_delta = datetime.timedelta(days=number_of_days)

        # Calculate the future date
        future_date = current_date + time_delta # Using current_date from outer scope

        # Print the future date in "YYYY-MM-DD" format
        formatted_future_date = future_date.strftime("%Y-%m-%d")
        print(f"Future date: {formatted_future_date}")

    # Call the inner function
    calculate_future_date()

# Main execution block
if __name__ == "__main__":
    display_current_datetime() # Calling the outer function will now also execute the inner function