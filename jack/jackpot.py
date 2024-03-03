import random
import pandas as pd
import numpy as np


URL = "https://www.euro-jackpot.net/statistics/number-frequency"

tables = pd.read_html(URL)

# The first table is the one we want
df_main = tables[0]
df_euro = tables[1]

main_base = np.array(
    sorted(
        df_main
        .sort_values(by=('Frequency', 'Frequency'), ascending=False)
        .head(5)['Number']['Number'].tolist()))
euro_base = np.array(
    sorted(
        df_euro
        .sort_values(by=('Frequency', 'Frequency'), ascending=False)
        .head(2)['Number']['Number'].tolist()))

# Output
main_nums = np.array(random.sample(range(1, 51), 5))
euro_nums = np.array(random.sample(range(1, 13), 2))
main_distance = np.linalg.norm(main_base - main_nums)
euro_distance = np.linalg.norm(euro_base - euro_nums)
for i in range(100):
    tmp_main = np.array(random.sample(range(1, 51), 5))
    if np.linalg.norm(main_base - tmp_main) < main_distance:
        main_distance = np.linalg.norm(main_base - tmp_main)
        main_nums = tmp_main

    tmp_euro = np.array(random.sample(range(1, 13), 2))
    if np.linalg.norm(euro_base - tmp_euro) < euro_distance:
        euro_distance = np.linalg.norm(euro_base - tmp_euro)
        euro_nums = tmp_euro

print(f"Main numbers: {main_nums}")
print(f"Euro numbers: {euro_nums}")
