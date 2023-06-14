def calculate_age():
    try:
        n = input("Enter your name: ")
        yob = int(input("Enter your year of birth: "))
        cy = 2023 
        age = cy - yob
        print(f"{n}, your age is {age}.")
    except TypeError:
        print("Please enter an integer ")

calculate_age()