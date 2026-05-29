
from sklearn.ensemble import IsolationForest
import pandas as pd, joblib
df=pd.read_csv('data/raw/network_logs.csv')
X=df[['bytes_sent','bytes_received','duration']]
m=IsolationForest(random_state=42)
m.fit(X)
joblib.dump(m,'models/isolation_forest.pkl')
