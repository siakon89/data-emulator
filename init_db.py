from models import Base
from settings import ENGINE, SESSION
from utils import populate_one_entry

Base.metadata.create_all(ENGINE)

session = SESSION()

create_company(session)
create_contact(session)

for _ in range(1000):
    
    populate_one_entry(session)
    
session.close()
