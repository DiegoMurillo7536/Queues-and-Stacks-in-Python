import utils
import random
class Stack:
    def __init__(self) -> None:
        self.data_list : list = []
    
    def insert_random_data_into_list(self,quantity : int):
        count = 0
        while count < quantity:
            value = random.randint(1,quantity)
            self.data_list.append(value)
            count += 1
    
    def empty(self) -> bool:
        if self.data_list is None:
            print(f"The list is empty")
            return True
        
    def size(self) -> int:
        if self.empty(self.data_list):
            return len(self.data_list)
    
    def top(self) -> int :
        return self.data_list[-1]
    
    def pop(self):
        return self.data_list.pop()

    def get_stack_exercises(self):
        print("==== Start stack exercises ====")
        util = utils
        random_quantity = int(input("Insert the random quantity numbers that you want "))
        self.insert_random_data_into_list(random_quantity)
        print(f" The random numbers into list is: {self.data_list}")
        util.search_even_numbers_into_list(self.data_list)
        util.average_data_list_without_functions(self.data_list)
        util.average_data_list_with_functions(self.data_list)
        print(f"The last item in the  stack is: {self.top()}")
        print("==== End stack exercises =====")

