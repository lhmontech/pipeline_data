🌍 Read this in [English](README.md) | Leia em [Português](README.pt.md)

<p align="center">
      <img src="pipeline-logo.png" alt="logo" width="400">
</p>

# Data Pipeline — Python & SQL (ETL)

## ℹ️ Sobre o projeto

Este projeto demonstra a construção de um pipeline de dados ETL (Extração, Transformação e Carga) utilizando Python e SQL.

O pipeline extrai dados brutos de um arquivo CSV público, realiza limpeza e padronização, normaliza os dados em tabelas relacionais e os carrega em um banco SQLite com schema definido.

O foco do projeto é aplicar conceitos fundamentais de engenharia de dados, como automação, qualidade de dados e modelagem relacional.

---

## 🎯 Objetivos do projeto

* Criar um pipeline ETL automatizado
* Aplicar técnicas de limpeza e transformação de dados
* Normalizar dados em tabelas relacionais
* Armazenar dados estruturados em um banco de dados SQL
* Validar e analisar dados usando consultas SQL

---

## 🗂️ Estrututa do projeto

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

## ⚙️ Fluxo da Pipeline

1. **Extract**

   * Lê os dados brutos de um arquivo CSV usando Pandas

2. **Transform**

   * Remove valores nulos e duplicatas
   * Padroniza campos de texto
   * Converte campos numéricos e de porcentagem
   * Divide os dados em entidades normalizadas (`products` and `reviews`)

3. **Load**

   * Cria o schema do banco de dados automáticamente
   * Carrega dado em tabelas SQLite
   * Impõe chaves primárias e relacionamentos

---

## 🧠 Schema Banco de dados

Os dados são normalizados em duas tabelas:

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

## 📊 Análises SQL

A pasta `sql/` contém consultas para:

* Validação de dado
* Análise exploratória
* Métricas de negócio
* Junções e agregações de tabelas

Exemplo:

```sql
SELECT
    category,
    ROUND(AVG(rating), 2) AS avg_rating
FROM products
GROUP BY category
ORDER BY avg_rating DESC;
```

---

## 🚀 Como rodar o projeto

### Pré-requisitos

* <a href="https://www.python.org/downloads/">
  <img alt="Python" height="40" align="left"
  src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/python/python-original.svg" />
  Python (version 3.10+)

</a>

---

### ⚙️ Rodando no Windows

1. Open **CMD** or **PowerShell**
2. Navegue até a pasta do projeto:

   ```bash
   cd caminho\do\pipeline_data
   ```
3. Instale as dependências:

   ```bash
   pip install -r requirements.txt
   ```
4. Rode a pipeline:

   ```bash
   py src/main.py
   ```

---

### ⚙️ Rodando no Linux / Mac

```bash
python3 src/main.py
```

---

## 🛠️ Tecnologias usadas

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

