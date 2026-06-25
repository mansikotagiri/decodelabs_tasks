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

## Author
Kotagiri Mansi

