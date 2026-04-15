# Keep this outside the function so the chatbot remembers the user's progress
session = {
    "issue": None,
    "step": 0
}

def get_response(user_input):
    user_input = user_input.lower().strip()

    yes_answers = ["yes", "worked", "it worked", "fixed", "okay", "ok"]
    no_answers = ["no", "not working", "still not working", "didn't work", "didnt work", "doesnt work"]

    mfa_steps = [
        "Ensure your primary CUNY Login credentials are correct.",
        "Check if your registered device or authenticator app is accessible.",
        "Make sure the MFA code has not expired.",
        "If it still does not work, reset your MFA or contact IT Support."
    ]

    login_steps = [
        "Use the correct login format: firstname.lastname##@login.cuny.edu.",
        "Make sure CAPS LOCK is not on.",
        "Try resetting your CUNY Login password.",
        "If the account is locked, wait 30 minutes or visit IT Support."
    ]

    password_steps = [
        "Go to the CUNY Login page.",
        "Click 'Forgot Password'.",
        "Enter your CUNYfirst EMPLID or CUNY Login.",
        "Check your Outlook email for the verification code."
    ]

    email_steps = [
        "Use your @login.cuny.edu account for CUNY systems.",
        "Use @brooklyn.cuny.edu only for Outlook.",
        "Reset your password through the CUNY Login page.",
        "Wait 30 minutes or contact IT if your account is locked."
    ]

    student_wifi_steps = [
        "Use firstname.lastname##@login.cuny.edu for eduroam.",
        "Forget and re-add the network.",
        "Restart your device.",
        "If it still does not work, wait 30 minutes or visit IT."
    ]

    faculty_wifi_steps = [
        "Use Firstname.Lastname@brooklyn.cuny.edu.",
        "Use your Outlook password.",
        "Forget and re-add the network.",
        "Restart your device.",
        "Contact IT if the issue persists."
    ]

    # -----------------------
    # CONTINUE CURRENT ISSUE
    # -----------------------
    if session["issue"] is not None:
        if session["issue"] == "mfa":
            steps = mfa_steps
        elif session["issue"] == "login":
            steps = login_steps
        elif session["issue"] == "password":
            steps = password_steps
        elif session["issue"] == "email":
            steps = email_steps
        elif session["issue"] == "student_wifi":
            steps = student_wifi_steps
        elif session["issue"] == "faculty_wifi":
            steps = faculty_wifi_steps
        else:
            steps = []

        if user_input in yes_answers:
            session["issue"] = None
            session["step"] = 0
            return "Great, your issue is fixed!"

        elif user_input in no_answers:
            session["step"] += 1

            if session["step"] < len(steps):
                return steps[session["step"]] + "\nDid this work?"
            else:
                session["issue"] = None
                session["step"] = 0
                return "Please contact IT Support for further help."

        else:
            return "Please reply with yes or no."

    # -----------------------
    # START NEW ISSUE
    # -----------------------
    if "mfa" in user_input:
        session["issue"] = "mfa"
        session["step"] = 0
        return mfa_steps[0] + "\nDid this work?"

    elif "cunyfirst" in user_input or "login" in user_input:
        session["issue"] = "login"
        session["step"] = 0
        return login_steps[0] + "\nDid this work?"

    elif "forgot password" in user_input or "reset password" in user_input:
        session["issue"] = "password"
        session["step"] = 0
        return password_steps[0] + "\nDid this work?"

    elif "email" in user_input or "outlook" in user_input:
        session["issue"] = "email"
        session["step"] = 0
        return email_steps[0] + "\nDid this work?"

    elif "wifi" in user_input:
        if "student" in user_input or "eduroam" in user_input:
            session["issue"] = "student_wifi"
            session["step"] = 0
            return student_wifi_steps[0] + "\nDid this work?"

        elif "faculty" in user_input or "staff" in user_input:
            session["issue"] = "faculty_wifi"
            session["step"] = 0
            return faculty_wifi_steps[0] + "\nDid this work?"

    # -----------------------
    # FALLBACK
    # -----------------------
    return (
        "What issue are you having?\n"
        "You can type: MFA, login, reset password, email, student wifi, or faculty wifi."
    )
