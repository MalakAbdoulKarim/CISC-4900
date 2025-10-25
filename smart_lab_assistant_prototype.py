# smart_lab_assistant_prototype.py

# This block prints a welcome message and presents the user with a main menu 
# of available troubleshooting categories.
print("Welcome to Smart Lab Assistant")
print("What issue are you facing?")
print("1. Login Issue")
print("2. MFA questions")
print("3. Software Crash")

# This block captures the user's choice from the menu.
# Input: A string representing a menu number (e.g., "1", "2", or "3").
# Output: The stored choice for use in the conditional logic below.
choice = input("Enter number: ")

# This is the main control flow block (if/elif/else).
# It directs the program to the appropriate troubleshooting guide based on the user's 'choice'.

# Conditional block for "1. Login Issue".
# Executes if the input 'choice' is exactly "1".
# Output: Prints three specific troubleshooting steps for login problems.
if choice == "1":
    print("Troubleshooting Login:")
    print("- Check if CAPS LOCK is on")
    print("- Try resetting your CUNY password")
    print("- Ensure you are connected to the campus network")

# Conditional block for "2. Printer Problem".
# Executes if the input 'choice' is exactly "2".
# Output: Prints three specific troubleshooting steps for printer issues.
elif choice == "2":
    print("Troubleshooting MFA:")
    print("- Ensure your primary login credentials are correct")
    print("- Check if your registered device or authenticator app is accessible")
    print("- Verify that the MFA code has not expired")
    print("- If issues persist, reset your MFA or contact IT support")


# Conditional block for "3. Software Crash".
# Executes if the input 'choice' is exactly "3".
# Output: Prints three specific troubleshooting steps for software crashes.
elif choice == "3":
    print("Troubleshooting Software:")
    print("- Restart the program")
    print("- Check if your file format is supported")
    print("- Update to the latest version")

# Fallback block.
# Executes if the input 'choice' does not match any of the defined options ("1", "2", or "3").
# Output: Prints a generic message indicating the option is not recognized.
else:
    print("Sorry, I don’t recognize that option yet.")
