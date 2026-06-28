# Caesar Cipher Encryption and Decryption

## Description
A Python program that implements the Caesar Cipher technique to encrypt and decrypt text messages using a shift key.

## Features
- Encrypts text messages
- Decrypts encrypted messages
- Supports uppercase and lowercase letters
- Preserves spaces and special characters
- User-defined shift key

## Technologies Used
- Python 3.X      

## How to Run

1. Open the project folder.
2. Run the Python file:

```bash
python "basic encryption and decryption technique(Task2).py"
```

3. Enter the text and shift key when prompted.

## Example

```text
Enter text: Hello
Enter shift key: 3

Encrypted Text: Khoor
Decrypted Text: Hello
```





# Password Strength Checker

## Description
A Python program that checks the strength of a password based on length, uppercase letters, lowercase letters, digits, and special characters.

## Features
- Minimum 8 characters
- Checks uppercase letters
- Checks lowercase letters
- Checks digits
- Checks special characters
- Classifies passwords as Weak, Medium, or Strong

## Technologies Used
- Python 3

## How to Run

1. Download or clone the repository.
2. Open the project folder.
3. Run the program:

```bash
python "password strength checker(Task 1).py"
```

4. Enter a password when prompted.

## Example

### Input
```text
Please enter your password: Pass@123
```

### Output
```text
Strong Password
```

### Input
```text
Please enter your password: password
```

### Output
```text
Weak Password
```

### Input
```text
Please enter your password: Password123
```

### Output
```text
Medium Password
```

## Password Rules

- At least 8 characters long
- Contains at least one uppercase letter
- Contains at least one lowercase letter
- Contains at least one digit
- Contains at least one special character




# Phishing Email Detector

## Overview

The Phishing Email Detector is a Python-based cybersecurity project that analyzes emails and messages for common phishing indicators. The program scans the content for suspicious keywords, malicious links, dangerous attachments, and urgency-based language often used by attackers.

Based on the analysis, the tool generates a detailed phishing report and assigns a risk level to help users identify potentially fraudulent emails.

---

## Features

### Suspicious Keyword Detection

Detects common phishing-related keywords and phrases such as:

* Urgent
* Verify
* Password
* OTP
* Account Holder
* Bank
* Login
* Security Alert
* Invoice
* Refund
* Prize

### URL Detection

Identifies links present in the message using Regular Expressions (Regex).

### Suspicious Attachment Detection

Detects potentially dangerous attachment types including:

* .exe
* .zip
* .rar
* .bat
* .scr
* .js
* .doc
* .xlsm

### Urgent Language Detection

Detects urgency-based phrases commonly used in phishing attacks.

### Risk Assessment

Classifies messages into:

* Low Risk
* Medium Risk
* High Risk

### Detailed Analysis Report

Generates a report containing:

* Suspicious keywords found
* Links detected
* Attachments detected
* Red flags identified
* Risk level assessment

---

## Technologies Used

* Python 3
* Regular Expressions (re Module)

---

## How to Run

1. Download or clone the repository.
2. Open the project folder.
3. Run the program:

```bash
python "Phishing emails(Task 3).py"
```

4. Enter the email/message content when prompted.
5. Type `END` on a new line to finish the input.
6. The program will analyze the message and display a phishing analysis report.

---

## Example Input

```text
Subject: Security Alert

Dear Account Holder,

We detected an unusual login attempt from an unrecognized device.

Click here:
https://fake-bank.com

Download Invoice.zip

Act immediately to secure your account.

END
```

---

## Example Output

```text
========== PHISHING ANALYSIS REPORT ==========

Suspicious Keywords Found:
- security alert
- account holder
- login
- click here

Links Found:
- https://fake-bank.com

Suspicious Attachments Found:
- .zip

Red Flags:
- Suspicious keywords found
- Suspicious links found
- Suspicious attachment detected
- Urgent language detected

Risk Level: HIGH
Assessment: Potential phishing email.
```

---

## Skills Demonstrated

* Python Programming
* String Processing
* Pattern Matching using Regex
* Cybersecurity Fundamentals
* Risk Assessment
* Threat Detection Concepts

---

## Limitations

* Rule-based detection only.
* Does not verify whether a URL is genuinely malicious.
* Does not analyze email headers.
* May generate false positives or false negatives.
* Does not use Machine Learning techniques.

---

## Future Enhancements

* Machine Learning-based phishing detection
* Email header analysis
* Domain reputation checking
* GUI development using Tkinter
* Real-time email scanning
* PDF report generation

---





# System Vulnerability Checklist

## Overview

The System Vulnerability Checklist is a Python-based cybersecurity project that identifies common security vulnerabilities in a computer system through a simple questionnaire. The program evaluates password strength, software update status, and user security practices to calculate a risk score and provide detailed security recommendations.

Based on the analysis, the tool generates a security report and classifies the system's overall security risk as Low, Medium, or High.

---

## Features

### Password Strength Check

Checks whether the password:

* Contains at least 8 characters
* Includes uppercase letters
* Includes lowercase letters
* Includes numbers
* Includes special characters

### Software Update Check

Verifies whether the operating system is updated with the latest security patches.

### User Security Practices Check

Evaluates common unsafe security practices such as:

* Reusing passwords
* Clicking unknown email links
* Using public Wi-Fi without a VPN

### Risk Assessment

Calculates a risk score based on detected vulnerabilities.

Classifies the system into:

* Low Risk
* Medium Risk
* High Risk

### Detailed Security Report

Generates a report containing:

* Password strength status
* Software update status
* Unsafe user practices detected
* Total risk score
* Overall security level
* Detailed security recommendations

---

## Technologies Used

* Python 3
* Standard Python Libraries

---

## How to Run

1. Download or clone the repository.
2. Open the project folder.
3. Run the program:

```bash
python "System Vulnerability Checklist(Task 4).py"
```

4. Answer the security-related questions displayed on the screen.
5. The program will analyze the responses and generate a security assessment report.

---

## Example Input

```text
Enter your password: Hello123

Is your operating system updated? (yes/no): no

Do you reuse passwords? (yes/no): yes

Do you click unknown email links? (yes/no): no

Do you use public Wi-Fi without VPN? (yes/no): yes
```

---

## Example Output

```text
==================== SECURITY REPORT ====================

Password Status : WEAK

Software Status : Not Updated

Total Risk Score : 4

Overall Security Level : HIGH RISK

Security Recommendations:

- Use a stronger password.
- Install the latest operating system updates.
- Avoid reusing passwords.
- Use a VPN while connected to public Wi-Fi.
- Enable Multi-Factor Authentication (MFA).
- Install trusted antivirus software.
- Back up important files regularly.
```

---

## Skills Demonstrated

* Python Programming
* Conditional Statements
* Loops
* String Processing
* Input Validation
* Cybersecurity Fundamentals
* Risk Assessment
* Basic System Security Analysis

---

## Limitations

* User-input based assessment only.
* Does not automatically scan the operating system.
* Does not verify installed software versions.
* Does not check firewall or antivirus status.
* Does not perform real-time vulnerability scanning.

---

## Future Enhancements

* Automatic system vulnerability scanning
* Firewall status detection
* Antivirus detection
* Password breach checking
* Report generation in PDF format
* Graphical User Interface (GUI) using Tkinter
* Automatic operating system update detection

---

## Author
Kotagiri Mansi


