def get_response(user_input):
    user_input = user_input.lower().strip()

    login_steps = [
        "Check if CAPS LOCK is on.",
        "Use the correct login format: firstname.lastname##@login.cuny.edu",
        "Try resetting your CUNY Login password.",
        "Make sure you are connected to the campus network."
    ]

    mfa_steps = [
        "Make sure your CUNY Login username and password are correct.",
        "Approve the Duo push notification on your phone.",
        "If you got a new phone, reactivate MFA through the CUNY portal.",
        "If MFA still fails, contact the IT Help Desk."
    ]

    email_steps = [
        "Use your full Brooklyn College email address.",
        "Make sure you are using your Outlook password.",
        "Try logging in through Outlook on the web.",
        "If needed, reset your password and try again."
    ]

    student_wifi_steps = [
        "Use firstname.lastname##@login.cuny.edu for eduroam login.",
        "Enter your CUNY Login password.",
        "Forget the network and reconnect to 'eduroam'.",
        "Restart your device if needed.",
        "If it still does not work, wait 30 minutes or visit the IT Help Desk.",
        "Connection instructions depending on your device:",
        "- iPhone/iPad: Go to Settings > Wi-Fi > Select 'eduroam' > Enter credentials.",
        "- Android: Select 'eduroam' > EAP Method: PEAP > Phase 2: MSCHAPV2 > Enter login info.",
        "- Mac: System Settings > Wi-Fi > Select 'eduroam' > Enter credentials.",
        "- Windows: Connect to 'eduroam' > Enter login when prompted."
    ]

    faculty_wifi_steps = [
        "Use Firstname.Lastname@brooklyn.cuny.edu for eduroam login.",
        "Use your Outlook (Brooklyn College email) password.",
        "Forget the network and reconnect to 'eduroam'.",
        "Restart your device if needed.",
        "Contact IT if the issue persists.",
        "Connection instructions depending on your device:",
        "- iPhone/iPad: Go to Settings > Wi-Fi > Select 'eduroam' > Enter credentials.",
        "- Android: Select 'eduroam' > EAP Method: PEAP > Phase 2: MSCHAPV2 > Enter BC email login.",
        "- Mac: System Settings > Wi-Fi > Select 'eduroam' > Enter credentials.",
        "- Windows: Connect to 'eduroam' > Enter BC email and password."
    ]

    # -----------------------
    # NUMBER MENU SELECTIONS
    # -----------------------
    if user_input == "1":
        return "Troubleshooting Login:\n- " + "\n- ".join(login_steps)

    elif user_input == "2":
        return "Troubleshooting MFA:\n- " + "\n- ".join(mfa_steps)

    elif user_input == "3":
        return "Troubleshooting Email:\n- " + "\n- ".join(email_steps)

    elif user_input == "4":
        return "Troubleshooting Student Wi-Fi:\n- " + "\n- ".join(student_wifi_steps)

    elif user_input == "5":
        return "Troubleshooting Faculty Wi-Fi:\n- " + "\n- ".join(faculty_wifi_steps)

    # -----------------------
    
    # -----------------------
    if "login" in user_input or "cuny login" in user_input:
        return "Troubleshooting Login:\n- " + "\n- ".join(login_steps)

    elif "mfa" in user_input or "duo" in user_input:
        return "Troubleshooting MFA:\n- " + "\n- ".join(mfa_steps)

    elif "email" in user_input or "outlook" in user_input or "bc email" in user_input:
        return "Troubleshooting Email:\n- " + "\n- ".join(email_steps)

    elif "wifi student" in user_input or ("wifi" in user_input and "student" in user_input):
        return "Troubleshooting Student Wi-Fi:\n- " + "\n- ".join(student_wifi_steps)

    elif "wifi faculty" in user_input or ("wifi" in user_input and "faculty" in user_input):
        return "Troubleshooting Faculty Wi-Fi:\n- " + "\n- ".join(faculty_wifi_steps)

    elif "wifi" in user_input or "eduroam" in user_input:
        return (
            "Are you connecting as a student or faculty member?\n"
            "Type:\n"
            "4 for Student Wi-Fi\n"
            "5 for Faculty Wi-Fi"
        )

    else:
        return (
            "Sorry, I did not understand that.\n"
            "Please choose one of these options:\n"
            "1. Login Issue\n"
            "2. MFA Questions\n"
            "3. Email Issue\n"
            "4. Student Wi-Fi\n"
            "5. Faculty Wi-Fi"
        )


# -----------------------
# MAIN CHATBOT LOOP
# -----------------------
print("Welcome to Smart Lab Assistant")
print("How can I help you today?")
print("1. Login Issue")
print("2. MFA Questions")
print("3. Email Issue")
print("4. Student Wi-Fi")
print("5. Faculty Wi-Fi")
print("Type 'quit' to exit.\n")

while True:
    user_input = input("You: ")

    if user_input.lower().strip() == "quit":
        print("Smart Lab Assistant: Goodbye!")
        break

    response = get_response(user_input)
    print("\nSmart Lab Assistant:")
    print(response)
    print()
