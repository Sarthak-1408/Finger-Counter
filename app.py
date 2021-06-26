from flask import Flask, render_template, request,Response
import cv2 , time
import HandTrackingModule as htm


app = Flask(__name__)
@app.route('/')
def index():
   return render_template('index.html')

wCam , hCam = 640 , 480
cap = cv2.VideoCapture(0)
cap.set(3 , wCam)
cap.set(4 , hCam)
pTime = 0

detector = htm.handDetector(detectionCon=0.75)

# all finger tip id's
tipids = [4 , 8 , 12 , 16 , 20]

def pyshine_process():
    pTime = 0
    while True:
        success , frame = cap.read()
        frame = detector.findHands(frame)
        lmList = detector.findPosition(frame , draw=False)
        if len(lmList) != 0:
            fingers = []

            # Thumb
            if lmList[tipids[0]][1] > lmList[tipids[0] - 1][1]:
                fingers.append(1)
            else:
                fingers.append(0)


            # Four Fingers
            for id in range(1,5):
                if lmList[tipids[id]][2] < lmList[tipids[id] - 2][2]:
                    fingers.append(1)
                else:
                    fingers.append(0)

            
            # print(fingers)
            totalFingers = fingers.count(1)

            cv2.rectangle(frame , (20,225) , (170,425) , (0,255,0) , cv2.FILLED)
            cv2.putText(frame , str(totalFingers) , (45 , 375) , cv2.FONT_HERSHEY_PLAIN , 10 , (255,0,0) , 25)

        cTime = time.time()
        fps = 1/ (cTime - pTime)
        pTime = cTime

        cv2.putText(frame , f"FPS:- {int(fps)}" , (30 , 60) , cv2.FONT_HERSHEY_PLAIN , 2 , (255,0,0) , 3)
        ret , buffer = cv2.imencode(".jpg" , frame)
        frame = buffer.tobytes()
        yield (b'--frame\r\n'
                    b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/res',methods = ['POST','GET'])
def res():
	global result
	if request.method == 'POST':
		result = request.form.to_dict()
		return render_template("results.html",result = result)

@app.route('/video_feed')
def video_feed():
	global result
	return Response(pyshine_process(),mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == "__main__":
    app.run()
