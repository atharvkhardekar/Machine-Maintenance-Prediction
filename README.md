# Machine Maintenance Prediction

This project uses machine learning models combined with the Crayfish Optimization Algorithm to predict maintenance needs for industrial machinery. By analyzing sensor data, it helps minimize downtime and optimize maintenance strategies.

## Features
- **Machine Learning Models**: Implemented various models and selected the best performing Random Forest model optimized using the Crayfish algorithm.
- **Predictive Maintenance**: Real-time analysis of sensor data to predict machine failures.

## Setup and Installation

### Setting Up the Model
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/atharvkhardekar/Machine-Maintenance-Prediction.git
   cd Machine-Maintenance-Prediction

2. **Dataset**
- The dataset **machine_failure.csv** contains 14 columns and 10,000 data points.

3. **Run Jupyter Notebook**:
- Open **Machine_Maintenance_Prediction_optimizer.ipynb** in Jupyter Notebook.
- Download the dataset **machine_failure.csv**.
- Train and optimize models using provided scripts to generate your **.pkl** files.
- You can also make changes in the model to achieve different accuracies and your own **.pkl** files.
- **Note**: .pkl files for two models are also provided for convenience you can directly use that.

## Deploying the Flask Application
## Setup Environment:
- Make sure you have Python installed.

1. **Install dependencies**:
   ```bash
   pip install -r requirements.txt

2. **Run Flask Application**:
   ```bash
   python app.py
   
3. **Access the Web App**:
- Visit http://localhost:5000 to use the prediction tool.

## Usage
- Load Sensor Data: Upload CSV data for analysis or upload your real-time data.
- Predict Failures: View model predictions for maintenance needs.

## Technologies Used
- Machine Learning: Scikit-learn, Pandas, Machine Learning algorithms, Crayfish Optimization Algorithm.
- Frontend: Flask Templates (HTML/CSS)
- Deployment: Flask Web Framework

## License
This project is licensed under the MIT License. See the **LICENSE** file for details.

## For More Details of The Project
- A research paper "**Optimized Manufacturing and Construction Site Machines Maintenance Prediction using Machine Learning and Crayfish Algorithm**" also published based on this project in "**International Journal For Multidisciplinary Research**" you can also refer that.   
- Paper Id : 28248

## Contact
- For any questions or support, reach out:

- Email: **khardekaratharv@gmail.com**
- GitHub: **atharvkhardekar**

