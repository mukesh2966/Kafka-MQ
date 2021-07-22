from json import dump
import joblib
import os


dump_file=os.path.join(os.path.dirname(__file__),"model_dump")

print(dump_file)
loaded_model=joblib.load(dump_file)

def predict(arguments):

    exp=float(arguments.get("exp"))
    predicted_value=loaded_model.predict([[exp]])
    return str(predicted_value[0])