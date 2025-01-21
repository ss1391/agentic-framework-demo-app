# Agentic Framework demp app

In this app, the code simply creates a python app that reads a csv file that 3 columns and displays it as html page.

### app.py

from fastapi import FastAPI
import pandas as pd

app = FastAPI()

@app.get("/")
def read_csv():
    df = pd.read_csv('product_price.csv')
    df['date'] = pd.to_datetime(df['date'], unit='s').dt.strftime('%m/%d/%Y')
    return df.to_html(index=False, header=True)


### product_price.csv


| Column Name | Data Type    | Description    |
| :---:   | :---: | :---: |
| product_id | integer   | Identifier for each product   |
| 1 | 100 | 2025-01-21 1:1:1.941332
| 2 | 100 | 2025-01-21 1:1:1.941332
| 3 | 100 | 2025-01-21 1:1:1.941332
| 1 | 200 | 2025-01-21 2:1:1.941332
| 2 | 200 | 2025-01-21 2:1:1.941332
| 3 | 200 | 2025-01-21 2:2:3.941332
| 1 | 300 | 2025-01-21 3:1:1.941332
| 2 | 300 | 2025-01-21 3:1:1.941332
| 3 | 300 | 2025-01-21 3:2:3.941332

# Problem statement

How can an agentic framework can work with Agents, towards identifying a problem (in this case a run-time python error), searching for answers and actually solving the problem in the code?

## Getting Started

To run this example, you'll need to have FastAPI and Pandas installed in your Python environment. You can install them using pip:

```bash
pip install fastapi pandas
