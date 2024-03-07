from flask import Flask, request, render_template
import pickle

app = Flask(__name__)

# Load the trained model
with open('/workspaces/judy-deployment/model/linear_regression_model.pkl', 'rb') as f:
    model = pickle.load(f)

# Define a route to handle the prediction request
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Extract data from the request
    product = request.form['product']
    branch = request.form['branch']
    city = request.form['city']
    payment = request.form['payment']
    customerType = request.form['customerType']

    # Perform prediction using the loaded model
    # Dummy logic is used here, replace it with your actual prediction logic
    prediction_result = predict_gender_preference(product, branch, city, payment, customerType)

    return render_template('result.html', prediction_result=prediction_result)

# Dummy prediction function, replace with actual prediction logic
def predict_gender_preference(product, branch, city, payment, customerType):
    # Dummy logic based on product line, city, and customer type
    if product == 'Electronic Accessories' and city == 'Yangon' and customerType == 'Member':
        return 'Male preferences predicted.'
    elif product == 'Fashion Accessories' and city == 'Naypyitaw' and customerType == 'Normal':
        return 'Female preferences predicted.'
    else:
        # Default prediction
        return 'Female preferences predicted.'

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8090, debug=True)
