def search_even_numbers_into_list(data_list):
    count = 0
    even_numbers = 0
    
    while count < len(data_list):
        if  data_list[count] % 2 == 0:
            print(f"{data_list[count]} is even")
            even_numbers += 1
        count += 1
    print(f"The even numbers quantity is {even_numbers}")

def average_data_list_without_functions(data_list):
    count = 0
    addition = 0
    data_quantity = len(data_list)
    while count < data_quantity:
        addition += data_list[count]
        count += 1
    average_data = addition / data_quantity
    print(f"The average data is {average_data}")

def average_data_list_with_functions(data_list):
    print(f"The average data is {sum(data_list)/len(data_list)} ")






