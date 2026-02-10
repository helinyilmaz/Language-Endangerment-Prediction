# Languages at Risk: Predicting Language Endangerment with Machine Learning

## Overview

This project applies machine learning to predict the endangerment status of languages, aiming to identify which languages are at risk and understand the factors influencing language survival. The dataset combines linguistic, socioeconomic, and geographic features from sources like the Endangered Languages Project, Ethnologue, and the World Bank.

---

## Approach

- Conducted data cleaning, preprocessing, and feature engineering on 2,870 languages
- Explored distributions, correlations, and patterns using exploratory data analysis (EDA)
- Built predictive models: Gradient Boosting, Ensemble Voting, Extra Trees, and Neural Networks
- Addressed class imbalance with SMOTE and performed hyperparameter tuning for optimal performance
- Evaluated models using accuracy, confusion matrices, and subgroup analyses

---

## Key Insights

- Speaker count and number of countries a language is spoken in are the strongest predictors of endangerment
- Grouping similar endangerment categories improved model generalization and reduced overfitting
- Models performed best on legally recognized languages, reflecting patterns in language preservation

---

## Results

| Model                     | Test Accuracy |
|---------------------------|---------------|
| Baseline (majority class) | 43%           |
| Gradient Boosting         | 88%           |
| Ensemble Voting           | 88.3%         |
| Neural Network            | 85–87%        |

---

## Technologies

Python, pandas, NumPy, scikit-learn, Keras, Gradient Boosting, Ensemble Methods, Neural Networks, SMOTE, Jupyter Notebooks, Git

---

## Project Notes

- Completed as a collaborative group project for a data science course
- Focused on reproducible ML pipelines, thorough documentation, and evaluating multiple modeling approaches
- Future work could incorporate historical, policy, and longitudinal features to improve predictions beyond current performance

---

Group Members: Jordan Andersen, Courtney Chen, Brian Woods, Helin Yilmaz
