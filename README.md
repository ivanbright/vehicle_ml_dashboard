# Vehicle ML Dashboard

A small Django app that loads a vehicle dataset with pandas and shows it on a clean Bootstrap dashboard. Right now it displays a one-way frequency table of manufacturers, with a spot reserved for ML predictions later.

## Getting started

```bash
python -m venv venv
venv\Scripts\activate        # Windows — use `source venv/bin/activate` on macOS/Linux
pip install -r requirements.txt
python manage.py runserver
```

Then open http://127.0.0.1:8000/ in your browser.

## How it works

- `vehicles/dummy_data/vehicles_ml_dataset.csv` — the dataset (10,000 rows)
- `vehicles/views.py` — reads the CSV and passes it to the template
- `vehicles/dashboard.py` — builds the frequency table
- `vehicles/templates/vehicles/index.html` — the dashboard UI (light/dark theme included)

Made for learning and tinkering — contributions and wild ideas welcome.
