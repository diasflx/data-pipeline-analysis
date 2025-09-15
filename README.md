
# Data Pipeline & Analysis (10k+ rows)

End-to-end data pipeline that:
- Generates synthetic operations dataset (10,000+ rows)
- Cleans data (missing values)
- Computes KPIs
- Produces charts and a summary report

## Quickstart (macOS)
```bash
cd 03_data_pipeline_analysis
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python generate_data.py
python analysis.py
open out/summary.txt
```
