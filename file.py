import os


project_root = "fintech_customer_experience_week2"

# Define the directory structure
directories = [
    "data/raw",                # Raw scraped data
    "data/processed",          # Cleaned/processed data
    "notebooks",               # Jupyter notebooks
    "scripts/scraping",        # Web scraping scripts
    "scripts/analysis",        # Sentiment & thematic analysis
    "scripts/database",        # Oracle/Postgres database scripts
    "scripts/visualization",   # Plotting and visualizations
    "reports",                 # Reports (interim & final)
    "assets",                  # Images or plots for reports
    "sql",                     # SQL dumps or schema
    ".github",                 # GitHub workflows or issue templates
]

files = {
    "README.md": "# Customer Experience Analytics for Fintech Apps\n\nThis project analyzes Google Play reviews for Ethiopian banking apps.",
    ".gitignore": "data/\n__pycache__/\n.env\n*.sqlite\n",
    "requirements.txt": "pandas\nmatplotlib\nseaborn\nscikit-learn\nspacy\ntextblob\ntransformers\nvaderSentiment\ngoogle-play-scraper\nsqlalchemy\ncx_Oracle\n",
    "notebooks/EDA.ipynb": "",
    "notebooks/Sentiment_Thematic_Analysis.ipynb": "",
    "notebooks/Visualization.ipynb": "",
}

for directory in directories:
    path = os.path.join(project_root, directory)
    os.makedirs(path, exist_ok=True)

# Create the files
for filename, content in files.items():
    path = os.path.join(project_root, filename)
    with open(path, "w") as f:
        f.write(content)

print(f"Project structure created successfully in '{project_root}'")
