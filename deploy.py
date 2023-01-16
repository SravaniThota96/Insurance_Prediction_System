from flask import Flask, request, render_template
import pandas as pd
import pickle
from flask_cors import CORS
#from pycaret.regression import predict_model,load_model
from sklearn.ensemble import GradientBoostingRegressor

#from flask.ext.cors import CORS, cross_origin

app = Flask(__name__)
CORS(app)
# file = open("xgb.pkl", 'rb')
# model = xgboost.XGBRegressor()
# model.load_model("xgb2.json")
model = pickle.load(open("final_model.pkl", 'rb'))
# model = load_model('')

# data = pd.read_csv('./clean_data.csv')
# data.head()

@app.route('/')
def index():
    
    return "<h1>Hello </h1>"
gender_map = {"male" : 0,
                     "female" : 1}
smoker_map = {"no":0,"yes":1}
region_map = {"northwest":1,"northeast":2,"southwest":3,"southeast":4}
@app.route('/predict', methods=['POST'])
def predict():
    print("request")
    print(request)
    age = request.form.get('age')
    sex = request.form.get('sex')
    bmi = request.form.get('bmi')
    children = request.form.get('children')
    smoker = request.form.get('smoker')
    region =request.form.get('region')
    print(age,sex,bmi,children,smoker,region)

    prediction = model.predict(pd.DataFrame([[age, sex, bmi, children, smoker, region]], 
                columns=["age","sex","bmi","dependants","smoker","region"]))
    #print(prediction)
    # prediction = predict_model(model, data = pd.DataFrame([[age, sex, bmi, children, smoker, region]], 
    #              columns=["age","sex","bmi","dependants","smoker","region"]))
    print(prediction)
    print(model)
    return str(prediction[0])           
    #return "hi"

if __name__=="__main__":
    app.run(debug=True)
