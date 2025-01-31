## Credit Card Fraud Detection

### Project Overview
This project aims to detect fraudulent credit card transactions using machine learning models. The dataset used includes transactional details, user demographics, and fraud labels.

### Dataset
- `fraudTrain.csv`: Training dataset.
- `fraudTest.csv`: Testing dataset.
- Dataset Link: [Kaggle Fraud Detection Dataset](https://www.kaggle.com/datasets/kartik2112/fraud-detection)

### Features Used
- **Date-based Features**: Year, month, day, hour, minute.
- **Categorical Encoding**: Label encoding for categorical variables.
- **Feature Selection**: Dropped highly correlated columns.

### Models Used
- Logistic Regression
- Decision Tree Classifier
- Random Forest Classifier

### Installation
1. Clone the repository:
   ```sh
   git clone https://github.com/4444Harsh/RD-INFRO-TECHNOLOGY
   cd RD-INFRO-TECHNOLOGY
   ```
2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
3. Run the Jupyter Notebook or Python script.

### Usage
- Run the notebook to preprocess data, train models, and evaluate results.
- The trained Random Forest model is saved as `model.pkl`.

### Dependencies
See `requirements.txt` for the necessary Python packages.
