Project Description:
This project analyzes Airbnb data with the aim of predicting property prices based on several characteristics. Using Machine Learning techniques, the model developed is capable of estimating the daily value of properties listed on the Airbnb platform, considering attributes such as property type, cancellation policies, location, number of bedrooms, and other factors that impact the price.

Main steps of the project:
Data Collection and Preparation:

The dataset used contains information about the properties listed on Airbnb, including data such as property type, location, cancellation policies, number of guests, reviews, and more.
Data was cleaned, missing values ​​were treated, and categorical variables were transformed into numeric variables, using techniques such as One-Hot Encoding.
Exploratory Data Analysis (EDA):

An exploratory analysis was performed to understand the variables that most impact property prices, identifying trends, correlations, and outliers.
Graphical visualizations were used to better understand the distribution of data and the relationships between variables.
Creating and Training the Prediction Model:

After preparing the data, different regression algorithms such as Linear Regression, Decision Trees, and Random Forest were tested to predict property prices.
The model was tuned to ensure the best possible accuracy, using techniques such as Cross-Validation and Grid Search to optimize the hyperparameters.
Model Evaluation:

The performance of the model was evaluated using metrics such as Mean Squared Error (MSE) and R², ensuring that the predictions were as accurate as possible.
Implementation and Testing:

The trained model was implemented in a simple interface, allowing users to input the characteristics of a property and receive a prediction of its daily rate.
Technologies Used:
Language: Python
Libraries: Pandas, NumPy, Matplotlib, Seaborn, Scikit-learn, Joblib
Tools: Jupyter Notebooks, Streamlit (for the forecasting interface)
Models: Linear Regression, Random Forest, XGBoost, among others
Results:
The model was able to predict prices with good accuracy, providing a useful tool for both Airbnb hosts looking to optimize their prices and users who want to estimate the cost of a stay based on certain characteristics of a property.

dataset airbnb: https://www.kaggle.com/datasets/allanbruno/airbnb-rio-de-janeiro
