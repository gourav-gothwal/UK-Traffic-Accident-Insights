import pandas as pd

accidents_path = 'D:/urban mobility/data/raw/Accident_Information.csv'
vehicles_path = 'D:/urban mobility/data/raw/Vehicle_Information.csv'
output_folder = 'D:/urban mobility/data/processed/'

accident_cols = [
    'Accident_Index', 'Accident_Severity', 'Date', 'Time', 'Latitude', 'Longitude',
    'Road_Type', 'Speed_limit', 'Light_Conditions', 'Weather_Conditions',
    'Road_Surface_Conditions', 'Urban_or_Rural_Area'
]
vehicle_cols = [
    'Accident_Index', 'Vehicle_Type', 'Was_Vehicle_Left_Hand_Drive',
    'Sex_of_Driver', 'Age_Band_of_Driver', 'Engine_Capacity_.CC.', 'make',
    'Journey_Purpose_of_Driver'
]

print("Loading datasets...")
accidents_df = pd.read_csv(accidents_path, usecols=accident_cols, low_memory=False)
vehicles_df = pd.read_csv(vehicles_path, usecols=vehicle_cols, low_memory=False, encoding='latin1')
print("Datasets loaded.")

print("Merging dataframes...")
df = pd.merge(
    accidents_df,
    vehicles_df,
    on='Accident_Index',
    how='left'
)
print(f"Checkpoint 1: Shape after merge: {df.shape}")

df.dropna(subset=['Vehicle_Type'], inplace=True)
print(f"Checkpoint 1.5: Shape after ensuring vehicle data exists: {df.shape}")

df.dropna(subset=['Latitude', 'Longitude'], inplace=True)
print(f"Checkpoint 2: Shape after dropping rows with no location: {df.shape}")

df['Date'] = pd.to_datetime(df['Date'], format='%Y-%m-%d', errors='coerce')

df.dropna(subset=['Date'], inplace=True)
print(f"Checkpoint 3: Shape after handling dates: {df.shape}")

df['Year'] = df['Date'].dt.year
latest_year = int(df['Year'].max())
print(f"Discovered the latest year in the dataset is: {latest_year}")

df_latest_year = df[df['Year'] == latest_year].copy()
print(f"Checkpoint 4: Final shape for {latest_year} data: {df_latest_year.shape}")

print(f"\nFirst 5 rows of the processed data for {latest_year}:")
print(df_latest_year.head())

output_filename = f"uk_accidents_{latest_year}.csv"
output_path = output_folder + output_filename

df_latest_year.to_csv(output_path, index=False)
print(f"\nSuccessfully saved processed file to '{output_path}'")
