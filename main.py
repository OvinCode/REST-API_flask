from flask import Flask, jsonify,request

app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST']) 
def home(): 
    if(request.method == 'GET'): 
  
        data = "hello world"
        bata = "how are you ?"
        return jsonify({'data': data,'question':bata}) 


if __name__ == '__main__': 
  
    app.run(debug = True) 