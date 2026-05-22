import joblib
model = joblib.load("model.pkl")
user_windspeed = float(input("Enter windspeed: "))
user_bladeangle = float(input("Enter blade angle: "))
user_rotorspeed = float(input("Enter rotor speed: "))
new_extension = model.predict([[user_windspeed, user_bladeangle, user_rotorspeed]])
print(new_extension) 