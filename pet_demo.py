import time
from pet import Pet


def main():
    print("=" * 50)
    print(" 🐾 WELCOME TO THE PET REGISTRATION PORTAL 🐾 ")
    print("=" * 50)

    my_pet = Pet()

    print("\nPlease enter your pet's details below:\n")

    name_input = input("Enter pet's name: ").strip()
    my_pet.set_name(name_input)

    type_input = input("Enter pet's animal type (e.g., Dog, Cat, Bird): ").strip()
    my_pet.set_animal_type(type_input.capitalize())

    while True:
        try:
            age_input = int(input("Enter pet's age (in years): "))
            if age_input < 0:
                print("Age cannot be negative. Try again.")
                continue
            my_pet.set_age(age_input)
            break
        except ValueError:
            print("⚠️ Invalid input! Please enter a whole number for the age.")

    print("\nProcessing registration data...")
    time.sleep(1.5)
    print("\n" + "=" * 50)
    print("PET REGISTRATION SUCCESSFUL")
    print("=" * 50)
    print(f"Name: {my_pet.get_name()}")
    print(f"Type: {my_pet.get_animal_type()}")
    age_suffix = "year old" if my_pet.get_age() == 1 else "years old"
    print(f"Age:  {my_pet.get_age()} {age_suffix}")
    print("=" * 50)

if __name__ == "__main__":
    main()