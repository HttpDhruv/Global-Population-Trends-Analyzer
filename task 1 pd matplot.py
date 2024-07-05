import pandas as pd
import matplotlib.pyplot as plt

# CSV file path
csv_file = r'C:\Users\dhrub\Downloads\prodigy ds dataset\TASK 1\API_SP.POP.TOTL_DS2_en_csv_v2_313761.csv'

# Load CSV data into a DataFrame
df_csv = pd.read_csv(csv_file, skiprows=4)

# Ensure 'Country Name' column values are trimmed of leading/trailing spaces
df_csv['Country Name'] = df_csv['Country Name'].str.strip()

# Extract unique country names
unique_countries = df_csv['Country Name'].unique()

# Iterate over each country and plot population trend
for country_name in unique_countries:
    country_data = df_csv[df_csv['Country Name'] == country_name]
    
    if country_data.empty:
        print(f"No data found for {country_name} in the CSV file.")
    else:
        # Extract years and population values
        years = country_data.columns[4:-1]  # Assuming population data starts from column '1960' to '2023'
        population_values = country_data.iloc[0, 4:-1].values.astype(float)

        # Plotting
        plt.figure(figsize=(12, 6))
        plt.plot(years, population_values, marker='o', linestyle='-')
        plt.xlabel('Year')
        plt.ylabel('Population')
        plt.title(f'Population of {country_name} over the years')
        plt.xticks(rotation=45)
        plt.grid(True)
        plt.tight_layout()
        plt.show()
