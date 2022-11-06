from models import Contact, Company
from utils import populate_one_entry
from settings import ENGINE, SESSION
import random
import time


session = SESSION()

while True:
    
    populate_one_entry(session)
    time.sleep(2)
    
session.close()
