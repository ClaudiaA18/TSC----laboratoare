#TODO Creati o baza de date fake ce contine minim 500 de intrari. 
# O intrare este reprezentata de o instanta a clasei Person (pe care trebuie sa o creati) 
# care are minim 3 atribute (nume, varsta, email). Cheia unica este representata de adresa de mail. 


from faker import Faker
import random

class Person:
    def __init__(self, name, age, email):
        self.name = name
        self.age = age
        self.email = email

    def __repr__(self):
        return f"Person(Name: {self.name}, Age: {self.age}, Email: {self.email})"

# Genereaza date false
def generate_fake_data(num_entries=500):
    fake = Faker()
    people_db = {}
    while len(people_db) < num_entries:
        name = fake.name()
        age = random.randint(18, 99)  # Varsta între 18 și 99 ani
        email = fake.email()
        # Asigura ca fiecare email este unic in baza de date
        if email not in people_db:
            people_db[email] = Person(name, age, email)
    return people_db

# Creaza baza de date fake
fake_people_db = generate_fake_data()

# Afiseaza primele 10 persoane pentru verificare
for email, person in list(fake_people_db.items())[:10]:
    print(person)
