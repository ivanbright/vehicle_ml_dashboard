from pathlib import Path

import pandas as pd
from django.conf import settings
from django.shortcuts import render

from .dashboard import frequency_table

CSV_PATH = Path(settings.BASE_DIR) / "vehicles" / "dummy_data" / "vehicles_ml_dataset.csv"

# Load dataset once globally
_df_cache = None

def get_dataframe():
    """Load and cache the dataframe globally"""
    global _df_cache
    if _df_cache is None:
        _df_cache = pd.read_csv(CSV_PATH)
    return _df_cache


def dashboard_view(request):
    df = get_dataframe()
    
    return render(request, "vehicles/index.html", {
        "frequency_table": frequency_table(df)
    })


def price_filter_view(request):
    df = get_dataframe()
    
    price_threshold = request.GET.get('price_threshold', None)
    filtered_df = None
    filtered_html = None
    
    if price_threshold:
        try:
            threshold_value = float(price_threshold)
            filtered_df = df[df['selling_price'] > threshold_value]
            
            # Create frequency table
            manufacturer_counts = filtered_df['manufacturer'].value_counts().reset_index()
            manufacturer_counts.columns = ['Manufacturer', 'Count']

            # Convert to HTML table
            filtered_html = manufacturer_counts.to_html(
                classes="table table-bordered table-striped table-sm",
                float_format='%.2f',
                justify='center'
            )
        except (ValueError, KeyError) as e:
            filtered_html = f'<div class="alert alert-danger">Error: {str(e)}</div>'
    
    return render(request, "vehicles/price_filter.html", {
        "frequency_table": frequency_table(df),
        "filtered_html": filtered_html,
        "price_threshold": price_threshold,
        "filtered_count": len(filtered_df) if filtered_df is not None else 0,
        "total_count": len(df)
    })



def group_view(request):
    df = get_dataframe()
    
    # Group by manufacturer and transmission, sum the selling prices
    grouped = df.groupby(['manufacturer', 'transmission'])['selling_price'].sum()
    
    # Convert to HTML table using to_frame() and to_html()
    grouped_html = grouped.to_frame('Total Selling Price').to_html(
        classes="table table-bordered table-striped table-sm",
        float_format='%.2f',
        justify='center'
    )
    
    return render(request, "vehicles/group_view.html", {
        "grouped_html": grouped_html
    })
