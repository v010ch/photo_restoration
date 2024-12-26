import os
import time
from flask import Flask, render_template, request

app = Flask(__name__)



@app.route("/", methods=["POST", "GET"])
def index_page():
#def index_page(text: Optional[str] = '', model_type: Optional[str] = '', prediction_message: Optional[str] = ''):

   #return render_template('index.html', text=text, model_type=model_type, prediction_message=prediction_message)
    return render_template('index.html')
    
    return render_template('index-Copy1.html')



if __name__ == "__main__":
    app.run()
