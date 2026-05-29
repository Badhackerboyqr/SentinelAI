
import joblib
class AnomalyDetector:
    def __init__(self):
        self.model=joblib.load('models/isolation_forest.pkl')
