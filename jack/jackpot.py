import pandas as pd

URL = "https://www.euro-jackpot.net/statistics/number-frequency"

tables = pd.read_html(URL)
print(tables)
