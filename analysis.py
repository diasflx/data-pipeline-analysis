
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

OUT = Path("out")
OUT.mkdir(exist_ok=True)

df = pd.read_csv("operations_data.csv")
df["unit_price"] = df["unit_price"].fillna(df["unit_price"].median())
df["revenue"] = df["units"] * df["unit_price"] * (1 - df["discount"])

kpis = {
    "total_orders": int(len(df)),
    "total_units": int(df["units"].sum()),
    "total_revenue": float(df["revenue"].sum()),
    "avg_order_value": float(df["revenue"].mean()),
}

rev_by_region = df.groupby("region")["revenue"].sum().sort_values(ascending=False)
rev_by_product = df.groupby("product")["revenue"].sum().sort_values(ascending=False)

plt.figure()
rev_by_region.plot(kind="bar", title="Revenue by Region")
plt.tight_layout()
plt.savefig(OUT / "rev_by_region.png")
plt.close()

plt.figure()
rev_by_product.plot(kind="bar", title="Revenue by Product")
plt.tight_layout()
plt.savefig(OUT / "rev_by_product.png")
plt.close()

with open(OUT / "summary.txt", "w") as f:
    f.write("DATA PIPELINE SUMMARY\n")
    f.write("====================\n\n")
    for k,v in kpis.items():
        f.write(f"{k}: {v}\n")
    f.write("\nTop regions by revenue:\n")
    f.write(rev_by_region.to_string())
    f.write("\n\nTop products by revenue:\n")
    f.write(rev_by_product.to_string())

print("Wrote out/summary.txt and charts.")
