# POST-OCR Error Correction

This project consists of three main components, each of which contain detailed individual ReadME.md explaining their installation as well as execution environments. This separation has been done keeping in mind tha in real-world deployment, it makes more sense to modularize software responsible for training and actual serving.

* Tensorflow-serving

This is the platform that will be used to deploy the train NMT model. The pre-packaged folder contains the optimally trained NMT model from OpenNMT-tf that can be deployed immediately. Once deployed tf-serving exposes endpoints i,e. Rest API's as well as GRPC endpoints that can be queried for prediction results.

* Serving-layer

This is a flask application that serves as a control layer for the tf-serving instance, with end-points that are capable of updating the configurations running on tf-serving, as well reloading the server, and testing the response times acheived via grpc calls for one request as well as for the complete test set. This application can be running through the terminal or can be loaded on to an IDE for further development and testing.

* Tensorflow-NMT

This is environment set up to train translation models using OpenNMT-tf. The required dataset taken from the outputs as well as the training/evaluation ground truths are present within this repository. Details are expanded within the ReadME file of the repository.

### Running Order

While Serving-layer depends on a running tensorflow-serving instance, they are by themselves sufficient to test the working of the predictions. This is because the tf-serving instance has been set up to serve the model trained from OpenNMT-tf to reduce setup effort. The training can be replicated using the Tensorflow-NMT repository which also provides instruction on evaluation of the accuracy of the trained model.
