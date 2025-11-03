# Datasets Information

This document provides detailed information about all datasets used in the PyCaret assignment notebooks.

## 📊 Dataset Overview

| # | Task | Dataset Name | Source | Size | Features | Target |
|---|------|--------------|--------|------|----------|--------|
| 1 | Binary Classification | Heart Disease | Kaggle | 303 rows | 13 | heart_disease |
| 2 | Multiclass Classification | Wine Quality | UCI | 1,599 rows | 11 | quality |
| 3 | Regression | California Housing | Sklearn | 20,640 rows | 8 | median_house_value |
| 4 | Clustering | Mall Customers | Kaggle | 200 rows | 4 | N/A |
| 5 | Anomaly Detection | Credit Card Fraud | Kaggle | 284,807 rows | 30 | Class |
| 6 | Association Rules | Online Retail | UCI | 541,909 rows | 8 | N/A |
| 7 | Time Series (Univariate) | Airline Passengers | Kaggle | 144 rows | 1 | Passengers |
| 8 | Time Series (Exogenous) | Store Sales | Kaggle | 3,000+ rows | 6 | sales |

---

## 1️⃣ Binary Classification - Heart Disease Dataset

### Description
This dataset contains medical information about patients and whether they have heart disease. It's perfect for binary classification tasks.

### Source
- **Kaggle:** https://www.kaggle.com/datasets/johnsmith88/heart-disease-dataset
- **UCI ML Repository:** https://archive.ics.uci.edu/ml/datasets/heart+disease

### Features (13)
1. `age` - Age in years
2. `sex` - Sex (1 = male; 0 = female)
3. `cp` - Chest pain type (0-3)
4. `trestbps` - Resting blood pressure (mm Hg)
5. `chol` - Serum cholesterol (mg/dl)
6. `fbs` - Fasting blood sugar > 120 mg/dl (1 = true; 0 = false)
7. `restecg` - Resting electrocardiographic results (0-2)
8. `thalach` - Maximum heart rate achieved
9. `exang` - Exercise induced angina (1 = yes; 0 = no)
10. `oldpeak` - ST depression induced by exercise
11. `slope` - Slope of peak exercise ST segment
12. `ca` - Number of major vessels colored by fluoroscopy (0-3)
13. `thal` - Thalassemia (1-3)

### Target
- `target` - Heart disease (1 = disease, 0 = no disease)

### Download Command
```python
import pandas as pd
url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/heart-disease/processed.cleveland.data'
df = pd.read_csv(url, header=None)
```

---

## 2️⃣ Multiclass Classification - Wine Quality Dataset

### Description
This dataset contains physicochemical properties of red wine and quality ratings. Perfect for multiclass classification.

### Source
- **UCI ML Repository:** https://archive.ics.uci.edu/ml/datasets/wine+quality
- **Kaggle:** https://www.kaggle.com/datasets/uciml/red-wine-quality-cortez-et-al-2009

### Features (11)
1. `fixed acidity` - Tartaric acid (g/dm³)
2. `volatile acidity` - Acetic acid (g/dm³)
3. `citric acid` - Citric acid (g/dm³)
4. `residual sugar` - Residual sugar (g/dm³)
5. `chlorides` - Sodium chloride (g/dm³)
6. `free sulfur dioxide` - Free SO2 (mg/dm³)
7. `total sulfur dioxide` - Total SO2 (mg/dm³)
8. `density` - Density (g/cm³)
9. `pH` - pH value
10. `sulphates` - Potassium sulphate (g/dm³)
11. `alcohol` - Alcohol percentage

### Target
- `quality` - Quality score (3-8, can be grouped into Low/Medium/High)

### Download Command
```python
url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv'
df = pd.read_csv(url, sep=';')
```

---

## 3️⃣ Regression - California Housing Dataset

### Description
This dataset contains information about housing in California districts. Perfect for regression tasks.

### Source
- **Scikit-learn:** Built-in dataset
- **Kaggle:** https://www.kaggle.com/datasets/camnugent/california-housing-prices

### Features (8)
1. `MedInc` - Median income in block group
2. `HouseAge` - Median house age in block group
3. `AveRooms` - Average number of rooms per household
4. `AveBedrms` - Average number of bedrooms per household
5. `Population` - Block group population
6. `AveOccup` - Average number of household members
7. `Latitude` - Block group latitude
8. `Longitude` - Block group longitude

### Target
- `MedHouseVal` - Median house value (in $100,000s)

### Download Command
```python
from sklearn.datasets import fetch_california_housing
housing = fetch_california_housing(as_frame=True)
df = housing.frame
```

---

## 4️⃣ Clustering - Mall Customers Dataset

### Description
This dataset contains information about mall customers including demographics and spending behavior. Perfect for customer segmentation.

### Source
- **Kaggle:** https://www.kaggle.com/datasets/vjchoudhary7/customer-segmentation-tutorial-in-python

### Features (4)
1. `CustomerID` - Unique customer identifier
2. `Gender` - Customer gender
3. `Age` - Customer age
4. `Annual Income (k$)` - Annual income in thousands
5. `Spending Score (1-100)` - Spending score assigned by mall

### Target
- None (Unsupervised learning)

### Download Command
```python
url = 'https://raw.githubusercontent.com/SteffiPeTaffy/machineLearningAZ/master/Machine%20Learning%20A-Z%20Template%20Folder/Part%204%20-%20Clustering/Section%2025%20-%20Hierarchical%20Clustering/Mall_Customers.csv'
df = pd.read_csv(url)
```

---

## 5️⃣ Anomaly Detection - Credit Card Fraud Dataset

### Description
This dataset contains credit card transactions, including fraudulent ones. Highly imbalanced dataset perfect for anomaly detection.

### Source
- **Kaggle:** https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud

### Features (30)
- `Time` - Seconds elapsed between transactions
- `V1-V28` - PCA transformed features (anonymized)
- `Amount` - Transaction amount

### Target
- `Class` - Fraud indicator (1 = fraud, 0 = legitimate)

### Statistics
- Total transactions: 284,807
- Fraudulent: 492 (0.172%)
- Legitimate: 284,315 (99.828%)

### Download Command
```python
# Requires Kaggle API setup
!kaggle datasets download -d mlg-ulb/creditcardfraud
```

---

## 6️⃣ Association Rules - Online Retail Dataset

### Description
This dataset contains all transactions for a UK-based online retail company. Perfect for market basket analysis.

### Source
- **UCI ML Repository:** https://archive.ics.uci.edu/ml/datasets/online+retail
- **Kaggle:** https://www.kaggle.com/datasets/vijayuv/onlineretail

### Features (8)
1. `InvoiceNo` - Invoice number
2. `StockCode` - Product code
3. `Description` - Product name
4. `Quantity` - Quantity purchased
5. `InvoiceDate` - Invoice date and time
6. `UnitPrice` - Product price per unit
7. `CustomerID` - Customer identifier
8. `Country` - Customer country

### Statistics
- Transactions: 541,909
- Unique products: 4,070
- Unique customers: 4,372
- Date range: 2010-2011

### Download Command
```python
url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/00352/Online%20Retail.xlsx'
df = pd.read_excel(url)
```

---

## 7️⃣ Time Series (Univariate) - Airline Passengers Dataset

### Description
Classic time series dataset showing monthly airline passenger numbers from 1949-1960. Shows clear trend and seasonality.

### Source
- **Kaggle:** https://www.kaggle.com/datasets/rakannimer/air-passengers
- **Seaborn:** Built-in dataset

### Features (1)
- `Month` - Date (monthly)

### Target
- `Passengers` - Number of passengers (in thousands)

### Statistics
- Time period: 1949-1960
- Frequency: Monthly
- Observations: 144
- Trend: Upward
- Seasonality: Strong yearly pattern

### Download Command
```python
import seaborn as sns
df = sns.load_dataset('flights')
```

---

## 8️⃣ Time Series (Exogenous) - Store Sales Dataset

### Description
Time series data for store sales with additional features like promotions, holidays, etc.

### Source
- **Kaggle:** https://www.kaggle.com/c/store-sales-time-series-forecasting

### Features (6+)
1. `date` - Date of sale
2. `store_nbr` - Store identifier
3. `family` - Product family
4. `sales` - Total sales
5. `onpromotion` - Number of items on promotion
6. `oil_price` - Daily oil price (exogenous)
7. `holiday` - Holiday indicator (exogenous)

### Target
- `sales` - Daily sales amount

### Download Command
```python
# Requires Kaggle API
!kaggle competitions download -c store-sales-time-series-forecasting
```

---

## 📥 General Download Instructions

### Method 1: Direct URL (Recommended)
Most datasets can be loaded directly from URLs as shown in the download commands above.

### Method 2: Kaggle API
For Kaggle datasets:

1. Install Kaggle API:
```bash
pip install kaggle
```

2. Get API credentials:
   - Go to Kaggle.com → Account → Create New API Token
   - Download `kaggle.json`
   - Place in `~/.kaggle/` (Linux/Mac) or `C:\Users\<user>\.kaggle\` (Windows)

3. Download dataset:
```bash
kaggle datasets download -d <dataset-path>
```

### Method 3: Manual Download
1. Visit the source URL
2. Download the dataset
3. Place in `data/` folder
4. Update file path in notebook

---

## 🔍 Data Quality Notes

### Preprocessing Required
- **Heart Disease:** Minimal, mostly clean
- **Wine Quality:** Clean, may need quality grouping
- **California Housing:** Clean, built-in dataset
- **Mall Customers:** Clean, small dataset
- **Credit Card Fraud:** Highly imbalanced, PCA features
- **Online Retail:** Needs transaction formatting, missing values
- **Airline Passengers:** Clean, classic dataset
- **Store Sales:** Multiple files, needs merging

### Missing Values
- Most datasets have minimal missing values
- PyCaret handles missing values automatically in setup
- Association rules dataset may need manual cleaning

---

## 📊 Dataset Licenses

All datasets used are publicly available for educational purposes:
- UCI ML Repository: Free for research and education
- Kaggle: Check individual dataset licenses
- Scikit-learn: BSD license

---

## 🔄 Alternative Datasets

If any dataset is unavailable, here are alternatives:

### Binary Classification
- Titanic Survival
- Diabetes Prediction
- Bank Marketing

### Multiclass Classification
- Iris Species
- MNIST Digits
- Fashion MNIST

### Regression
- Boston Housing (deprecated but available)
- Bike Sharing Demand
- Insurance Cost

### Clustering
- Iris (for clustering)
- Wholesale Customers
- Seeds Dataset

### Anomaly Detection
- Network Intrusion Detection
- Sensor Data Anomalies

### Association Rules
- Groceries Dataset
- Instacart Market Basket

### Time Series
- Stock Prices
- Weather Data
- Energy Consumption

---

**Last Updated:** November 2024
