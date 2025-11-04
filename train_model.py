import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import LabelEncoder
import joblib

# Cargar dataset
data = pd.read_csv("train.csv")
cols = ["Pclass", "Sex", "Age", "Fare", "Embarked", "Survived"]
data = data[cols].dropna()

# Codificadores
label_sex = LabelEncoder()
label_emb = LabelEncoder()
data["Sex"] = label_sex.fit_transform(data["Sex"])
data["Embarked"] = label_emb.fit_transform(data["Embarked"])

# Guardar codificadores
joblib.dump(label_sex, "label_sex.pkl")
joblib.dump(label_emb, "label_emb.pkl")

# Entrenar modelo
X = data.drop("Survived", axis=1)
y = data["Survived"]
model = DecisionTreeClassifier(max_depth=4, random_state=42)
model.fit(X, y)

# Guardar modelo entrenado
joblib.dump(model, "titanic_model.pkl")
print("Modelo entrenado y guardado")
