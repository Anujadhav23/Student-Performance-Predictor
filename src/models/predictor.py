import joblib
import os
import numpy as np

class StudentPerformancePredictor:
    def __init__(self):
        current_dir = os.path.dirname(os.path.abspath(__file__))
        self.model = joblib.load(os.path.join(current_dir, 'student_performance_model.pkl'))
        self.encoders = joblib.load(os.path.join(current_dir, 'encoders.pkl'))

    def predict(self, features):
        try:
            # Convert categorical features using corresponding encoders
            categorical_cols = [
                'gender', 
                'race/ethnicity', 
                'parental level of education',
                'lunch', 
                'test preparation course'
            ]
            
            # Process each categorical feature with its specific encoder
            categorical_values = []
            for col in categorical_cols:
                value = features[col]
                encoder = self.encoders[col]
                encoded_value = encoder.transform([value])[0]
                categorical_values.append(encoded_value)
            
            # Get numeric scores as floats
            numeric_values = [
                float(features['math score']),
                float(features['reading score']),
                float(features['writing score'])
            ]
            
            # Combine features in correct order
            X = np.array(categorical_values + numeric_values).reshape(1, -1)
            
            # Make prediction
            prediction = self.model.predict(X)[0]
            
            return float(prediction)
            
        except Exception as e:
            raise Exception(f"Error making prediction: {str(e)}")