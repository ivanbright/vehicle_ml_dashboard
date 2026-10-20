from pathlib import Path

import pandas as pd
from django.conf import settings
from django.shortcuts import render

from .dashboard import frequency_table

CSV_PATH = Path(settings.BASE_DIR) / "vehicles" / "dummy_data" / "vehicles_ml_dataset.csv"


def dashboard_view(request):

    queryset = pd.read_csv(CSV_PATH)

    df = pd.DataFrame(queryset)

    return render(request, "vehicles/index.html", {

        "frequency_table": frequency_table(df)
    })


