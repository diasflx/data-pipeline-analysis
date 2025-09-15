
import numpy as np
import pandas as pd

rng = np.random.default_rng(42)
N = 12000

regions = ["Americas", "EMEA", "APAC"]
products = ["Alpha","Beta","Gamma","Delta"]

df = pd.DataFrame({
    "order_id": np.arange(1, N+1),
    "region": rng.choice(regions, size=N, p=[0.4,0.35,0.25]),
    "product": rng.choice(products, size=N),
    "units": rng.integers(1, 50, size=N),
    "unit_price": rng.normal(50, 10, size=N).clip(5, 200),
    "discount": rng.choice([0,0.05,0.1,0.15], size=N, p=[0.6,0.2,0.15,0.05]),
})
mask = rng.random(N) < 0.01
df.loc[mask, "unit_price"] = np.nan

df.to_csv("operations_data.csv", index=False)
print("Generated operations_data.csv")
