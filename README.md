# Airbnb price prediction in Riyadh

## Overview

This project aims to predict Airbnb listing prices in Saudi Arabia, Riyadh using machine learning techniques. By analyzing various factors such as location, property type, amenities, and ratings, the model predicts the nightly rental price for a given Airbnb listing. This can help property owners optimize their pricing strategy and enhance their hosbitality as well as providing insights for potential renters.

## Key Features

* Data Collection and cleaning
   * Data imputation by using mean of a group.
   * Feature engineering(added stayed nights feature, specific location for each airbnb and more).

* Exploratory data analysis (EDA)
   * summary statistics for numerical features.
   * visualized data for better understanding.

* Clustering
   * performed elbow method to get number of airbnb clusters.
   * Kmeans for clustering the airbnbs
   * visualized the result of kmeans in a folium map of Riyadh.

  
* Model building
   * Implemented Decision tree regressors
   * Implemented AdaBoost (Adaptive Boosting) ensemble learning method that combines the decision trees to create a stronger model.

* Results
   * Entire rental unit type is the most profitable airbnb.
   * Most airbnbs were in Riyadh governorator, least in Zilfi and Sulaymaniyah.

* Model evaluation
   * Implemented Decision tree regressors
   * Mean absolute error (MAE) and R-squared (R²) to evaluate model performance 


