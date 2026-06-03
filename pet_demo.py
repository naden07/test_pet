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

