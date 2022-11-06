import random
from faker import Faker
from models import Company, Contact
from  sqlalchemy.sql.expression import func, select, update
from sqlalchemy.orm import load_only
from settings import ENGINE


def get_randon_entry_id(session, model_name):
    return session.query(model_name).options(load_only('id')).offset(
        func.floor(
            func.random()*
            session.query(func.count(model_name.id))
        )
    ).limit(1).all()[0].id


def create_company(session):
    fake = Faker()
    
    company = Company(
        company_name=fake.company(),
        address=fake.address()
    )
    
    session.add(company)
    session.commit()
    
    return company


def update_company(session):
    fake = Faker()
    company_id = get_randon_entry_id(session, Company)
    
    session.execute(
        update(Company)
        .where(Company.id == company_id)
        .values(company_name=fake.company())
    )
    
    session.commit()


def create_contact(session):
    fake = Faker()
    
    company_id = get_randon_entry_id(session, Company)
    
    contact = Contact(
        company_id = company_id,
        first_name = fake.first_name(),
        last_name = fake.last_name(),
        phone_number = fake.phone_number(),
        active = random.choices([True, False], weights=[0.8, 0.2])[0],
        address = fake.address(),
    )
    
    session.add(contact)
    session.commit()
    
    return contact


def update_contact(session):
    fake = Faker()
    contact_id = get_randon_entry_id(session, Contact)
    
    session.execute(
        update(Contact)
        .where(Contact.id == contact_id)
        .values(first_name=fake.first_name())
    )
    
    session.commit()
    

def populate_one_entry(session):
    
    if random.choice([True, False]):
        if random.choices([True, False], weights=[0.3, 0.7])[0]:
            update_company(session)
        else:
            create_company(session)

    if random.choices([True, False], weights=[0.3, 0.7])[0]:
        update_contact(session)
    else:
        create_contact(session)
