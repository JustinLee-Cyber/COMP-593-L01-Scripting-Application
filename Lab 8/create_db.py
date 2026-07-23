"""
Name: Justin Lee

Description:
 Creates the people table in the Social Network database
 and populates it with 200 fake people.

Usage:
 python create_db.py
"""
import os
import sqlite3
from datetime import datetime
from faker import Faker


# Determine the path of the database
script_dir = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(script_dir, 'social_network.db')

def main():
    create_people_table()
    populate_people_table()

def create_people_table():
    """Creates the people table in the database"""

    con = sqlite3.connect(db_path)
    cur = con.cursor()

    # TODO: Create function body
    # Hint: See example code in lab instructions entitled "Creating a Table"

    
    ppl_table_query = """
        CREATE TABLE IF NOT EXISTS people
        (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            email TEXT NOT NULL,
            address TEXT NOT NULL,
            city TEXT NOT NULL,
            province TEXT NOT NULL,
            bio TEXT,
            age INTEGER,
            created_at DATETIME NOT NULL,
            updated_at DATETIME NOT NULL 
        );
"""
    #Execute the SQL query to create the 'people' table
    cur.execute(ppl_table_query)

    con.commit()
    con.close()

    return

def populate_people_table():
    """Populates the people table with 200 fake people"""

    con = sqlite3.connect(db_path)
    cur = con.cursor()

    # TODO: Create function body
    # Hint: See example code in lab instructions entitled "Inserting Data into a Table"
    # Hint: See example code in lab instructions entitled "Working with Faker"

    add_person_query = """
    INSERT INTO people
    (
        name,
        email,
        address,
        city,
        province,
        bio,
        age,
        created_at,
        updated_at 
    )
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?);
"""
    fake = Faker("en_CA")
    #define and create the tuple of data for the new person to be insert into the people table
    for _ in range(200):
        #tuble of data that will be insert - fake person
        new_person = (fake.name(),
                      fake.ascii_email(),
                      fake.street_address(),
                      fake.city(),
                      fake.administrative_unit(),
                      fake.sentence(nb_words=5),
                      fake.random_int(min=1, max=100),
                      datetime.now(),
                      datetime.now())
        #Add the fake person to the data base
        cur.execute(add_person_query,new_person)

    con.commit()
    con.close()

    return

if __name__ == '__main__':
   main()