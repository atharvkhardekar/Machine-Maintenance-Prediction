import joblib
from flask import Flask, request, render_template

# Initialize Flask app
app = Flask(__name__)

# Load the Random Forest model
random_forest_model = joblib.load('random_forest_model.pkl')

@app.route('/info')
def info():
    return render_template('info.html')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get data from the form
        feature_1 = float(request.form['feature_1'])
        feature_2 = float(request.form['feature_2'])
        feature_3 = float(request.form['feature_3'])
        feature_4 = float(request.form['feature_4'])

        # Print the features for debugging
        print(f"Features: {feature_1}, {feature_2}, {feature_3}, {feature_4}")

        # Make prediction using the Random Forest model
        result = random_forest_model.predict([[feature_1, feature_2, feature_3, feature_4]])[0]
        
        # Print the result for debugging
        print(f"Prediction Result: {result}")

        # Convert the prediction result to a readable format
        prediction_text = "Maintenance Required" if result == 1 else "No Maintenance Required"

        # Render the result page with the prediction
        return render_template('result.html', prediction=prediction_text)

    except Exception as e:
        # If an error occurs, return the error message
        return str(e)

if __name__ == '__main__':
    app.run(debug=True)
