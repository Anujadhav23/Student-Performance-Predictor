import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestRegressor
import joblib
import os

def train_model():
    # Get the current directory path
    current_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Load data
    data_path = os.path.join(os.path.dirname(current_dir), 'data', 'StudentsPerformance.csv')
    df = pd.read_csv(data_path)
    
    # Define columns
    categorical_cols = [
        'gender', 
        'race/ethnicity', 
        'parental level of education',
        'lunch', 
        'test preparation course'
    ]
    numeric_cols = ['math score', 'reading score', 'writing score']
    
    # Create and fit encoders for each categorical column
    encoders = {}
    for col in categorical_cols:
        encoders[col] = LabelEncoder()
        df[col] = encoders[col].fit_transform(df[col])
    
    # Calculate average score
    df['average_score'] = df[numeric_cols].mean(axis=1)
    
    # Prepare features and target
    X = df[categorical_cols + numeric_cols]
    y = df['average_score']
    
    # Split data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Train model
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    
    # Save model and encoders
    joblib.dump(model, os.path.join(current_dir, 'student_performance_model.pkl'))
    joblib.dump(encoders, os.path.join(current_dir, 'encoders.pkl'))
    
    print(f"Model R² Score: {model.score(X_test, y_test):.4f}")

if __name__ == "__main__":
    train_model()