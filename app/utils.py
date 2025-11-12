from pathlib import Path
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# --- Paths to your cleaned CSVs ---
DATA_DIR = Path(__file__).parent.parent / "data"  # assumes utils.py is in app/

FILE_MAP = {
    "Benin": DATA_DIR / "benin-malanville_clean.csv",
    "Sierra Leone": DATA_DIR / "sierraleone-bumbuna_clean.csv",
    "Togo": DATA_DIR / "togo-dapaong_qc_clean.csv"
}

# --- Load cleaned CSV by country ---
def load_country_data(country_name: str) -> pd.DataFrame:
    file_path = FILE_MAP[country_name]
    if not file_path.exists():
        raise FileNotFoundError(f"{file_path} does not exist")
    df = pd.read_csv(file_path, parse_dates=['Timestamp'])
    df['Country'] = country_name
    return df

# --- Combine multiple countries ---
def combine_countries(selected_countries):
    dfs = [load_country_data(c) for c in selected_countries]
    combined_df = pd.concat(dfs, ignore_index=True)
    return combined_df

# --- Plot boxplot for selected metric ---
def plot_boxplot(df, metric):
    fig, ax = plt.subplots(figsize=(8,5))
    sns.boxplot(x='Country', y=metric, data=df, ax=ax, palette=['orange','green','blue'])
    ax.set_title(f"{metric} Distribution by Country")
    ax.set_ylabel(f"{metric} (W/m²)")
    ax.set_xlabel("Country")
    return fig
