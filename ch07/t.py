line_keys = ['id', 'first_name', 'last_name', 'email', 'gender', 'ip_address', 'birth_date']

row = ['995', 'Tabbatha', 'Mate', 'tmaterm@netscape.com', 'Female', '39.105.253.208', '1992-06-06']

d={}
for pos,k in enumerate(line_keys):
    d[k] = row[pos]
    print(d)

