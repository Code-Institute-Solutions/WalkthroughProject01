import numpy as np
import pandas as pd
import os
import base64
from datetime import datetime

def download_dataframe_as_csv(df):

    datetime_now = datetime.now().strftime("%d%b%Y_%Hh%Mmin%Ss")
    csv = df.to_csv().encode()
    b64 = base64.b64encode(csv).decode()
    href = (
        f'<a href="data:file/csv;base64,{b64}" download="Report {datetime_now}.csv" '
        f'target="_blank">Download Report</a>'
    )
    return href


def download_file(bin_file, file_label='File'):

    with open(bin_file, 'rb') as f: data = f.read()
    bin_str = base64.b64encode(data).decode()
    href = (
        f'<a href="data:application/octet-stream;base64,{bin_str}" '
        f'download="{os.path.basename(bin_file)}">Download {file_label}</a>'
    )
    return href