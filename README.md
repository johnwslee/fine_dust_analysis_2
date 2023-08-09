![license
status](https://img.shields.io/github/license/johnwslee/fine_dust_analysis_2)

# Prediction of Air Quality in Seoul Using a Multi-Scale Convolutional Neural Network on Weather Data

**Author:** John W.S. Lee

## 1. Introduction

This project is sequel to [this project](https://github.com/johnwslee/fine_dust_analysis) that studied the relationship between weather parameters and fine dust concentration. The purpose of the previous study was not to predict the fine dust concentration based on the weather parameters but to investigate how the fine dust concentration is related to the weather parameters. 

The purpose of this study is to actually predict the air quality of the next day based on the 24 hour data of weather parameters for the given day. More specifically, total of 8 features that were found useful in the previous study were used as the inputs for the prediction model. The features were `wind_direction`, `humidity(%)`, `lowest_ceiling(100m)`, `temp(°C)`, `wind_speed(m/s)`, `local_P(hPa)`, `precipitation(mm)`, and `PM10_Counts`. For the target, `Air_is_bad?`, which is binary, was generated based on `PM10_Counts` of the next day (`True` for `PM10_COUNTS` higher than 45, `False` for lower than 45). Detailed procedure for data preprocessing can be found in the [data_preprocessing_notebook](https://github.com/johnwslee/fine_dust_analysis_2/blob/main/notebooks/0_data_preprocessing.ipynb).