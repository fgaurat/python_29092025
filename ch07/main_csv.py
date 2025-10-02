from pprint import pprint
import convert_dates
import json



def main():
    csv_file = "MOCK_DATA.csv"
    
    # f = open(csv_file,"a")
    with open(csv_file,"r") as f:
        # all = f.read() # read all file
        line_keys = f.readline().strip().split(',')     
        # list_lines = f.readlines()
        # line_keys = list_lines[0]
        # all_lines =  list_lines[1:]
        
        # print(list_lines)
        all_data = []
        for line in f:
            line = line.strip()
            row = line.split(',')
            # print(line_keys)
            # print(row)
            birth_date = row[-1]
            new_birth_date = convert_dates.convert_date_format(birth_date)
            # print(new_birth_date)
            # list_birth_date = birth_date.split('-')
            # new_birth_date = f"{list_birth_date[2]}/{list_birth_date[1]}/{list_birth_date[0]}"
            # print(new_birth_date)
            row[-1] = new_birth_date
            # ['id', 'first_name', 'last_name', 'email', 'gender', 'ip_address', 'birth_date']
            # ['995', 'Tabbatha', 'Mate', 'tmaterm@netscape.com', 'Female', '39.105.253.208', '1992-06-06']
            t = dict(zip(line_keys,row))
            all_data.append(t)
            # data_dict = {}
            # for i,k in enumerate(line_keys):
            #     data_dict[k] = row[i]
            # print(data_dict)

        
        pprint(all_data)
    # csv_file = "MOCK_DATA.csv"
    json_file_name = csv_file.replace(".csv",".json")
    
    with open(json_file_name,"w") as f:
        json.dump(all_data,f)

    

if __name__=='__main__':
    main()

