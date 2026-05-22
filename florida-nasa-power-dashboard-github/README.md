# Florida NASA POWER Climate Analytics Dashboard

An AI-assisted capstone project that analyzes Florida climate patterns using NASA POWER daily meteorological data from 2015 to present. The project includes exploratory data analysis, a data story, an interactive static dashboard, a final report, a notebook, source code, prompts, and references.

## Live Dashboard

After publishing this repository with GitHub Pages, the dashboard URL will follow this format:

`https://YOUR-GITHUB-USERNAME.github.io/florida-nasa-power-dashboard/`

The interactive dashboard is also available locally as:

- `index.html`
- `dashboard/florida_nasa_power_dynamic_dashboard_2015_to_present.html`

Open either HTML file in a modern browser.

## Important Dashboard Note

The dashboard is static and self-contained. The NASA POWER data were downloaded once and embedded directly into the HTML/JavaScript. Therefore, the dashboard does **not** need to download data at runtime and does **not** need to read the CSV file in order to work. The CSV is included only for documentation, transparency, and reproducibility.

## Project Structure

```text
.
├── index.html
├── README.md
├── GITHUB_PUBLISHING_GUIDE.md
├── LICENSE
├── .gitignore
├── .nojekyll
├── code/
│   ├── download_nasa_power_data.py
│   └── download_nasa_power_data.ipynb
├── dashboard/
│   └── florida_nasa_power_dynamic_dashboard_2015_to_present.html
├── data/
│   ├── florida_nasa_power_daily.csv
│   └── data_dictionary.csv
├── figures/
│   └── EDA figures used in the report
├── notebooks/
│   └── Florida_NASA_POWER_EDA_and_Dashboard_Development.ipynb
├── prompts/
│   ├── Dashboard_Development_Prompts.docx
│   ├── dashboard_development_prompts.txt
│   ├── Reverse_Prompting_and_AI_Use_Appendix.docx
│   └── reverse_prompting_prompts.txt
├── proposal/
│   └── Dataset_Selection_Proposal.docx
├── references/
│   ├── ai_use_credit_statement.md
│   ├── bibliography_apa.md
│   ├── data_sources.md
│   └── reference_folder_readme.md
├── report/
│   ├── Final_Capstone_Report.docx
│   └── Executive_Summary.docx
└── submission_checklist.md
```

## Dashboard Features

- Static standalone HTML dashboard with embedded data
- Daily, monthly, and yearly aggregation controls
- KPI summary cards
- City-level climate comparison
- Temperature and precipitation trend views
- Turbo-color seasonal heatmap
- Geographical map of selected Florida cities with satellite-style basemap
- Interactive filtering and tooltips

## Dataset

The project uses NASA POWER meteorological data for selected Florida cities. The included CSV contains downloaded daily observations and is retained for reproducibility.

Source: NASA POWER Project, Prediction Of Worldwide Energy Resources API, https://power.larc.nasa.gov/

## Variables

The analysis focuses on climate and environmental variables including:

- Temperature
- Precipitation
- Relative humidity
- Solar radiation
- Wind speed
- Date
- City
- Latitude and longitude

## How to Run Locally

1. Download or clone this repository.
2. Open `index.html` in Chrome, Edge, Firefox, or Safari.
3. Use the dashboard controls to explore the data.

No local server is required because the dashboard data are embedded.

## How to Reproduce the Data

The code used to download the NASA POWER data is included in:

- `code/download_nasa_power_data.py`
- `code/download_nasa_power_data.ipynb`

The EDA notebook is included in:

- `notebooks/Florida_NASA_POWER_EDA_and_Dashboard_Development.ipynb`

## Capstone Deliverables Included

- Final report: `report/Final_Capstone_Report.docx`
- Executive summary: `report/Executive_Summary.docx`
- Dashboard: `index.html`
- Dataset: `data/florida_nasa_power_daily.csv`
- Notebook/source files: `notebooks/` and `code/`
- AI prompt appendix: `prompts/`
- References: `references/`
- Dataset proposal: `proposal/`
- Submission checklist: `submission_checklist.md`

## AI Use Disclosure

This project was developed using ChatGPT AI. The user repeatedly provided prompts, feedback, corrections, and revision requests. ChatGPT generated the dashboard code, data download script, notebook structure, report, README content, prompt appendix, and packaging structure. Outputs were revised through user review and iterative prompt-based improvement.

## Suggested Dashboard Link for Submission

After GitHub Pages is enabled, use the GitHub Pages URL as the required dashboard link:

`https://YOUR-GITHUB-USERNAME.github.io/florida-nasa-power-dashboard/`

If the instructor allows file uploads instead of a hosted URL, submit the repository ZIP and identify `index.html` as the dashboard file.
