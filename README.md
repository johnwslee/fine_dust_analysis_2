![license
status](https://img.shields.io/github/license/johnwslee/fine_dust_analysis_2)

# Prediction of Air Quality in Seoul Using a 1-D Convolutional Neural Network on Weather Data

**Author:** John W.S. Lee

## 1. Introduction

This project is a sequel to the [previous study](https://github.com/johnwslee/fine_dust_analysis) that examined the correlation between weather parameters and fine dust concentration. The primary aim of the prior investigation was not to anticipate fine dust concentration based on weather parameters, but rather to explore the interplay between fine dust concentration and weather factors.

In this study, the objective is to predict the air quality for the upcoming day using a 24-hour dataset of weather parameters from the given day. Specifically, a total of eight features that demonstrated utility in the earlier study have been employed as inputs for the predictive model. These features encompass `wind_direction`, `humidity(%)`, `lowest_ceiling(100m)`, `temp(°C)`, `wind_speed(m/s)`, `local_P(hPa)`, `precipitation(mm)`, and `PM10_Counts`. The target variable, denoted as `Air_is_bad?`, assumes a binary state and is determined based on the PM10 particle counts for the following day (True for `PM10 counts`` exceeding 45, and False for counts below 45). A detailed outline of the data preprocessing procedure can be found in the [data_preprocessing_notebook](https://github.com/johnwslee/fine_dust_analysis_2/blob/main/notebooks/0_data_preprocessing.ipynb).

## 2. Modelling

Given that the input data for prediction exists in the form of a time series, a 1-D convolutional neural network was employed as the foundational architecture for the model. The 24-hour dataset of the eight input features underwent scaling and conversion into a `NumPy` array. Subsequently, these arrays were stacked to create an input data structure with eight channels (For an in-depth process, refer to the [data_preprocessing_notebook](https://github.com/johnwslee/fine_dust_analysis_2/blob/main/notebooks/0_data_preprocessing.ipynb)). The following figure shows a representative instance of input features, accompanied by the corresponding target value as the title.

<img src="https://github.com/johnwslee/fine_dust_analysis_2/blob/main/img/features_for_DL.png" style="width:800px;height:400px;background-color:white">

The architecture of the models was refined through the implementation of the `optuna` library. The following figures display the classification report, confusion matrix, and ROC curve of the model. The accuracy of the prediction on the test set was 83%. 

<p float="left">
    <img src="https://github.com/johnwslee/fine_dust_analysis_2/blob/main/img/classification.png" style="width:400px;height:300px;background-color:white">
    <img src="https://github.com/johnwslee/fine_dust_analysis_2/blob/main/img/confusion_matrix.png" style="width:400px;height:300px;background-color:white">
</p>
<img src="https://github.com/johnwslee/fine_dust_analysis_2/blob/main/img/roc_curve.png" style="width:500px;height:400px;background-color:white">

Comprehensive procedures for model setup and hyperparameter tuning, as well as model evaluations, are outlined in the [modeling_notebook](https://github.com/johnwslee/fine_dust_analysis_2/blob/main/notebooks/1_1d_CNN_model_training_with_hyper_opt.ipynb) and [evaluation_notebook](https://github.com/johnwslee/fine_dust_analysis_2/blob/main/notebooks/2_1d_CNN_model_evaluation.ipynb) respectively. The subsequent illustration provides a preview of predictions alongside actual labels.

<img src="https://github.com/johnwslee/fine_dust_analysis_2/blob/main/img/prediction_result.png" style="width:800px;height:400px;background-color:white">

## How to Run the Notebooks Locally

To download the contents of this GitHub page on to your local machine, follow these steps:

1. Copy and paste the following link: `git clone https://github.com/johnwslee/fine_dust_analysis_2.git` to your Terminal.

2. On your terminal, type: `cd fine_dust_analysis_2`.

3. Create a virtualenv by typing: `conda env create -f env.yml`

4. Activate the virtualenv by typing: `conda activate finedust_env`

5. Run the notebooks in notebook folder in order.