# Azure Databricks ADLS ETL Project

This project demonstrates how to load, extract, and transform data using Azure Databricks (PySpark) and store the results in Azure Data Lake Storage (ADLS).

## Architecture

- **Azure Databricks**: For running PySpark notebooks.
- **Azure Data Lake Storage (ADLS Gen2)**: For storing raw and processed data.
- **GitHub**: For version control and collaboration.

## Project Structure

```
azure-databricks-adls-etl/
├── notebooks/
│   ├── 01_load_data.py
│   ├── 02_extract_transform.py
│   └── 03_write_to_adls.py
├── data/
│   └── sample_data.csv
├── README.md
└── requirements.txt
```

## Setup Instructions

1. **Provision Azure Resources**
   - Create an Azure Data Lake Storage Gen2 account and a container.
   - Create an Azure Databricks workspace.
   - Generate credentials (Service Principal or SAS) for Databricks to access ADLS.

2. **Upload Data**
   - Place your raw data (e.g., `sample_data.csv`) in the `data/` folder or upload to Databricks DBFS.

3. **Configure Databricks**
   - Mount ADLS to Databricks or use ABFS paths with credentials.
   - Install required libraries (see `requirements.txt`).

4. **Run Notebooks**
   - Execute the notebooks in order: `01_load_data.py`, `02_extract_transform.py`, `03_write_to_adls.py`.

## How to Run

- Open each notebook in Databricks and run all cells.
- Adjust paths and credentials as needed for your Azure environment.

## Example Data

A sample CSV file is provided in the `data/` folder for testing.

## License

MIT 