Machine Maintenance Prediction 
This project uses machine learning models combined with the Crayfish Optimization Algorithm to predict maintenance needs for industrial machinery. By analyzing sensor data, it helps minimize downtime and optimize maintenance strategies.

Features
Machine Learning Models: Implemented various machine learning models and selected the best accuracy Random Forest model with Crayfish optimizer.
Predictive Maintenance: Real-time sensor data analysis to predict potential machine failures.

Setup and Installation
Setting Up the Model
Clone the Repository:
Copy code
git clone https://github.com/atharvkhardekar/Machine-Maintenance-Prediction.git
cd Machine-Maintenance-Prediction

Dataset
machine_failure.csv 
contains 14 cloumns and 10000 data points.

Run Jupyter Notebook:
Open Machine_Maintenance_Prediction_optimizer.ipynb in Jupyter Notebook.
Download the dataset machine_failure.csv
Train and optimize models using provided scripts to generate your .pkl files.
You can also do your own changes in model to get different accuracies for your model.
OR I have also uploaded two differnt pkl files of two models you can also use that.

Deploying the Flask Application
Setup Environment:
Make sure you have Python installed.
Install dependencies:
pip install -r requirements.txt

Run Flask Application:
python app.py

Access the Web App:
Visit http://localhost:5000 to use the prediction tool.

Usage
Load Sensor Data: Upload CSV data for analysis.
Predict Failures: View model predictions for maintenance needs.

Technologies Used
Machine Learning: Scikit-learn, Pandas, Crayfish Optimization Algorithm
Frontend: Flask Templates (HTML/CSS)
Deployment: Flask Web Framework

License
This project is licensed under the MIT License. See the LICENSE file for details.

Contact
For any questions or support, reach out:

Email: khardekaratharv@gmail.com
GitHub: atharvkhardekar
