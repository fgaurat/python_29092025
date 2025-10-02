import streamlit as st
import json
from Customer import Customer

def main():
    st.set_page_config(layout="wide",page_title="Hoooooo !",)


    json_file_name = "MOCK_DATA.json"
    list_customers=[]
    with open(json_file_name) as f:
        all_customers = json.load(f)
        for c in all_customers:
            customer = Customer(*c.values())
            list_customers.append(customer)



    st.markdown("# Formation Python c'est bien")
    st.markdown("## Le titre 2")

    name = st.text_input("Name", "")
    if st.button('le button'):
        st.markdown(f"bonjour {name}")
    
    st.table(list_customers)

if __name__=='__main__':
    main()
