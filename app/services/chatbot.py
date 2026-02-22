def chatbot_response(msg):
    msg = msg.lower()

    if "invest" in msg:
        return "Diversify between equity and debt funds."
    elif "retirement" in msg:
        return "Start early to benefit from compounding."
    else:
        return "Ask about investing, saving or retirement."
