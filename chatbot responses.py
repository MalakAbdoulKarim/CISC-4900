def get_response(user_input):
    user_input = user_input.lower()

    if "mfa" in user_input:
        return "To reset your MFA, visit https://cunyfirst.cuny.edu and click 'Forgot Password'. You’ll need your CUNY ID and access to your email."
    elif "cunyfirst" in user_input:
        return "If you can’t log into CUNYFirst, make sure you’re using your CUNY Login (firstname.lastname##@login.cuny.edu)."
    elif "forgot password" in user_input:
        return "You can reset your password through the CUNY Login page: https://home.cunyfirst.cuny.edu."
    elif "help" in user_input or "support" in user_input:
        return "I can help with MFA login, CUNYFirst, or password resets. What issue are you facing?"
    else:
        return "Sorry, I didn’t understand that. Try asking about MFA, CUNYFirst, or password reset."
