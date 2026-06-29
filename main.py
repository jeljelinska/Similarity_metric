import numpy as np
import pandas as pd
from similarity import SimilarityMetric
file_path = "data.xlsx"

df_long = pd.read_excel(file_path)

metric = SimilarityMetric()

df_ap = df_long.pivot_table(
    index=["Patient_ID", "Point"],
    columns="Method",
    values="A-P_Component",
    aggfunc="mean"
).reset_index()

A_cbct_molar_ap = metric.calculate(
    df_ap["CBCT"],
    df_ap["MOLAR"]
)

print("CBCT vs MOLAR, A-P:", A_cbct_molar_ap)
