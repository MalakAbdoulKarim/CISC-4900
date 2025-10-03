# smart_lab_assistant_prototype.py
print("Welcome to Smart Lab Assistant")
print("What issue are you facing?")
print("1. Login Issue")
print("2. Printer Problem")
print("3. Software Crash")
choice = input("Enter number: ")

if choice == "1":
    print("Troubleshooting Login:")
    print("- Check if CAPS LOCK is on")
    print("- Try resetting your CUNY password")
    print("- Ensure you are connected to the campus network")

elif choice == "2":
    print("Troubleshooting Printer:")
    print("- Check if the printer is online")
    print("- Clear the print queue")
    print("- Try a different lab printer")

elif choice == "3":
    print("Troubleshooting Software:")
    print("- Restart the program")
    print("- Check if your file format is supported")
    print("- Update to the latest version")

else:
    print("Sorry, I don’t recognize that option yet.")
