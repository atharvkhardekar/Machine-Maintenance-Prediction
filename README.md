# Machine Maintenance Prediction

This project uses machine learning models combined with the Crayfish Optimization Algorithm to predict maintenance needs for industrial machinery. By analyzing sensor data, it helps minimize downtime and optimize maintenance strategies.

## Features
- **Machine Learning Models**: Various models implemented; the best performing is a Random Forest model optimized using the Crayfish algorithm.
- **Predictive Maintenance**: Real-time analysis of sensor data to foresee machine failures.

## Setup and Installation

### Setting Up the Model
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/atharvkhardekar/Machine-Maintenance-Prediction.git
   cd Machine-Maintenance-Prediction

Dataset

The dataset machine_failure.csv contains 14 columns and 10,000 data points.
Run Jupyter Notebook:

Open Machine_Maintenance_Prediction_optimizer.ipynb in Jupyter Notebook.
Download the dataset machine_failure.csv.
Train and optimize models using provided scripts to generate your .pkl files.
You can also make changes in the model to achieve different accuracies.
Note: Pre-trained .pkl files for two models are also provided for convenience.
Deploying the Flask Application
Setup Environment:

Make sure you have Python installed.
Install dependencies:
bash
Copy code
pip install -r requirements.txt
Run Flask Application:

bash
Copy code
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

