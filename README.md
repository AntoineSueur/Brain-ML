# Brain-ML
Research project on brain inspired architectures for multi-modal unsupervised learning


## Getting Started

To run the script and  generate training and test images and captions.

``` python generate_dataset.py
```


Run the Text_labelling.ipynb notebook.

You should get the following output after model training and clustering : 
![alt text](https://github.com/AntoineTelecom/Brain-ML/blob/master/BCPNN_clusters.png)


### Model Architecture

This is an overview of the model: 

![alt text](https://github.com/AntoineTelecom/Brain-ML/blob/master/Architecture.PNG)

It uses Word2Vec and Resnet-18 as feature extractors which are then encoded using an overcomplete autoencoder and fed to a Bayesian Confidence Propagation Neural Network (BCPNN). This model uses associative learning (also called hebbian learning) instead of backpropagation to train a model in a more biologically plausible manner. 
The end goal for the model is to learn a multimodal representation of thedata divided into a defined number of concepts (using for instance K-means centroids). We also want the model to acquire some form of robustness to the absence of one of the modalities, for instance removing the image or the associated text.


## Authors

* **Antoine Sueur**
* **Piere Marza**

