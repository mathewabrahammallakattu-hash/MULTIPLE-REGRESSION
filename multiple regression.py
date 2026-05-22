import pandas as pd  
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import joblib
data = pd.read_csv("powerdata.csv")
x = data[["windspeed","bladeangle",'rotorspeed']]
y = data[["poweroutput"]]
model= LinearRegression()
model.fit(x,y)
print(model.coef_)
print(model.intercept_)
# Save the trained model
joblib.dump(model, "model.pkl")
print("Model saved as model.pkl")
   


