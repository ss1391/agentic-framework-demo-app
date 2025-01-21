from fastapi import FastAPI
import pandas as pd

app = FastAPI()

@app.get("/")
def read_csv():
    df = pd.read_csv('product_price.csv')
    df['date'] = pd.to_datetime(df['date'], unit='s').dt.strftime('%m/%d/%Y')
    return df.to_html(index=False, header=True)
