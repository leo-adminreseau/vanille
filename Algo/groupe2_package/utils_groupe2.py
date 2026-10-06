import pandas as pd


def filter_dataframe(df, column, value):
    """Garde les lignes où column == value."""
    return df[df[column] == value]


def filter_by_range(df, column, min_value, max_value):
    """Garde les lignes où min_value <= column <= max_value."""
    return df[(df[column] >= min_value) & (df[column] <= max_value)]


def join_dataframes(df1, df2, on, how="left"):
    """Jointure de df1 et df2 sur la colonne 'on'."""
    return df1.merge(df2, on=on, how=how)