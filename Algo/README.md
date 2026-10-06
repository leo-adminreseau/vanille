# nicolas_package

Package pédagogique créé par **Nicolas** dans le cadre du TD 1 (M1 Cyber —
Introduction à l'IA : Créer son algorithme).

`nicolas_package` fournit des fonctions réutilisables de **filtrage** et de
**jointure** sur des DataFrames pandas, construites à partir du jeu de
données `cardata.csv`.

## Fonctions disponibles

- `filter_dataframe(df, column, value)` — garde les lignes où `column` vaut
  exactement `value`.
- `filter_by_range(df, column, min_value, max_value)` — garde les lignes
  dont la valeur numérique de `column` est comprise entre `min_value` et
  `max_value` (bornes incluses).
- `join_dataframes(df1, df2, on, how="inner")` — jointure entre deux
  DataFrames sur la ou les colonnes `on`.

Aucune de ces fonctions ne contient de valeur fixe : tous les critères sont
passés en paramètres, ce qui permet de les réutiliser sur n'importe quel
DataFrame respectant la même structure.

## Installation

```bash
pip install dist/nicolas_package-0.1-py3-none-any.whl
```

## Utilisation

```python
import pandas as pd
from nicolas_package.utils_Nicolas import (
    filter_dataframe,
    filter_by_range,
    join_dataframes,
)

df = pd.read_csv("cardata.csv", delimiter=";")
petrol_cars = filter_dataframe(df, "Fuel_Type", "Petrol")
affordable = filter_by_range(df, "Selling_Price", 0, 5)
```
