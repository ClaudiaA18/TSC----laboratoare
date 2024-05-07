# TODO Creati un stub si o functie fake care sa simuleze 
# functionalitatea metodei get(cheie_unica) pe o baza de date. 
# Puteti sa folositi baza de date creata anterior. 

from faker import Faker
import random

class Person:
    def __init__(self, name, age, email):
        self.name = name
        self.age = age
        self.email = email

def generate_fake_data(num_entries):
    fake = Faker()
    return {fake.email(): Person(fake.name(), random.randint(18, 80), fake.email()) for _ in range(num_entries)}

def get_youngest_person(db):
    return min(db.values(), key=lambda person: person.age, default=None)
