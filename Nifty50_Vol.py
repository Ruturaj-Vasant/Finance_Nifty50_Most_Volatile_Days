
import os
print("files:", os.listdir())

import pandas as pd
df = pd.read_csv("NIFTY50_Historical_PR_01021990to27022025.csv")

print(df.head())
