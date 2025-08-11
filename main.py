#!/usr/bin/env python
# coding: utf-8

# In[1]:


from typing import Tuple

import numpy as np
from itertools import product
import cv2


# In[ ]:





# In[ ]:





# In[2]:


#img = cv2.imread('HR_result.png')


# In[5]:


#img = cv2.imread('P:\\DataScience\\\photo_restoration\\data\\5.jpg')
#img = cv2.imread('P:\\DataScience\\\photo_restoration\\data\\12.webp')
img = cv2.imread('P:\\DataScience\\photo_restoration\\flask_app\\static\\loaded_tmp.png', cv2.IMREAD_UNCHANGED)


# In[46]:


img = cv2.imread('P:\\DataScience\\photo_restoration\\flask_app\\static\\loaded_tmp.png', cv2.IMREAD_UNCHANGED)
#img = cv2.imread('P:\\DataScience\\photo_restoration\\flask_app\\static\\loaded_tmp_v.jpg', cv2.IMREAD_UNCHANGED)


# In[56]:


h, w = img.shape[:2]
#w = img.shape[1]
#h = img.shape[0]

if w >= h:
    devider = w / 640
else:
    devider = h / 640

new_w = int(w / devider)
new_h = int(h / devider)

aspect = w / h
new_aspect = new_w / new_h

print(aspect)
print(new_aspect)

print(w, h)
print(new_w, new_h)


# In[ ]:





# In[26]:


cv2.imshow('current image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()


# In[5]:


img2 = cv2.resize(img, (640, 480))


# In[6]:


cv2.imshow('current image', img2)
cv2.waitKey(0)
cv2.destroyAllWindows()


# In[9]:


cv2.imwrite('P:\\DataScience\\photo_restoration\\flask_app\\static\\before.jpg', img2)


# In[ ]:





# In[ ]:


@app.route('/hello')
def hello():
    return 'Hello, World'


# In[5]:


class PhotoRestoreaiton():

    def __init__(self, ):
        self._img_before_url = ''
        self._img_after_url = ''

        self._model = None

    
    def set_url_before(self, inp_url: str):
        self._img_before_url = inp_url

    def set_url_after(self, inp_url: str):
        self._img_after_url = inp_url
    
    def restore(self, ):
        pass


# In[ ]:





# In[ ]:





# In[ ]:


<p><input type="hidden" name="folder" size="200" /></p>


# In[ ]:


def check_and_save_photo_before(inp_request) -> None:

    if 'file' not in inp_request.files:
        flash('No file part')
        return redirect(inp_request.url)

    file = inp_request.files['before_name']
    if file.filename == '':
        flash('No selected file')
        return redirect(inp_request.url)

    return 0

