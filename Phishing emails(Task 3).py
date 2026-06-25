# ==========================================
# Project Title: Phishing Email Detector
# Features:
# 1. Detect suspicious keywords
# 2. Detect suspicious links
# 3. Detect suspicious attachments
# 4. Detect urgent language
# 5. Generate risk level
# 6. Generate phishing analysis report
#==========================================

import re
def phishing_analysis(message):

    # Common phishing keywords and phrases
    suspicious_keywords = [
        "urgent",
        "verify",
        "verification",
        "password",
        "otp",
        "account",
        "account holder",
        "bank",
        "login",
        "log in",
        "sign in",
        "sign-in",
        "click here",
        "immediately",
        "suspended",
        "locked",
        "lock your account",
        "confirm",
        "update",
        "security alert",
        "security",
        "unusual login",
        "unrecognized device",
        "unauthorized",
        "unauthorized access",
        "verify your identity",
        "secure my account",
        "reset password",
        "payment",
        "invoice",
        "refund",
        "winner",
        "prize"
    ]

    # Suspicious attachment types
    suspicious_attachments = [
        ".exe",
        ".zip",
        ".rar",
        ".bat",
        ".scr",
        ".js",
        ".doc",
        ".xlsm"
    ]

    found_keywords = []
    found_attachments = []
    red_flags = []

    # Check suspicious keywords
    for word in suspicious_keywords:
        if word.lower() in message.lower():
            found_keywords.append(word)

    # Find URLs
    links = re.findall(r'https?://\S+', message)

    # Check suspicious attachments
    for attachment in suspicious_attachments:
        if attachment.lower() in message.lower():
            found_attachments.append(attachment)

    # Red flags
    if found_keywords:
        red_flags.append("Suspicious keywords found")

    if links:
        red_flags.append("Suspicious links found")

    if found_attachments:
        red_flags.append("Suspicious attachment detected")

    urgent_words = [
        "urgent",
        "immediately",
        "act now",
        "limited time",
        "respond now"
    ]

    if any(word in message.lower() for word in urgent_words):
        red_flags.append("Urgent language detected")

    # Generate Report
    print("\n========== PHISHING ANALYSIS REPORT ==========")

    print("\nMessage:")
    print(message)

    print("\nSuspicious Keywords Found:")
    if found_keywords:
        for keyword in found_keywords:
            print("-", keyword)
    else:
        print("Suspicious keywords are not found.")

    print("\nLinks Found:")
    if links:
        for link in links:
            print("-", link)
    else:
        print("No links found")

    print("\nSuspicious Attachments Found:")
    if found_attachments:
        for attachment in found_attachments:
            print("-", attachment)
    else:
        print("No suspicious attachments found")

    print("\nRed Flags:")
    if red_flags:
        for flag in red_flags:
            print("-", flag)
    else:
        print("No red flags found")

    # Final Result
    if len(red_flags)>=3:
        print("\nRisk Level: HIGH")
        print("Assessment: Potential phishing email.")
    elif len(red_flags)>=1:
        print("\nRisk Level: MEDIUM")
        print("Assessment:Suspicious content detected. Manual review "
              "recommended.")
    else:
        print("\nRisk Level: LOW")
        print("Assessment:No obvious phishing indicators detected. ")


# Take multi-line input
print("Enter email/message (Type END on a new line to finish):")

lines = []

while True:
    line = input()

    if line.upper() == "END":
        break

    lines.append(line)

message = "\n".join(lines)

# Analyze the message/calling the function
phishing_analysis(message)