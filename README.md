Population Trends Visualization for Multiple Countries
This project uses Python to load and visualize population trends over time for various countries based on a CSV dataset. The project leverages pandas for data manipulation and matplotlib for plotting population trends.

Features
Data Loading: The project loads a CSV dataset containing global population data.
Data Cleaning: Ensures that country names are properly formatted by trimming any leading or trailing spaces.
Unique Country Extraction: The script automatically extracts the list of all unique countries available in the dataset.
Population Trend Visualization: For each country, it generates a line plot showing population trends from 1960 to 2023 (or the most recent available year).
Iterative Plotting: The project iterates through all countries in the dataset and displays a population trend for each one in a separate graph.
Prerequisites
Python 3.x
Required libraries:
pandas
matplotlib
