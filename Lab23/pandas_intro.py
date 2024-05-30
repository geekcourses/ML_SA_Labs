import pandas as pd
import numpy as np


df_users = pd.DataFrame(
    {
        "name":['Maria', 'Petyr', 'Ivan'],
        "age":[23, 21, 34],
        "gender":['female', 'male', 'male']
    }
)

print(df_users)