# Software Developer Salary Predictor
### [Let's Predict ]( https://lets-predict-salary.streamlit.app/) ![Predict](https://img.shields.io/badge/Streamlit-orange)


This project is a web application that predicts the salary of software developers based on their country, education level, and years of experience. The application uses a Random Forest model trained on data from the Stack Overflow Developer Survey 2023.

## Project Structure

- `app.py`: The main entry point of the application, where users can choose to explore data or predict salaries.
- `predict_page.py`: Contains the functionality to gather user input and predict salaries.
- `explore_page.py`: Provides an interactive exploration of the salary data.
- `Salary_prediction.ipynb`: A Jupyter Notebook used for data analysis, feature engineering, and model training.
- `Salary_Prediction/models/`: Directory where the trained model and encoders are saved.

## Features

- **Salary Prediction**: Predicts the salary of a software developer based on their country, education level, and years of experience.
- **Data Exploration**: Visualizes salary data by country and experience level, using charts like bar charts, line charts, and pie charts.

## Getting Started

### Prerequisites

- Python 3.8 or higher
- Required Python libraries listed in `requirements.txt`

### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/Ganesh2409/salary-predictor.git
    cd salary-predictor
    ```

2. Install the required packages:

    ```bash
    pip install -r requirements.txt
    ```

3. Run the application:

    ```bash
    streamlit run app.py
    ```

## Usage

1. **Predict Salary**: Navigate to the "Predict" page, select your country, education level, and years of experience, then click "Calculate Salary". The application will display the predicted salary.
  
2. **Explore Data**: On the "Explore" page, you can visualize salary distributions by country and experience.

## Model Information

- **Data**: The model is trained on data from the Stack Overflow Developer Survey 2023.
- **Algorithms**: The application uses a Random Forest Regressor to predict salaries.
- **Preprocessing**:
  - Label Encoding: For the country column.
  - Ordinal Encoding: For the education level column.
## Model Improvement:

- **Try Different Algorithms**: Experiment with other machine learning models like Gradient Boosting, XGBoost, or Neural Networks to see if they offer better performance than Random Forest.
- **Hyperparameter Tuning**: Perform more advanced hyperparameter tuning using techniques like Bayesian optimization or Genetic Algorithms to further improve the model's accuracy.
## Contributing

Contributions are welcome! Please fork this repository and submit a pull request with your changes.

## Contact
For any questions or feedback, please contact:
- **Name** - [Ganesh Chowdhary P]()
- **Email** - [pinnamaneniganesh24@gmail.com ](mailto:your.pinnamaneniganesh24@gmail.com)

I look forward to hearing from you!
