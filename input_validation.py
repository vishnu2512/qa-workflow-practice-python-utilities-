def get_valid_age():
    while True:
        try:
            age = int(input("Enter age: "))
            if age <= 0:
                print("Age must be a positive number.")
            else:
                return age
        except ValueError:
            print("Please enter a valid integer.")

if __name__ == "__main__":
    age = get_valid_age()
    print(f"Validated age: {age}")
