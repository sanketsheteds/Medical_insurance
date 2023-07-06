from flask import Flask, request, jsonify, render_template
from utils import MedicalInsurance
import config

app = Flask(__name__)

@app.route('/medical_insurance')
def home():
    return render_template('medical_insurance.html')

@app.route('/predict_charges', methods=['GET', 'POST'])
def predict_charges():
    if request.method == 'GET':
        data = request.args
    elif request.method == 'POST':
        data = request.form
    else:
        return jsonify({"message": "Unsuccessful"})

    age = int(data.get('age'))
    gender = data.get('gender')
    bmi = int(data.get('bmi'))
    children = int(data.get('children'))
    smoker = data.get('smoker')
    region = data.get('region')

    insurance_obj = MedicalInsurance(age, gender, bmi, children, smoker, region)
    pred_price = insurance_obj.get_predicted_price()

    return render_template('medical_insurance.html', prediction=pred_price)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port='8080')
