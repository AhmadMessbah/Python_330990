from flask import Flask, render_template, request, jsonify
from repository.database_maker import create_database
from controller.customer_controller import CustomerController
from controller.visit_controller import VisitController
from controller.timing_controller import TimingController


app = Flask(__name__)

# create_database()

@app.route('/')
def home():
    customer_controller = CustomerController()
    status, customer_list = customer_controller.find_all()
    return render_template("customer.html", customer_list=customer_list)

@app.route('/api/customers')
def customers():
    # API برای گرفتن لیست مشتریان
    return [{"id": 1, "first_name": "Ali", "family_name": "Ahmadi"},
            {"id": 2, "first_name": "Sara", "family_name": "Karimi"}]

@app.route('/customers', methods=['POST'])
def save_customer():
    first_name = request.form.get('first_name')
    family_name = request.form.get('family_name')
    gender = request.form.get('gender')
    phone = request.form.get('phone')
    birth_date = request.form.get('birth_date')
    medical_history = request.form.get('medical_history')
    customer_controller = CustomerController()
    status, message = customer_controller.save(
        first_name, family_name, gender, phone, birth_date, medical_history
    )
    status, customer_list = customer_controller.find_all()
    return render_template("customer.html", customer_list=customer_list, status=status, message=message)

@app.route('/visits')
def visits():
    visit_controller = VisitController()
    status, visit_list = visit_controller.find_all()
    return render_template("visit.html", visit_list=visit_list)

@app.route('/timings')
def timings():
    timing_controller = TimingController()
    status, timing_list = timing_controller.find_all()
    return render_template("timing.html", timing_list=timing_list)

if __name__ == "__main__":
    app.run(host="192.168.39.100", port=80, debug=True)
