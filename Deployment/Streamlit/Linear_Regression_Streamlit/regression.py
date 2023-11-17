import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_percentage_error
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
import pickle

# Load the dataset
df = pd.read_csv("healthcare_dataset.csv")

# Separate independent (features) and dependent (target) variables
X = df[['Age', 'Gender', 'Blood Type', 'Medical Condition']]
y = df['Billing Amount']

# Preprocess the categorical variables using one-hot encoding
categorical_features = ['Gender', 'Blood Type', 'Medical Condition']
one_hot = OneHotEncoder(handle_unknown='ignore')
transformer = ColumnTransformer([("one_hot", one_hot, categorical_features)],
                                 remainder='passthrough')

# Apply transformation to the features
transformed_X = transformer.fit_transform(X)

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(transformed_X, y, test_size=0.2, random_state=42)

# Create and train the linear regression model
regressor = LinearRegression()
regressor.fit(X_train, y_train)

# Predict on the test set
y_pred = regressor.predict(X_test)

# Evaluate the model using Mean Absolute Percentage Error
mape = mean_absolute_percentage_error(y_test, y_pred)
print(f"MAPE: {mape * 100:.2f}%")

# Save the model and transformer to pickle files for later use
with open('linear_regression_model.pkl', 'wb') as file:
    pickle.dump(regressor, file)

with open('transformer.pkl', 'wb') as file:
    pickle.dump(transformer, file)
