# Student Performance Predictor

A machine learning web application that predicts student performance based on various demographic and academic factors. The application uses Random Forest Regression to analyze and predict student scores.

## 🎯 Features

- Predicts student performance based on multiple factors
- Interactive web interface for data input
- Real-time predictions
- Supports various demographic and academic parameters
- Score validation and error handling
- Responsive design

## 🛠️ Technologies Used

- **Python 3.x**
  - Flask (Web Framework)
  - Scikit-learn (Machine Learning)
  - Pandas (Data Processing)
  - NumPy (Numerical Operations)
  - Joblib (Model Serialization)

- **Frontend**
  - HTML5
  - CSS3
  - JavaScript
  - Responsive Design

- **Machine Learning**
  - Random Forest Regression
  - Label Encoding
  - Train-Test Split
  - Model Persistence

## 📊 Dataset

The project uses the "Students Performance in Exams" dataset, which includes:
- Gender
- Race/Ethnicity
- Parental Level of Education
- Lunch Type
- Test Preparation Course
- Math Score
- Reading Score
- Writing Score

## 🚀 Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/student-performance-predictor.git
cd student-performance-predictor
```

2. Create a virtual environment (optional but recommended):
```bash
python -m venv venv
source venv/bin/activate  # For Linux/Mac
venv\Scripts\activate     # For Windows
```

3. Install required packages:
```bash
pip install -r requirements.txt
```

4. Train the model:
```bash
cd src/models
python train_model.py
```

5. Run the application:
```bash
cd ..
python app.py
```

6. Open your browser and navigate to:
```
http://127.0.0.1:5000
```

## 📁 Project Structure

```
student-performance-predictor/
├── src/
│   ├── data/
│   │   └── StudentsPerformance.csv
│   ├── models/
│   │   ├── __init__.py
│   │   ├── predictor.py
│   │   └── train_model.py
│   ├── static/
│   │   └── styles.css
│   ├── templates/
│   │   ├── index.html
│   │   └── results.html
│   └── app.py
├── requirements.txt
└── README.md
```

## 💡 Usage

1. Fill in the student's demographic information:
   - Gender
   - Race/Ethnicity
   - Parental Education Level
   - Lunch Type
   - Test Preparation Course Status

2. Enter test scores (0-100):
   - Math Score
   - Reading Score
   - Writing Score

3. Click "Predict Performance" to get the prediction

## 📈 Model Performance

- Algorithm: Random Forest Regressor
- Metrics: R² Score
- Current Model Performance: 0.994

## 📸 Screenshots

### Input Form
![Input Form](screenshots/input_form.png)
*Input form with student information and test scores*

### Prediction Results
![Prediction Results](screenshots/prediction_results.png)
*Prediction results showing the estimated average score*

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Dataset source: Kaggle
- Inspiration: Educational Data Mining
- Contributors and Open Source Community

## 👤 Author

Your Name
- GitHub: [@yourusername](https://github.com/yourusername)
- LinkedIn: [Your Name](https://linkedin.com/in/yourprofile)

## 🔗 Links

- Project Link: [https://github.com/yourusername/student-performance-predictor](https://github.com/yourusername/student-performance-predictor)
- Dataset Link: [Kaggle - Students Performance in Exams](https://www.kaggle.com/datasets/spscientist/students-performance-in-exams)