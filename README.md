# Drowsiness-Detection

I built a drowsiness detection model using yolovs
This is a small model built on a set of small number of imgaes(40), collected personally using a webcam and i used the yolov5s model to build a custom object detection model with just two classes.
I also integrated a custom alarm system to a video stream (webcam) to relay signs and information to keep our user awake, when drowsy for a certain period of time.

The trchyolo.ipynb file contains the image collection and custom model building process, I will recommend @nicholas renotte onn youtube as he has a very comprehensive tutorial on this topic.
The trchyolo.py file contains code utilizing our trained model and our alarm logic(which can still be improved)

Our model can be still be improved in various ways such as supplying more images, using bigger models and training for more epochs

Thanks Guys
