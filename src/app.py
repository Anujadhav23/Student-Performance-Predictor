from flask import Flask, render_template, request
import os
import sys

# Add the current directory to Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from models.predictor import StudentPerformancePredictor

app = Flask(__name__)
predictor = StudentPerformancePredictor()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get form data
        features = {
            'gender': request.form['gender'],
            'race/ethnicity': request.form['race'],
            'parental level of education': request.form['education'],
            'lunch': request.form['lunch'],
            'test preparation course': request.form['test_prep'],
            'math score': float(request.form['math']),
            'reading score': float(request.form['reading']),
            'writing score': float(request.form['writing'])
        }
        
        # Make prediction
        prediction = predictor.predict(features)
        
        return render_template('results.html', prediction=prediction)
    except Exception as e:
        return render_template('index.html', error=str(e))

if __name__ == '__main__':
    app.run(debug=True)