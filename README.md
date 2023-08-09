![license
status](https://img.shields.io/github/license/johnwslee/fine_dust_analysis_2)

# Prediction of Air Quality in Seoul Using a Multi-Scale Convolutional Neural Network on Weather Data

**Author:** John W.S. Lee

## 1. Introduction

This project is a sequel to the [previous study](https://github.com/johnwslee/fine_dust_analysis) that examined the correlation between weather parameters and fine dust concentration. The primary aim of the prior investigation was not to anticipate fine dust concentration based on weather parameters, but rather to explore the interplay between fine dust concentration and weather factors.

In this study, the objective is to predict the air quality for the upcoming day using a 24-hour dataset of weather parameters from the given day. Specifically, a total of eight features that demonstrated utility in the earlier study have been employed as inputs for the predictive model. These features encompass `wind_direction`, `humidity(%)`, `lowest_ceiling(100m)`, `temp(°C)`, `wind_speed(m/s)`, `local_P(hPa)`, `precipitation(mm)`, and `PM10_Counts`. The target variable, denoted as `Air_is_bad?`, assumes a binary state and is determined based on the PM10 particle counts for the following day (True for `PM10 counts`` exceeding 45, and False for counts below 45). A detailed outline of the data preprocessing procedure can be found in the [data_preprocessing_notebook](https://github.com/johnwslee/fine_dust_analysis_2/blob/main/notebooks/0_data_preprocessing.ipynb).

## 2. Modelling

Since the input data for prediction is in a form of timeseries, 1-D convolutional neural network was used as the base architecture for the model. The 24-hour data of 8 input features were scaled and converted into `numpy` array. Then the arrays were stacked together so that the input data has 8 channels (Detailed procedure is shown in the [data_preprocessing_notebook](https://github.com/johnwslee/fine_dust_analysis_2/blob/main/notebooks/0_data_preprocessing.ipynb)). The following figure shows an example of input features, and the corresponding target value as the title.

<img src="https://github.com/johnwslee/fine_dust_analysis_2/blob/main/img/features_for_DL.png" style="width:800px;height:500px;background-color:white">