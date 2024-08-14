import random
from faker import Faker

class Queue:
    def __init__(self) -> None:
        self.person_data = []
        self.fake = Faker()

    def enqueue(self,quantity:int):
        count = 0
        while count < quantity:
            data = [
                self.fake.unique.random_int(min=1,max=quantity), # code 
                self.fake.name(), # name
                self.fake.phone_number(), # phone number
                random.randint(0,100) # age
                ]
            self.person_data.append(data)
            count += 1

    def dequeue(self):
        if len(self.person_data) > 0: 
            self.person_data.pop(0)

    def front(self):
        if len(self.person_data) > 0:
            print(f" The first element in the queue is:{self.person_data[0]}")

    def rear(self):
            if len(self.person_data) > 0:
                print(f" The last element in the queue is:{self.person_data[-1]}")

    def get_queues_exercises(self):
        print("==== Start queue exercises ====")
        random_quantity = int(input("¿How many random persons do you want to insert? "))
        self.enqueue(random_quantity)
        print(f"Full queue: {self.person_data}")
        self.dequeue()
        print(f" Queue without first element: {self.person_data}")
        print(len(self.person_data))
        print("==== End queue exercises ====")
