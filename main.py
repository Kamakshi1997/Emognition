#!usr/bin/python3
# main.py

from flask import Flask, render_template, Response
#from camera import VideoCamera
from emotion_recognition import EmotionRecognition


app = Flask(__name__)
#web page
page="""
<html>
<body background="qwe.jpg">
<h1 style="font-family:Comic Sans MS;font-size:400%;color:white"> Try your Facial Expressions here...</h1>
<img src="emoji1.jpg" width="200" height="200">
<img src="emoji4.jpg" width="200" height="200">
<img src="emoji2.jpg" width="200" height="200">
<a href="http://0.0.0.0:5000/video_feed" >click here </a>
<br/>  <br/>  <br/> <br/>
</body>
</html>
"""
@app.route('/')

def index():
	return page
        #return render_template('index.html')

'''def gen(camera):
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')'''

@app.route('/video_feed')
def video_feed():
	#return Response(gen(EmotionRecognition()),mimetype='multipart/x-mixed-replace;boundary=frame')
	import poc

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
