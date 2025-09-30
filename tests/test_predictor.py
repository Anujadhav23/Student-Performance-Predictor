import unittest
from src.models.predictor import StudentPerformancePredictor

class TestStudentPerformancePredictor(unittest.TestCase):

    def setUp(self):
        self.predictor = StudentPerformancePredictor()
        self.predictor.load_model('path/to/your/model')  # Update with the actual model path

    def test_predict_performance(self):
        test_input = {
            'gender': 'female',
            'race/ethnicity': 'group B',
            'parental level of education': 'some high school',
            'lunch': 'standard',
            'test preparation course': 'none',
            'math score': 70,
            'reading score': 75,
            'writing score': 80
        }
        prediction = self.predictor.predict_performance(test_input)
        self.assertIsNotNone(prediction)
        self.assertIn('prediction', prediction)

if __name__ == '__main__':
    unittest.main()