# 🛡️ Credit Card Fraud Detection

This repository contains a project focused on detecting fraudulent transactions in credit card data. By leveraging a combination of exploratory data analysis, dimensionality reduction techniques, machine learning models, and a custom AutoEncoder architecture, this project aims to effectively distinguish between legitimate and fraudulent transactions.

---

## 📄 Introduction

Credit card fraud is a growing concern in today's digital economy. This project is designed to address this issue by analyzing transaction data to identify patterns of fraudulent activity. The work involves cleaning and preprocessing data, exploring features, and applying both traditional machine learning and neural network-based approaches to create a robust fraud detection system.

---

## 📊 Dataset Description

The dataset used in this project consists of anonymized credit card transaction records, with the following key attributes:
- **Features:** 29 anonymized numerical features (likely principal components).
- **Class Label:** Binary target variable indicating whether the transaction is fraudulent (1) or normal (0).

The dataset was preprocessed to remove noise and outliers and prepared for modeling.

---

## 🔎 Analysis Performed

1. **Data Cleaning and Outlier Detection:** 
   - Processed raw data to remove inconsistencies and extreme outliers.

2. **Exploratory Data Analysis (EDA):**
   - Analyzed class distributions, feature correlations, and visualized patterns using various charts.

3. **Dimensionality Reduction:**
   - Applied **Principal Component Analysis (PCA)** and **Linear Discriminant Analysis (LDA)** to explore and reduce feature space while preserving variance.

---

## 🧠 Models Used

The following models were trained and evaluated for fraud detection:
1. **Logistic Regression**
2. **Decision Tree**
3. **Random Forest**
4. **Gradient Boosting**
5. **Bernoulli Naive Bayes**
6. **AutoEncoder (TensorFlow):**
   - Developed a neural network-based anomaly detection system using reconstruction loss to identify fraud.

---

## 📈 Model Performance

The models were evaluated using **Precision**, **Recall**, and **F1 Score** to ensure balanced performance. Below is a summary of the results:

| Model                    | Precision | Recall | F1 Score |
|--------------------------|-----------|--------|----------|
| Logistic Regression      | 0.88      | 0.86   | 0.87     |
| Decision Tree            | 0.90      | 0.88   | 0.89     |
| Random Forest            | 0.90      | 0.88   | 0.89     |
| Gradient Boosting        | 0.95      | 0.88   | 0.91     |
| Bernoulli Naive Bayes    | 0.92      | 0.83   | 0.87     |
| AutoEncoder (Reconstruction Loss) | 0.99 | 0.84   | 0.91     |

---

## 🔮 Future Planning

- **Hyperparameter Tuning with Optuna:** 
  Plan to use **Optuna**, a powerful optimization library, to fine-tune model parameters and enhance performance.
  
- **Handling Class Imbalance:** 
  Implement **SMOTE (Synthetic Minority Oversampling Technique)** to balance the dataset, improving model training on minority (fraudulent) classes.
  
- **Deep Learning Extensions:**
  Explore additional architectures like convolutional or recurrent neural networks to enhance fraud detection capabilities.

---

## 🤝 Contribution

Contributions are welcome! If you have suggestions for improving this project or new techniques to implement, feel free to create a pull request or open an issue. 🌟


