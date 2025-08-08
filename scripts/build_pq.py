# Quick and dirty script to generate sample parquet files for testing

input_file = (
    "./src/20250708_195725_00092_d7hpj_7eaa1c40-cf87-41cf-aacf-2634826ef725.parquet"
)

import numpy as np
import pandas as pd

df = pd.read_parquet(input_file)

new_df = df.iloc[:5].copy()

new_values = 12345678901230 + np.arange(len(new_df))
new_df["cnpj_num"] = new_df["cnpj_num"].astype(str)
new_df["cnpj_num"] = new_values

new_df.to_parquet("str_document_data.parquet", index=False)
