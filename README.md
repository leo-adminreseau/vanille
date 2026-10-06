# groupe2_package

Package pédagogique créé par le **Groupe 2** dans le cadre du TD 1 (M1 Cyber —
Introduction à l'IA : Créer son algorithme).

`groupe2_package` fournit des fonctions réutilisables de **filtrage** et de
**jointure** sur des DataFrames pandas, construites à partir du jeu de
données `cardata.csv`.

## Fonctions disponibles

Les fonctions se trouvent dans le module `groupe2_package.utils_groupe2`.

- `filter_dataframe(df, column, value)` — garde les lignes où `column` vaut
  exactement `value`.
- `filter_by_range(df, column, min_value, max_value)` — garde les lignes
  dont la valeur numérique de `column` est comprise entre `min_value` et
  `max_value` (bornes incluses).
- `join_dataframes(df1, df2, on, how="left")` — jointure entre deux
  DataFrames sur la ou les colonnes `on`. Le type de jointure se règle avec
  `how` (`"left"` par défaut).

Aucune de ces fonctions ne contient de valeur fixe : tous les critères sont
passés en paramètres, ce qui permet de les réutiliser sur n'importe quel
DataFrame respectant la même structure.

## Structure du projet

```
Algo_groupe2/
├── Algo/
│   ├── cardata.csv
│   ├── Script_groupe2.py
│   ├── README.md
│   ├── LICENSE.txt
│   ├── setup.py
│   └── groupe2_package/
│       ├── __init__.py
│       └── utils_groupe2.py
└── test_package/
    ├── cardata.csv
    └── test_Script_groupe2.py
```

## Construction du package (.whl)

Depuis le dossier `Algo/` :

```bash
python3 setup.py sdist bdist_wheel
```

Le fichier à installer est généré dans `dist/` :
`groupe2_package-0.1-py3-none-any.whl`.

Après une modification du code, supprimer les anciens fichiers de build
avant de reconstruire :

```bash
rm -rf build dist *.egg-info
python3 setup.py sdist bdist_wheel
```

## Installation

Depuis le dossier `test_package/` :

```bash
python3 -m pip install --force-reinstall ../Algo/dist/groupe2_package-0.1-py3-none-any.whl
```

`pandas` est installé automatiquement comme dépendance.

## Utilisation

```python
import pandas as pd
from groupe2_package.utils_groupe2 import (
    filter_dataframe,
    filter_by_range,
    join_dataframes,
)

df = pd.read_csv("cardata.csv", delimiter=";")

# Filtrage exact : voitures à essence
petrol_cars = filter_dataframe(df, column="Fuel_Type", value="Petrol")

# Filtrage par intervalle : prix de vente entre 2 et 5
affordable = filter_by_range(df, column="Selling_Price", min_value=2, max_value=5)

# Jointure avec une table de correspondance
fuel_labels = pd.DataFrame({
    "Fuel_Type": ["Petrol", "Diesel", "CNG"],
    "Fuel_Label_FR": ["Essence", "Diesel", "Gaz naturel"],
})
labeled = join_dataframes(petrol_cars, fuel_labels, on="Fuel_Type", how="left")
```

## Test

Depuis `test_package/` (le fichier `cardata.csv` doit être dans le même
dossier) :

```bash
python3 test_Script_groupe2.py
```

Résultats attendus sur `cardata.csv` :

- 239 voitures à essence (`Petrol`) ;
- 87 voitures avec un `Selling_Price` entre 2 et 5 ;
- une nouvelle colonne `Fuel_Label_FR` après la jointure.
