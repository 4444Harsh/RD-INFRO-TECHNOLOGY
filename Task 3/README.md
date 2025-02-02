# Bank Customer Churn Prediction

This project aims to predict customer churn using machine learning techniques. The dataset contains various customer details, including demographics and financial information.

## Dataset
- **Source:** [Kaggle - Bank Customer Churn Prediction](https://www.kaggle.com/datasets/shantanudhakadd/bank-customer-churn-prediction)
- **Description:** The dataset consists of customer details such as credit card usage, balance, estimated salary, and more.

## Repository
- **GitHub:** [RD-INFRO-TECHNOLOGY](https://github.com/4444Harsh/RD-INFRO-TECHNOLOGY.git)

## Project Workflow
1. **Data Preprocessing**
   - Load and clean the dataset
   - Handle missing values and outliers
   - Convert categorical variables using one-hot encoding
2. **Exploratory Data Analysis**
   - Visualize data distribution
   - Identify key features affecting churn
3. **Feature Engineering**
   - Normalize numerical features
   - Select relevant features for the model
4. **Model Training**
   - Train a machine learning model (Random Forest Classifier)
   - Evaluate model performance using accuracy and classification reports
5. **Prediction and Analysis**
   - Make predictions on test data
   - Analyze model results

## Requirements
- Python 3.x
- Pandas, NumPy
- Scikit-learn
- Seaborn, Matplotlib

## Installation
Clone the repository and install dependencies:
```sh
$ git clone https://github.com/4444Harsh/RD-INFRO-TECHNOLOGY.git
$ cd RD-INFRO-TECHNOLOGY
$ pip install -r requirements.txt
```

## Usage
Run the script to train and evaluate the model:
```sh
$ python Churn_model.py
```

## Results
- Accuracy and classification report will be printed in the terminal.
- Feature importance can be analyzed for better insights.

## Contribution
Feel free to contribute by submitting pull requests or reporting issues!

## License
This project is open-source and available under the MIT License.
