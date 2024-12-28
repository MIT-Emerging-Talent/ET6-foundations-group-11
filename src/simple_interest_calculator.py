def calculate_simple_interest(principal, rate, time):
    """
    Calculate the simple interest.

    :param principal: The principal amount (float).
    :param rate: The annual interest rate (as a percentage, float).
    :param time: The time the money is invested or borrowed for (in years, float).
    :return: The calculated simple interest (float).
    """
    interest = (principal * rate * time) / 100
    return interest


def main():
    print("Welcome to the Simple Interest Calculator!")

    # Input the principal, rate, and time
    try:
        principal = float(input("Enter the principal amount: "))
        rate = float(input("Enter the annual interest rate (in %): "))
        time = float(input("Enter the time (in years): "))

        # Validate input to ensure positive values
        if principal <= 0 or rate <= 0 or time <= 0:
            print("All values must be positive. Please try again.")
            return

        # Calculate simple interest
        interest = calculate_simple_interest(principal, rate, time)

        # Display the result (formatted to 2 decimal places)
        print(
            f"The simple interest for a principal of {principal} at a rate of {rate}% for {time} years is: {interest:.2f}"
        )
    except ValueError:
        print(
            "Invalid input. Please enter numeric values for principal, rate, and time."
        )


if __name__ == "__main__":
    main()
