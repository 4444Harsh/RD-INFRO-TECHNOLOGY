# Movie Genre Classification

## Overview
This project aims to classify movie genres using machine learning techniques. The goal is to create a model that can predict the genre of a movie based on its plot summary or other textual information. Techniques like TF-IDF or word embeddings are used along with classifiers such as Naive Bayes, Logistic Regression, or Support Vector Machines.

## Dataset
The dataset used in this project is available at:
- [Kaggle: Genre Classification Dataset (IMDB)](https://www.kaggle.com/datasets/hijest/genre-classification-dataset-imdb)

The dataset contains the following key features:
- **Title**: The name of the movie.
- **Description**: A brief summary of the movie.
- **Other metadata**: Includes attributes such as director, actors, release year, etc.
- **Genres**: The target variable indicating the genre(s) of the movie.

## Technologies Used
- Python
- Jupyter Notebook
- Pandas
- NumPy
- Scikit-learn
- Natural Language Processing (NLP) techniques
- Machine Learning algorithms

## Installation
To run this project locally, follow these steps:

1. Clone the repository:
   ```sh
   git clone https://github.com/4444Harsh/RD-INFRO-TECHNOLOGY.git
   ```
2. Navigate to the project directory:
   ```sh
   cd movie-genre-classification
   ```
3. Install the required dependencies:
   ```sh
   pip install -r requirements.txt
   ```
4. Run the Jupyter Notebook:
   ```sh
   jupyter notebook MOVIE_GENRE_CLASSIFICATION.ipynb
   ```

## Approach
1. **Data Preprocessing**: Cleaning and preparing the dataset, handling missing values, and tokenizing text features.
2. **Feature Engineering**: Extracting relevant features from textual and numerical data.
3. **Model Training**: Implementing various machine learning models such as:
   - Naive Bayes
   - Logistic Regression
   - Support Vector Machine (SVM)
4. **Evaluation**: Measuring model performance using accuracy, precision, recall, and F1-score.

## Results
The performance of the models is evaluated, and the best-performing model is selected based on validation metrics.

## Future Work
- Improve text processing techniques using advanced NLP models.
- Explore deep learning-based classification approaches.
- Enhance dataset quality with more features.

## Contributors
- Harsh Gupta

## License
This project is licensed under the MIT License.

---
Feel free to modify the content based on your specific implementation.

