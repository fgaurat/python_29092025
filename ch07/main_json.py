import json

def main():
    json_file_name = "MOCK_DATA.json"
    with open(json_file_name) as f:
        all_data = json.load(f)

    print(all_data[3])
    d = all_data[3] 
    #     {
    #     "id": "4",
    #     "first_name": "Levin",
    #     "last_name": "Martel",
    #     "email": "lmartel3@artisteer.com",
    #     "gender": "Male",
    #     "ip_address": "160.95.124.234",
    #     "birth_date": "19/04/1998"
    # },
    print(d['email'])





if __name__=='__main__':
    main()
