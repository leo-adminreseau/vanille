import pandas as pd

# nicolas_package est maintenant installé via pip (fichier .whl) :
# on l'importe comme n'importe quel autre module Python.
from groupe2_package.utils_groupe2 import (
    filter_dataframe,
    filter_by_range,
    join_dataframes,
)

# Read the CSV file
file_path = 'cardata.csv'
delimiter = ';'
df = pd.read_csv(file_path, delimiter=delimiter)

print("Aperçu des données :")
print(df.head())

# --- 1. Filtrage exact : uniquement les voitures à essence (Petrol) ---
petrol_cars = filter_dataframe(df, column="Fuel_Type", value="Petrol")
print(f"\nVoitures Petrol : {len(petrol_cars)} lignes")
print(petrol_cars.head())

# --- 2. Filtrage par intervalle : prix de vente entre 2 et 5 (lakhs) ---
affordable_cars = filter_by_range(df, column="Selling_Price", min_value=2, max_value=5)
print(f"\nVoitures entre 2 et 5 (Selling_Price) : {len(affordable_cars)} lignes")
print(affordable_cars.head())

# --- 3. Jointure : on enrichit les voitures Petrol avec une table de correspondance ---
fuel_labels = pd.DataFrame({
    "Fuel_Type": ["Petrol", "Diesel", "CNG"],
    "Fuel_Label_FR": ["Essence", "Diesel", "Gaz naturel"],
})
petrol_cars_labeled = join_dataframes(petrol_cars, fuel_labels, on="Fuel_Type", how="left")
print("\nVoitures Petrol enrichies (jointure) :")
print(petrol_cars_labeled.head())
