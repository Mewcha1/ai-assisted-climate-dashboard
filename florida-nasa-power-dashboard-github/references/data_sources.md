# Data Sources

## Primary Dataset

Dataset name: Florida NASA POWER Daily Climate Dataset, 2015 to present

Source: NASA POWER API, NASA Langley Research Center

Source URL: https://power.larc.nasa.gov/

API documentation: https://power.larc.nasa.gov/docs/services/api/

Geographic scope: Selected Florida metropolitan locations used in the dashboard:
- Miami
- Tampa
- Orlando
- Jacksonville
- Fort Myers / Cape Coral

Variables used in the project include temperature, precipitation, humidity, wind speed, and solar radiation variables returned by NASA POWER.

## Data Preparation Note

The project package includes the downloaded CSV file in the data folder and the Python download script/notebook in the code folder. The dashboard HTML has the final dataset embedded so it can run even if the CSV file is removed from the data folder.
