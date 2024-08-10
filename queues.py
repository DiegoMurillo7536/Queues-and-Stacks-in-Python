import random
from faker import Faker

person_data = []
fake = Faker()

def insert_random_data_into_list(quantity:int):
    count = 0
    while count < quantity:
        data = [
            fake.unique.random_int(min=1,max=quantity), # code 
            fake.name(), # name
            fake.phone_number(), # phone number
            random.randint(0,100) # age
            ]
        person_data.append(data)
        count += 1
def remove_first_item_in_list(data_list:list):
    data_list.pop(0)


insert_random_data_into_list(5)
print(f"Full queue: {person_data}")
remove_first_item_in_list(person_data)
print(f" Queue without first element: {person_data}")
print(len(person_data))