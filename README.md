# Brain-ML
Research project on brain inspired architectures for multi-modal unsupervised learning


## Getting Started

Run the generate_dataset.py file to generate training and test images and captions.


Run the Text_labelling.ipynb notebook.

You should get the following output after model training and clustering : 
![alt text](https://github.com/AntoineTelecom/Brain-ML/blob/master/Architecture.PNG)


### Model Architecture

This is an overview of the model: 

![alt text](https://github.com/AntoineTelecom/Brain-ML/blob/master/BCPNN_clusters.png)

It uses Word2Vec and Resnet-18 as feature extractors which are then encoded using an overcomplete autoencoder and fed to a Bayesian Confidence Propagation Neural Network (BCPNN). This model uses associative learning (also called hebbian learning) instead of backpropagation to train a model in a more biologically plausible manner.


## Authors

* **Antoine Sueur**
* **Piere Marza**

