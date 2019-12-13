

# Darknet #
Darknet is an open source neural network framework written in C and CUDA. It is fast, easy to install, and supports CPU and GPU computation.


For custom object detection 
1.Run the yolo.py file inside YOLO folder ,with input images directory path,labels dir path and class names file's path .there you go ! Now you have all the required files to train your custom object detector 


2.Now you have to change configuration file for your custom object detector by choosing any of the model from cfg folder and copy the model configuration file inside YOLO folder and change .

filter = 3 * (5 + #number of classes)    
classes = #number of classes

3. run darknet detector  , There you go ! you have your weights now :)


4. You can test it by replacing your weight file path ,image path and cfg file path in custom_detector.py 

For more information see the [Darknet project website](http://pjreddie.com/darknet).

For questions or issues please use the [Google Group](https://groups.google.com/forum/#!forum/darknet).
