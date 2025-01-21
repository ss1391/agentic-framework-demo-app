# Agentic Framework demp app

In this app, the code simply creates a python app that reads a csv file that 3 columns and displays it as html page.

### app.py

```
from fastapi import FastAPI
import pandas as pd

app = FastAPI()

@app.get("/")
def read_csv():
    df = pd.read_csv('product_price.csv')
    df['date'] = pd.to_datetime(df['date'], unit='s').dt.strftime('%m/%d/%Y')
    return df.to_html(index=False, header=True)
```

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
```

## Run the code
Start the application by running the following command in your terminal
```
uvicorn app:app --reload
```
This will start a development server that allows you to access your application using a web browser. You should be able to navigate to http://localhost:8000/ in your browser and see the DataFrame displayed on the page.

## Expected 

When opening the server using above link, the app is going to fail to display the page with `Internal Server Error`

Error
```
File "/agentic-framework/agentic-framework-demo-app/app.py", line 9, in read_csv
  df['date'] = pd.to_datetime(df['date'], unit='s').dt.strftime('%m/%d/%Y')
File "/python3.10/site-packages/pandas/core/tools/datetimes.py", line 1067, in to_datetime
  values = convert_listlike(arg._values, format)
File "/python3.10/site-packages/pandas/core/tools/datetimes.py", line 407, in _convert_listlike_datetimes
  return _to_datetime_with_unit(arg, unit, name, utc, errors)
File "/python3.10/site-packages/pandas/core/tools/datetimes.py", line 526, in _to_datetime_with_unit
  arr, tz_parsed = tslib.array_with_unit_to_datetime(arg, unit, errors=errors)
File "tslib.pyx", line 344, in pandas._libs.tslib.array_with_unit_to_datetime
File "tslib.pyx", line 318, in pandas._libs.tslib.array_with_unit_to_datetime
ValueError: non convertible value 2025-01-21 1:1:1.941332 with the unit 's', at position 0
```
