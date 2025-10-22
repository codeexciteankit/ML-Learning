# Machine Learning Basics

## What is Machine Learning?
Machine learning is a subset of artificial intelligence that enables systems to learn and improve from experience without being explicitly programmed.

## Types of Machine Learning
1. **Supervised Learning**
   - Classification
   - Regression

2. **Unsupervised Learning**
   - Clustering
   - Dimensionality Reduction

3. **Reinforcement Learning**

## Basic Workflow
```python
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Load and prepare data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Create and train model
model = LinearRegression()
model.fit(X_train, y_train)

# Evaluate
score = model.score(X_test, y_test)