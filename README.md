Project Description: This project performs an Airbnb data analysis with the goal of predicting property prices based on various characteristics. Using Machine Learning techniques, the developed model can estimate the nightly price of properties listed on the Airbnb platform, taking into account attributes such as property type, cancellation policies, location, number of rooms, and other factors that influence price.

Key Project Phases:
  1 - Data Collection and Preparation:

        - The dataset used contains information about properties listed on Airbnb, including data such as property type, location, cancellation policies, number of guests, reviews, and more.
        - Data cleaning was performed, missing values were handled, and categorical variables were transformed into numeric ones using techniques like One-Hot Encoding.

  2 - Exploratory Data Analysis (EDA):

        - An exploratory analysis was conducted to understand which variables most influence property prices, identifying trends, correlations, and outliers.
        - Graphical visualizations were used to better understand data distribution and relationships between variables.

  3 - Model Creation and Training:

        - After data preparation, various Regression algorithms were tested, including Linear Regression, Decision Trees, and Random Forest, to predict property prices.
        - The model was fine-tuned to ensure the best possible accuracy, using techniques like Cross-Validation and Grid Search to optimize hyperparameters.

  4 - Model Evaluation:

        - The model's performance was evaluated using metrics like Mean Squared Error (MSE) and R², ensuring that predictions were as accurate as possible.

  5 - Implementation and Testing:

        - The trained model was implemented into a simple interface, allowing users to input property characteristics and receive a predicted nightly price.

Technologies Used:
  Language: Python
  Libraries: Pandas, NumPy, Matplotlib, Seaborn, Scikit-learn, Joblib
  Tools: Jupyter Notebooks, Streamlit (for the prediction interface)
  Models: Linear Regression, Random Forest, XGBoost, among others

Results: The model was able to predict prices with good accuracy, providing a useful tool for both Airbnb hosts looking to optimize their prices and users who wish to estimate the cost of a stay based on specific property features.

dataset airbnb: https://www.kaggle.com/datasets/allanbruno/airbnb-rio-de-janeiro
