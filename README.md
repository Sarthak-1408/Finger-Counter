# Finger Counter:

## Table of Content
  * [Demo](#demo)
  * [Overview](#overview)
  * [Motivation](#motivation)
  * [Installation](#installation)
  * [Directory Tree](#directory-tree)
  * [Bug / Feature Request](#bug---feature-request)
  * [Future scope of project](#future-scope)

## Demo
https://user-images.githubusercontent.com/72247049/123632646-cd0d4f80-d835-11eb-86f1-b2b3bf3c5924.mp4

![Screenshot from 2021-06-28 16-54-56](https://user-images.githubusercontent.com/72247049/123632902-1c538000-d836-11eb-8094-06f68446df6e.png)

![Screenshot from 2021-06-28 16-55-00](https://user-images.githubusercontent.com/72247049/123633267-9edc3f80-d836-11eb-8d63-3d094acbd4a7.png)

## Overview
- Finger Counter is Flask web app to Count the number on finger in a Real time feed.
- I used [Mediapipe](https://google.github.io/mediapipe/) framework to build a HandTrackingModule and it's very helpfull to get the best Accuracy result , discovered by google.
- I also used [opencv-python](https://docs.opencv.org/4.5.2/d6/d00/tutorial_py_root.html) library to create videostream handle all the other thing like putting text , putting rectangle etc.
- The Aim of this project , we can easily teach the Countings of children in a exited way with the help of the Visualization.

## Motivation
In this world , Only Education is one way you can achieve everything in this life so nothing is impossible , sometime if you feel low so just remember one thing why i started this things and what i want in future So stand and learn the machine learning because trust me machine learning is so amazing.

## Installation
The Code is written in Python 3.8.5. If you don't have Python installed you can find it [here](https://www.python.org/downloads/). If you are using a lower version of Python you can upgrade using the pip package, ensuring you have the latest version of pip. To install the required packages and libraries, run this command in the project directory after [cloning](https://www.howtogeek.com/451360/how-to-clone-a-github-repository/) the repository:
```bash
pip install -r requirements.txt
```

## Directory Tree
```
├── __pycache__ 
│   ├── HandTrackingModule.cpython-38.pyc
├── template
│   ├── index.html , results.html
├── Procfile
├── README.md
├── app.py
├── HandTrackingModule.py
├── requirements.txt
```
## Technologies Used

![](https://forthebadge.com/images/badges/made-with-python.svg)

[<img target="_blank" src="https://flask.palletsprojects.com/en/1.1.x/_images/flask-logo.png" width=170>](https://flask.palletsprojects.com/en/1.1.x/) [<img target="_blank" src="https://number1.co.za/wp-content/uploads/2017/10/gunicorn_logo-300x85.png" width=280>](https://gunicorn.org) [<img target="_blank" src="https://google.github.io/mediapipe/images/logo_horizontal_color.png" width=200>](https://google.github.io/mediapipe/) 

## Bug / Feature Request

If you find a bug (the code couldn't handle the query and / or gave undesired results), kindly open an issue section here and enter your query and in a 1 to 2 days i will solve your problems or you can also mail me about the problem
- sarthakparashar1408@gmail.com

## Future Scope

* Use multiple Algorithms
* Optimize Flask app.py
* Front-End 
* Deployment
