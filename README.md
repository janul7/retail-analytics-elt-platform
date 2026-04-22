# Retail Analytics ELT Platform

A retail analytics data engineering project that ingests raw sales data, orchestrates ELT workflows, and builds analytics-ready marts using Python, Apache Airflow, dbt, and PostgreSQL/DuckDB.

## Project Overview

This project simulates a modern analytics engineering workflow for retail data. It ingests raw transactional datasets, loads them into a warehouse-style environment, applies layered transformations, and publishes reporting-ready marts for downstream analysis.

The goal of this project is to demonstrate practical junior data engineering skills in:
- data ingestion
- ELT pipeline design
- workflow orchestration
- dimensional modeling
- data testing
- analytics-ready warehouse design

## Business Problem

Retail teams often receive raw sales, customer, and product data from multiple operational sources, but that data is rarely ready for analytics as-is.

This project solves that problem by building a structured ELT workflow that:
- ingests raw retail datasets
- standardizes and validates source data
- transforms data into clean staging and business-ready marts
- supports downstream reporting and KPI analysis

## What This Project Demonstrates

- End-to-end ELT workflow design
- Airflow-based orchestration
- dbt modeling with staging, intermediate, and mart layers
- Incremental transformation patterns
- Data quality validation
- Warehouse-style schema design
- Reproducible local development with Docker

## Architecture

Raw Data Sources -> Python Ingestion -> PostgreSQL/DuckDB -> Airflow Orchestration -> dbt Models -> Analytics Marts -> BI / Reporting

## Tech Stack

- Python
- SQL
- Apache Airflow
- dbt
- PostgreSQL / DuckDB
- Docker
- Great Expectations or Soda
- Git / GitHub

## Datasets

- Retail sales dataset: `<dataset-link>`
- Customer dataset: `<dataset-link>`
- Product reference data: `<dataset-link>`

## Key Features

- Automated daily ingestion of raw retail datasets
- Layered transformations using dbt
- Fact and dimension modeling for analytics use cases
- Data quality checks for nulls, uniqueness, and referential integrity
- Reproducible local setup for pipeline development
- Analytics-ready marts for orders, customers, products, and revenue

## Data Model

Example marts included in this project:
- `dim_customers`
- `dim_products`
- `dim_dates`
- `fct_orders`
- `fct_order_items`
- `mart_sales_summary`
- `mart_customer_ltv`

## Repository Structure

```text
retail-analytics-elt-platform/
├── airflow/
│   ├── dags/
│   └── logs/
├── dbt/
│   ├── models/
│   │   ├── staging/
│   │   ├── intermediate/
│   │   └── marts/
│   └── tests/
├── data/
│   ├── raw/
│   └── processed/
├── ingestion/
│   ├── extract/
│   ├── load/
│   └── utils/
├── docs/
├── docker-compose.yml
└── README.md
