from flask import Flask, render_template
import json
from Customer import Customer

app = Flask(__name__)

# flask run
@app.route("/hello")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/customers_json")
def customers_json():
    json_file_name = "MOCK_DATA.json"
    list_customers=[]
    with open(json_file_name) as f:
        all_customers = json.load(f)
        for c in all_customers:
            customer = Customer(*c.values())
            list_customers.append(customer)
    
    return list_customers

@app.route("/customers_html")
def customers_html():
    json_file_name = "MOCK_DATA.json"
    html=""
    with open(json_file_name) as f:
        all_customers = json.load(f)
        for c in all_customers:
            customer = Customer(*c.values())
            html+=f"<li>{customer.first_name} {customer.email}</li>"
    
    return f"<ul>{html}</ul>"

@app.route("/customers_jinja")
def customers_jinja():
    json_file_name = "MOCK_DATA.json"
    list_customers=[]
    with open(json_file_name) as f:
        all_customers = json.load(f)
        for c in all_customers:
            customer = Customer(*c.values())
            list_customers.append(customer)
    
    return render_template("customers.html",customers = list_customers)