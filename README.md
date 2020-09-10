# cat_breed_detector

## Problem Statement

*Does anybody know what breed their cat is?*

On a recent walk I came across a group of dogs that were out for a stroll with their owners. I overhead the owners talking about their dog's breed from afar. This piqued my interest. I live with 3 cats at home, when I just adopted them I had no clue what kind of cats they are. So I asked a few of my friends with cats, they could only tell me the color and the length of their fur but not their breed. So I decided to make an application that can identifies cat breeds. 

## Dataset

For this project I have 832 pictures in total. Most of the images are collected from [Kaggle's Cat Breeds Dataset](https://www.kaggle.com/ma7555/cat-breeds-dataset)

| Cat Breed | Data Type | Value Counts |
| --- | --- | --- |
| Tabby (orange tabby) | Image | 28.9% |
| Siamese | Image | 27.2% |
| Bombay | Image | 43.9%|


## Use PCA to Reconstruct Images

I used PCA to reduce the total number of pixel values and recontruct the images with the newly created principal components. 

![ezgif com-gif-maker](https://user-images.githubusercontent.com/39779186/91904108-342f9700-ec59-11ea-9e81-c94da07958bf.gif)

## Modeling 

For this project I tested out Support Vector Machine and Convolutional Neural Netowrk both with and without using PCA to reduce features. The best model is the Convolutional Neural Network. I got 91.4% validation accuracy and 0.39% of validation loss. 


## Breed Detection in Action
 I took the best model and used openCV library to detect cats from my own webcam. Here are some screen grabs of the process in action. You can see that the model still has some trouble identifying Bombay. This is because of the fur color of the Bombay which gives a challenge for the model to identify outside of Siamese. To overcome this I have added even more Bombay photos to the dataset, however it still has its limitations.
 ![Screen Shot 2020-09-10 at 12 23 06 PM](https://user-images.githubusercontent.com/39779186/92790503-ae9a9e00-f360-11ea-9ea3-c25ca3c55b4c.png)

## References

1. Cat Breeds Dataset: https://www.kaggle.com/ma7555/cat-breeds-dataset
2. PCA using Python(scikit-learn): https://towardsdatascience.com/pca-using-python-scikit-learn-e653f8989e60
3. Python OpenCV: Capture Video from Camera: https://www.geeksforgeeks.org/python-opencv-capture-video-from-camera/