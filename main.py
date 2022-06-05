import json 
from flask import Flask,render_template,request, jsonify
from flask_cors import CORS
#<strong>#Set up Flaskstrong>:
app = Flask(__name__)
#<strong>#Set up Flask to bypass CORSstrong>:
cors = CORS(app)
#Create the receiver API POST endpoint:
@app.route("/")
def index():
     return render_template("index.html")

@app.route("/receiver", methods=["POST"])
def postME():
   data = request.get_json()
   len_data = len(data)
   for r in range(0,len_data):
       json_data = data[r]
       print(json_data,len_data)
   data = jsonify(data)
   
   return data
if __name__ == "__main__": 
   app.run(debug=True)
