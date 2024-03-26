import sys
import pickle
import json

with open("alert_model.pkl", "rb") as f:
    alert_model = pickle.load(f)

with open("description_model.pkl", "rb") as f:
    description_model = pickle.load(f)

form_data = json.loads(sys.argv[1])

# Retrieve form data
age = int(form_data["age"])
trestbps = int(form_data["trestbps"])
chol = int(form_data["chol"])
thalch = int(form_data["thalch"])
oldpeak = float(form_data["oldpeak"])
ca = int(form_data["ca"])
oxygen_level = int(form_data["oxygen_level"])
heart_condition = int(form_data["heart_condition"])
sex = int(form_data["sex"])
cp = int(form_data["cp"])
fbs = int(form_data["fbs"])
restecg = int(form_data["restecg"])
slope = int(form_data["slope"])
thal = int(form_data["thal"])
exang = int(form_data["exang"])

# Convert categorical variables to one-hot encoding
sex_Female = 1 if sex == 0 else 0
sex_Male = 1 if sex == 1 else 0

cp_asymptomatic = 1 if cp == 0 else 0
cp_atypicalAngina = 1 if cp == 1 else 0
cp_nonAnginal = 1 if cp == 2 else 0
cp_typicalAngina = 1 if cp == 3 else 0

fbs_False = 1 if fbs == 0 else 0
fbs_True = 1 if fbs == 1 else 0

restecg_lvhypertrophy = 1 if restecg == 0 else 0
restecg_normal = 1 if restecg == 1 else 0
restecg_sttAbnormality = 1 if restecg == 2 else 0

slope_downsloping = 1 if slope == 0 else 0
slope_flat = 1 if slope == 1 else 0
slope_upsloping = 1 if slope == 2 else 0

thal_fixedDefect = 1 if thal == 0 else 0
thal_normal = 1 if thal == 1 else 0
thal_reversableDefect = 1 if thal == 2 else 0

exang_False = 1 if exang == 0 else 0
exang_True = 1 if exang == 1 else 0

# Make predictions using the loaded models
alert_prediction = alert_model.predict([[age, trestbps, chol, thalch, oldpeak, ca, oxygen_level, heart_condition,
                                          sex_Female, sex_Male, cp_asymptomatic, cp_atypicalAngina, cp_nonAnginal,
                                          cp_typicalAngina, fbs_False, fbs_True, restecg_lvhypertrophy, restecg_normal,
                                          restecg_sttAbnormality, slope_downsloping, slope_flat, slope_upsloping,
                                          thal_fixedDefect, thal_normal, thal_reversableDefect, exang_False, exang_True]])[0]

description_prediction = description_model.predict([[age, trestbps, chol, thalch, oldpeak, ca, oxygen_level, heart_condition,
                                                     sex_Female, sex_Male, cp_asymptomatic, cp_atypicalAngina, cp_nonAnginal,
                                                     cp_typicalAngina, fbs_False, fbs_True, restecg_lvhypertrophy, restecg_normal,
                                                     restecg_sttAbnormality, slope_downsloping, slope_flat, slope_upsloping,
                                                     thal_fixedDefect, thal_normal, thal_reversableDefect, exang_False, exang_True]])[0]

# Return predictions as JSON
predictions = [alert_prediction, description_prediction]
print(json.dumps(predictions))
