import os
from typing import Optional
import time

import cv2
from flask import Flask, render_template, request, redirect


UPLOAD_FOLDER = 'static'


app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


def check_and_save_photo_before(inp_request) -> None:

    if 'before_name' not in inp_request.files:   #CHECK
        flash('No file part')
        return redirect(inp_request.url)

    file = inp_request.files['before_name']
    print(type(file))
    if file.filename == '':                      #CHECK
        flash('No selected file')
        return redirect(inp_request.url)

    #filename = secure_filename(file.filename)
    filename = 'loaded_tmp.' + file.filename.split('.')[-1].lower()
    file.save(os.path.join('.', app.config['UPLOAD_FOLDER'], filename))

    return 0



def prepare_for_publication(inp_request) -> None:
    file = inp_request.files['before_name']
    filename = 'loaded_tmp.' + file.filename.split('.')[-1].lower()
    img = cv2.imread(os.path.join('.', app.config['UPLOAD_FOLDER'], filename), 
                     cv2.IMREAD_UNCHANGED)
    img = cv2.resize(img, (640, 480))
    cv2.imwrite(os.path.join('.', app.config['UPLOAD_FOLDER'], 'before.jpg'),
        img)

    return 0



@app.route("/", methods=["POST", "GET"])
def index_page(file_before_url: Optional[str] = ''):
#def index_page(text: Optional[str] = '', model_type: Optional[str] = '', prediction_message: Optional[str] = ''):

    print(request.method)
    if request.method == "POST":
        print('post')
        check_and_save_photo_before(request)
        prepare_for_publication(request)

        tmp = request.files
        print(type(tmp))

        return render_template('index.html')
    else:
        #print('get')
        pass

    return render_template('before_after.html')    
    return render_template('index.html')




if __name__ == "__main__":
    app.run()
