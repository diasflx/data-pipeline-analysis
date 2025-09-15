An end-to-end Python data pipeline that generates a synthetic dataset (12,000+ rows), cleans it, computes KPIs, and produces both charts and a summary report.

## Demo (local)
```bash
git clone git@github.com:diasflx/data-pipeline-analysis.git
cd data-pipeline-analysis
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

# generate dataset
python generate_data.py

# run analysis
python analysis.py

# open results (macOS)
open out/summary.txt
open out/rev_by_region.png

Features:

* Synthetic dataset generator
Generates operations_data.csv with 12,000+ rows (region, product, units, pricing, discounts).

* Data cleaning
Handles missing values by filling with median unit price.

* KPI calculations
Computes total orders, total units, total revenue, and average order value.

* Aggregations
Groups revenue by region and product for business insights.

* Visualizations
Produces bar charts using matplotlib (rev_by_region.png, rev_by_product.png).

* Reporting
Writes results to out/summary.txt and saves charts in out/.


Project Structure

data-pipeline-analysis/
├─ generate_data.py
├─ analysis.py
├─ requirements.txt
├─ README.md
└─ out/
   ├─ summary.txt
   ├─ rev_by_region.png
   └─ rev_by_product.png
