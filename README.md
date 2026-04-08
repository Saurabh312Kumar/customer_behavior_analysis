# customer_behavior_analysis
Data Analytics Project

##  Customer Shopping Behavior Analysis

## Overview

This project presents an end-to-end data analytics workflow on customer shopping behavior data. It involves data cleaning and transformation using Python, exploratory data analysis (EDA), advanced SQL queries in MySQL, and an interactive Power BI dashboard to generate actionable business insights.

The objective is to understand customer patterns, purchasing behavior, and key drivers of revenue.


##  Dataset
* Dataset: **Customer Shopping Behavior**
* Contains information such as:

  * Customer demographics (age, gender)
  * Purchase details (amount, items, frequency)
  * Discounts and subscription status
  * Product categories and ratings


##  Tools & Technologies

* **Python (Pandas, NumPy)** – Data cleaning and preprocessing, Exploratory Data Analysis (EDA)
* **MySQL** – Data querying and business analysis
* **Power BI** – Interactive dashboard and visualization


##  Project Steps
### 1. Data Loading & Understanding

* Loaded CSV dataset using Pandas
* Explored dataset structure using `.info()`, `.describe()`, and `.head()`

### 2. Data Cleaning & Transformation

* Handled missing values in `review_rating` using median by category 
* Standardized column names (lowercase, underscores) 
* Created new features:

  * `age_group` (customer segmentation) 
  * `purchase_frequency_days` (numerical mapping of frequency) 
* Removed redundant columns (`promo_code_used`) 

### 3. Exploratory Data Analysis (EDA)

* Analyzed:

  * Customer demographics
  * Purchase patterns
  * Product performance
* Identified trends, distributions, and potential outliers

### 4. Data Storage in MySQL

* Created database and table
* Loaded cleaned dataset into MySQL using SQLAlchemy 

### 5. SQL Analysis

Performed business-driven queries such as:

* Revenue by gender
* Top-rated products
* Impact of discounts on spending
* Subscription vs non-subscription revenue
* Customer segmentation (New, Returning, Loyal)
* Top products by category
* Revenue contribution by age group 

### 6. Power BI Dashboard

* Built an interactive dashboard using Power BI
* Key features:

  * KPIs: Total Revenue, Average Purchase, Customer Count
  * Filters: Category, Gender, Subscription Status
  * Visuals: Bar charts, line charts, and segmentation analysis


##  Dashboard
The dashboard provides:

* Clear visualization of customer behavior and sales trends
* Drill-down analysis using filters
* Business insights for decision-making


## Results & Insights

* Identified high-value customer segments
* Found top-performing products and categories
* Analyzed the impact of discounts and subscriptions on revenue
* Observed spending behavior across age groups and genders
* Provided data-driven insights to improve marketing and sales strategies


##  How to Run
### 1. Python Script

```bash
pip install pandas numpy sqlalchemy pymysql 
```

* Run the Python script:

```bash
python customer_shopping_behavior.py
```

### 2. MySQL

* Execute SQL script:

```sql
source customer_shopping_behavior.sql;
```

### 3. Power BI

* Open `Customer_Behavior.pbix` file
* Refresh data connection if required


## Conclusion

This project demonstrates practical, industry-relevant skills in:

* Data cleaning and feature engineering
* SQL-based business analysis
* Data visualization and storytelling

It showcases the ability to transform raw data into meaningful insights and present them effectively using modern data tools.


##  Author
**Saurabh Kumar**
Aspiring Data Analyst
