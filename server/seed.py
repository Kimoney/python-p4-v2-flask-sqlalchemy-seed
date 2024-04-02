#!/usr/bin/env python3
#server/seed.py
from random import choice as rc
from faker import Faker

from app import app
from models import db, Pet

with app.app_context():

    # Create and initialize a faker generator
    fake = Faker()

    #Delete All Rows In pets table before seeding the data
    Pet.query.delete()

    # Create an empty list
    pets = []

    species = ["Dog", "Cat", "Chicken", "Hamster", "Turtle"]

    # Create some Pet instances to the pets list
    for n in range(20):
        pet = Pet(name=fake.first_name(), species=rc(species))
        pets.append(pet)
# Manually Input Data Commented Out
    # # Add some Pet instances to the list
    # pets.append(Pet(name = "Fido", species = "Dog"))
    # pets.append(Pet(name = "Whiskers", species = "Cat"))
    # pets.append(Pet(name = "Hermie", species = "Hamster"))
    # pets.append(Pet(name="Snek", species="Snake"))

    # Insert each Pet in the list into the database table
    db.session.add_all(pets)

    # Commit the transaction
    db.session.commit()