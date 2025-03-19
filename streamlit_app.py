import os
import urllib

import pandas as pd
from sqlalchemy import create_engine
import streamlit as st

# CONNECT TO DATABASE
connection_string = (
    f'{"mssql"}+{"pyodbc"}:///?odbc_connect=' +
    urllib.parse.quote_plus(
        f'DRIVER={os.environ["ODBC_DRIVER"]};' +
        f'SERVER={os.environ["ODBC_SERVER"]};' +
        f'DATABASE={os.environ["ODBC_DATABASE"]};' +
        f'UID={os.environ["AZURE_CLIENT_ID"]};' +
        f'PWD={os.environ["AZURE_CLIENT_SECRET"]};' +
        f'AUTHENTICATION={os.environ["ODBC_AUTHENTICATION"]};'
    )
)

# Create SQLAlchemy engine
conn = create_engine(
    connection_string,
)

df = pd.read_sql_query(
    sql="""
        select top 10 *
        from core.person
    """,
    con=conn,
)

st.write(df)
