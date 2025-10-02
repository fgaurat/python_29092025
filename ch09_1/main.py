import json
from Customer import Customer
def main():
    json_file_name = "MOCK_DATA.json"
    with open(json_file_name) as f:
        all_customers = json.load(f)
        
        # c = all_customers[0]
        for c in all_customers:
            print(50*'-')
            customer = Customer(*c.values())
            # print(customer)
            print(customer.first_name)
            print(customer.age)
            print(customer.birth_date)

if __name__=='__main__':
    main()
