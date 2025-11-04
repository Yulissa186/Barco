from rest_framework.decorators import api_view
from rest_framework.response import Response
import joblib

# Cargar modelo y codificadores
model = joblib.load("titanic_model.pkl")
label_sex = joblib.load("label_sex.pkl")
label_emb = joblib.load("label_emb.pkl")

@api_view(['POST'])
def predict_survival(request):
    try:
        data = request.data
        Pclass = int(data["Pclass"])
        Sex = "male" if data["Sex"] == "Hombre" else "female"
        Sex_num = label_sex.transform([Sex])[0]
        Age = float(data["Age"])
        Fare = float(data["Fare"])
        Embarked_num = label_emb.transform([data["Embarked"].upper()])[0]

        pred = model.predict([[Pclass, Sex_num, Age, Fare, Embarked_num]])[0]
        prob = model.predict_proba([[Pclass, Sex_num, Age, Fare, Embarked_num]])[0][1]

        return Response({
            "prediction": int(pred),
            "probability": round(prob * 100, 2)
        })
    except Exception as e:
        return Response({"error": str(e)})
