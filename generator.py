import random  
import string  

def generate_password(length):

    char_dump = string.ascii_letters + string.digits + string.punctuation
    
    password = ""

    for _ in range(length):
        password += random.choice(char_dump)
        
    return password

def main():
    print("=== Secure Password Generator ===")
    

    try:
        user_input = input("How many characters long should the password be? (e.g., 12): ")
        length = int(user_input)
        
        if length < 8:
            print("Warning: Passwords shorter than 8 characters are easy to guess!")
            
        secure_password = generate_password(length)
        print(f"\nYour secure password is: {secure_password}")
        
    except ValueError:
        print("Invalid input. Please type a whole number.")


if __name__ == "__main__":
    main()