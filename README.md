🌍 Read this in [English](README.md) | Leia em [Português](README.pt.md)

<p align="center">
      <img src="pipeline-logo.png" alt="logo" width="400">
</p>

# Data Pipeline — Python & SQL (ETL)

## ℹ️ About the project

This project demonstrates the construction of a complete **ETL (Extract, Transform, Load) data pipeline** using **Python and SQL**.

The pipeline extracts raw data from a public CSV dataset, performs data cleaning and transformation, normalizes the data into relational entities, and loads it into a **SQLite database** with a defined schema.

This project focuses on **data engineering fundamentals**, such as:

* Automation
* Data cleaning
* Schema control
* Relational modeling
* SQL-based analysis

---

## 🎯 Project Goals

* Build an automated ETL pipeline
* Apply data cleaning and transformation techniques
* Normalize data into relational tables
* Store structured data in a SQL database
* Validate and analyze data using SQL queries

---

## 🗂️ Project Structure

```
pipeline_data/
│
├─ data/
│   └─ raw_data.csv
│
├─ database/
│   ├─ pipeline.db
│   └─ schema.sql
│
├─ sql/
│   ├─ validation.sql
│   ├─ exploratory.sql
│   ├─ metrics.sql
│   └─ joins.sql
│
└─ src/
    ├─ extract.py
    ├─ transform.py
    ├─ load.py
    └─ main.py
```

---

## ⚙️ Pipeline Flow

1. **Extract**

   * Reads raw data from a CSV file using Pandas

2. **Transform**

   * Removes null values and duplicates
   * Standardizes text fields
   * Converts numeric and percentage fields
   * Splits data into normalized entities (`products` and `reviews`)

3. **Load**

   * Creates database schema automatically
   * Loads data into SQLite tables
   * Enforces primary keys and relationships

---

## 🧠 Database Schema

The data is normalized into two tables:

### 🟦 Products

* product_id (PK)
* product_name
* category
* discounted_price
* actual_price
* discount_percentage
* rating
* rating_count
* about_product
* img_link
* product_link

### 🟨 Reviews

* review_id (PK)
* product_id (FK)
* user_id
* user_name
* review_title
* review_content

---

## 📊 SQL Analysis

The `sql/` folder contains queries used for:

* Data validation
* Exploratory analysis
* Business metrics
* Table joins and aggregations

Example:

```sql
SELECT
    category,
    ROUND(AVG(rating), 2) AS avg_rating
FROM products
GROUP BY category
ORDER BY avg_rating DESC;
```

---

## 🚀 How to run the project

### Prerequisites

* <a href="https://www.python.org/downloads/">
  <img alt="Python" height="40" align="left"
  src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/python/python-original.svg" />
  Python (version 3.10+)

</a>

---

### ⚙️ Running on Windows

1. Open **CMD** or **PowerShell**
2. Navigate to the project folder:

   ```bash
   cd path\to\pipeline_data
   ```
3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```
4. Run the pipeline:

   ```bash
   py src/main.py
   ```

---

### ⚙️ Running on Linux / Mac

```bash
python3 src/main.py
```

---

## 🛠️ Technologies Used

* Python
* Pandas
* SQLite
* SQL
* Git

---

## 🛠️ Developed by

**👤 Lucas Monteiro**

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge\&logo=linkedin\&logoColor=white)](https://www.linkedin.com/in/lucas-henrique-monteiro-55101a365/)
[![Gmail](https://img.shields.io/badge/Gmail-D14836?style=for-the-badge\&logo=gmail\&logoColor=white)](mailto:lhmonteiro.ti@gmail.com)
[![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge\&logo=github\&logoColor=white)](https://github.com/lhmontech)
