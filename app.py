from flask import Flask, render_template,request,jsonify
import pickle
import numpy as np
import os

filename = 'heart-disease-model.pkl'
model = pickle.load(open(filename,'rb'))

app = Flask(__name__)

IMG_FOLDER = os.path.join("static", "PNG")
app.config["UPLOAD_FOLDER"] = IMG_FOLDER

@app.route('/')
def index():
    image = os.path.join(app.config["UPLOAD_FOLDER"], "heart-rate_9424143.png")
    return render_template('index.html', user_image=image)

@app.route('/predict', methods=['GET','POST'])
def predict():
   if request.method == 'POST':
      bmi = float(request.form['bmi'])
      smoking = int(request.form['smoking'])
      alcoholdrinking = int(request.form['alcoholdrinking'])
      stroke = int(request.form['stroke'])
      physicalhealth = int(request.form['physicalhealth'])
      mentalhealth = int(request.form['mentalhealth'])
      diffwalking = int(request.form['diffwalking'])
      sex = int(request.form['sex'])
      age = int(request.form['age'])
      race = int(request.form['race'])
      diabetic = int(request.form['diabetic'])
      physicalactivity = int(request.form['physicalactivity'])
      genhealth = int(request.form['genhealth'])
      sleeptime = int(request.form['sleeptime'])

      asthma = int(request.form['asthma'])
      kidneydisease = int(request.form['kidneydisease'])
      skincancer = int(request.form['skincancer'])
      image = os.path.join(app.config["UPLOAD_FOLDER"], "heart-rate_9424143.png")

      data = np.array([[bmi,smoking,alcoholdrinking,stroke,physicalhealth,mentalhealth,diffwalking,sex,age,race,diabetic,physicalactivity,genhealth,sleeptime,asthma,kidneydisease,skincancer]])
      my_prediction = model.predict(data)
      # if my_prediction == 1:
      #     result = 'Khong co benh tim'
      # else:
      #    result = 'Ban mac benh tim'
      print(my_prediction)
      print (bmi,smoking,alcoholdrinking,stroke,physicalhealth,mentalhealth,diffwalking,sex,age,race,diabetic,physicalactivity,genhealth,sleeptime,asthma,kidneydisease,skincancer)
      return render_template('result.html', prediction=my_prediction, user_image=image)
      

   
if __name__ == '__main__':
    app.run(debug=True)
