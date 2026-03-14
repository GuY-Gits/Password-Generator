# Secure Password Generator

A lightweight utility script built in Python that leverages randomized algorithms to generate highly secure, customizable passwords based on user-defined constraints.

## Features
* **Custom Length:** Users can specify the exact number of characters for their password.
* **High Entropy:** Utilizes a complete pool of lowercase letters, uppercase letters, digits, and special punctuation to ensure maximum security.
* **Input Validation:** Safely handles incorrect user inputs (like typing letters instead of numbers) without crashing.
* **Security Warnings:** Alerts the user if they request a password that is considered too short to be secure.

## Technologies Used
* Python 3
* Built-in Modules: `random`, `string`

## How to Run
1. Ensure you have Python installed on your system.
2. Clone this repository to your local machine.
3. Open your terminal and navigate to the project folder.
4. Run the script by typing:
   `python generator.py` *(or `python3 generator.py` depending on your setup)*

---
*This project was built while learning the basics of Python.*