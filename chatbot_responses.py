def get_response(user_input):
    user_input = user_input.lower().strip()

    # -----------------------
    # NUMBER MENU SELECTIONS
    # -----------------------

    if user_input == "1":
        return (
            "Troubleshooting Login:\n"
            "- Check if CAPS LOCK is on\n"
            "- Use the correct login format (firstname.lastname##@login.cuny.edu)\n"
            "- Try resetting your CUNY Login password\n"
            "- Ensure you are connected to the campus network"
        )

    elif user_input == "2":
        user_input = "mfa"  # Route to MFA section below

    elif user_input == "3":
        user_input = "email"  # Route to email section

    elif user_input == "4":
        user_input = "wifi student"  # Route to student wifi

    elif user_input == "5":
        user_input = "wifi faculty"  # Route to faculty wifi


    # -----------------------
    # NATURAL LANGUAGE INPUT
    # -----------------------

    if "mfa" in user_input:
        return (
            "Troubleshooting MFA:\n"
            "- Ensure your primary CUNY Login credentials are correct\n"
            "- Check if your registered device or authenticator app is accessible\n"
            "- Make sure the MFA code has not expired\n"
            "- If issues continue, reset your MFA or contact IT Support"
        )

    elif "cunyfirst" in user_input or "login" in user_input:
        return (
            "Troubleshooting CUNYFirst Login:\n"
            "- Use the correct login format: firstname.lastname##@login.cuny.edu\n"
            "- Make sure CAPS LOCK is not on\n"
            "- Try resetting your CUNY Login password\n"
            "- If the account is locked, wait 30 minutes or visit IT Support"
        )

    elif "forgot password" in user_input or "reset password" in user_input:
        return (
            "Password Reset Instructions:\n"
            "- Go to the CUNY Login page\n"
            "- Click 'Forgot Password'\n"
            "- Enter your CUNYfirst EMPLID or CUNY Login\n"
            "- Check your Outlook email for the verification code"
        )

    elif "email" in user_input or "outlook" in user_input:
        return (
            "Troubleshooting Email (BC Email / Outlook):\n"
            "- Use your @login.cuny.edu account for CUNY systems\n"
            "- Use @brooklyn.cuny.edu only for Outlook\n"
            "- Reset password through the CUNY Login page\n"
            "- Wait 30 minutes OR contact IT if your account is locked"
        )

    elif "wifi" in user_input:
        if "student" in user_input or "eduroam" in user_input:
            return (
                "Troubleshooting Student Wi-Fi (eduroam):\n"
                "- Students: Use firstname.lastname##@login.cuny.edu\n"
                "- Forget and re-add the network\n"
                "- Restart your device\n"
                "- If still not working, wait 30 minutes or visit IT"
            )

        elif "faculty" in user_input or "staff" in user_input:
            return (
                "Troubleshooting Faculty Wi-Fi:\n"
                "- Faculty/Staff: Use Firstname.Lastname@brooklyn.cuny.edu\n"
                "- Use your Outlook password\n"
                "- Forget and re-add the network\n"
                "- Restart your device\n"
                "- Contact IT if the issue persists"
            )

        else:
            return (
            "Sorry, I didn’t understand that.\n"
            "Try typing:\n"
            "1. Login Issue\n"
            "2. MFA\n"
            "3. Email / Outlook\n"
            "4. Student Wi-Fi\n"
            "5. Faculty Wi-Fi"
        )
