import os
from typing import Optional
import time

import cv2
from flask import Flask, flash, render_template, request, redirect, url_for


UPLOAD_FOLDER = os.path.join('.', 'static')


app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.secret_key = b'_5#y2L"F4Q8zxec]/'


def check_and_save_photo_before(inp_request) -> None:

    if 'before_name' not in inp_request.files:
        flash('Системная ошибка. Отсутствуют необходимые данные в запросе. Обратитесь к разработчику.')
        return -1 

    file = inp_request.files['before_name']
    if file.filename == '':
        flash('Изображение не выбрано. Необходимо выбрать изображение для восстановления.')
        return -2

    filename = 'loaded_tmp.' + file.filename.split('.')[-1].lower()
    file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

    return 0



def restore(inp_img) -> None:

    cv2.imwrite(os.path.join(app.config['UPLOAD_FOLDER'], 'after.jpg'),
               inp_img)
    return 0



def prepare_for_publication(inp_request) -> None:
    file = inp_request.files['before_name']
    filename = 'loaded_tmp.' + file.filename.split('.')[-1].lower()
    img = cv2.imread(os.path.join(app.config['UPLOAD_FOLDER'], filename), 
                     cv2.IMREAD_UNCHANGED)

    w = img.shape[1]
    h = img.shape[0] 
    if w >= h:
        devider = w / 640
    else:
        devider = h / 640
    new_w = int(w / devider)
    new_h = int(h / devider)

    img = cv2.resize(img, (new_w, new_h))
    cv2.imwrite(os.path.join(app.config['UPLOAD_FOLDER'], 'before.jpg'),
        img)

    restore(img)

    return 0



@app.route("/", methods=["POST", "GET"])
def index_page():

    print('index_page ', request.method)
    if request.method == "POST":
        ret = check_and_save_photo_before(request)
        if ret != 0:
            return redirect(request.url)

        prepare_for_publication(request)
        return redirect(url_for('restored'))
    else:
        pass

    return render_template('index.html')



@app.route("/restored", methods=["POST", "GET"])
def restored():
    print('restored ', request.method)
    if request.method == "POST":
        print(request.form)
        if ('back' in request.form) and request.form['back']:
            return redirect(url_for('index_page'))

    return render_template('before_after.html')    



if __name__ == "__main__":
    app.run()
