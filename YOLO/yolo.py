#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 10:51:06 2019

@author: sanath vernekar
"""
'''
#pipeline for training on any YOLO model with configuration 
#usage #
python3 yolo.py --imagedir = "/home/sanath/work/test_python/pipeline_for_YOLO/images" --labeldir="/home/sanath/work/test_python/pipeline_for_YOLO/labels" --newdataset="y" --labelnames="/home/sanath/work/test_python/pipeline_for_YOLO/classes.txt" 


'''
import os
from util import download_pre_requisites as prereq
from util import test_train as tt
from util import copy_files
from util import classes
#import random
#import sys 

import argparse

def main():
    # Initiate argument parser
    parser = argparse.ArgumentParser(description="Pipeline for YOLO Custom Object Detection")
    parser.add_argument("-i","--imagedir",
                        help="Path to the folder where the input image files are stored",type=str)
    parser.add_argument("-l","--labeldir",
                        help="Path to the folder where the input image files are stored", type=str)
    parser.add_argument("-d" ,"--newdataset", default ="no",
                    choices=["yes", "y", "no", "n"],
                    type=str, help="Do you want seperate dataset to be created inside this folder , enter no to deny")
    parser.add_argument("-n","--labelnames", type =str ,help = "Enter the file path containing labels of your custom dataset ")
    args = parser.parse_args()
    cwd=os.getcwd()
    
    #validate arguments if they are correct 
    
    ImageDirectory=str(args.imagedir)
    LabelDirectory=str(args.labeldir)
    classnames= str(args.labelnames)
    flg=args.newdataset
    # You can even give path directly here by uncommenting the below lines
    ImageDirectory="/home/sanath/work/test_python/pipeline_for_YOLO/images"
    LabelDirectory="/home/sanath/work/test_python/pipeline_for_YOLO/labels"
    classnames= "/home/sanath/work/test_python/pipeline_for_YOLO/classes.txt"
    
    
    print("input images directory is ",ImageDirectory)
    print("input labels directory is ",LabelDirectory)
    
    
    
    if(ImageDirectory == 'None'):
        ImageDirectory = os.path.join(cwd,"images")
    if(LabelDirectory == 'None'):
        LabelDirectory = os.path.join(cwd,"labels")
    if (classnames == 'None'):
        classnames=os.path.join(cwd,"objects.names")
    if not os.path.exists(classnames):
        print("class names file doesnot exist or the path might be wrong !")
        exit()
    if not os.path.exists(ImageDirectory):
        print("images directory doesnot exist or the path might be wrong !")
        exit()
    if not os.path.exists(LabelDirectory):
        print("labels directory doesnot exist or the path might be wrong !")
        exit()
        
        
        
    #print("current working directory is ",cwd)
    
    a = open("LabelDataset.txt", "w")
    b = open("ImageDataset.txt","w")
    c = open("No_corresponding_label.txt","w" )
    d = open("Just_file_names.txt","w")
    total_count=0
    for path ,suddirs, files in os.walk(ImageDirectory):
        for filename in files :
            fname,ext=os.path.splitext(filename)
            if ext == '.jpg':
                txtname=fname+".txt"
                txtpath=os.path.join(LabelDirectory,txtname)
                total_count+=1
                if os.path.isfile(txtpath):
                    a.write(str(os.path.join(LabelDirectory,txtname))+os.linesep)
                    b.write(str(os.path.join(path,filename))+os.linesep)
                    d.write(str(fname)+os.linesep)
                else :
                    c.write(str(os.path.join(path,filename))+os.linesep)
    print("Total count of Dataset images is ", total_count)
    #the file No_corresponding_label.txt contains all the files without corresponding label for the given image
    #so either you can delete it manually or run the script in the flder to delete files 
    #To check if file No_correspondin_label.txt is empty 
    d.close()
    a.close()
    b.close()
    c.close()
    if os.stat("No_corresponding_label.txt").st_size == 0:
        os.remove("No_corresponding_label.txt")
        print("Dataset is verified")
    else :
        print("******************NOTE****************")
        print("The Dataset contains few image files, which are not annotated , The file names are stored in No_corresponding_label.txt file ")
        #Run the query script , which can move the images or label files from original dataaset to other folder 

    imgpath=ImageDirectory
    labelpath=LabelDirectory
    if flg =="yes" or flg =="y":
        imgpath=os.path.join(os.getcwd(),"ImageDataset")
        labelpath=os.path.join(os.getcwd(),"LabelDataset")
        copy_files("ImageDataset.txt","ImageDataset")
        copy_files("LabelDataset.txt","LabelDataset")
        
    
    #check for pre requisites 
    prereq()
    #create test and train files
    tt(total_count, imgpath , labelpath)
    #create objects.names file ,where all the classes are mentioned 
    NumberOfClasses=classes(classnames)
    print("Number of classes are :",NumberOfClasses)
    


if __name__ == '__main__':
    main()