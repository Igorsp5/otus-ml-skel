import pandas
from sklearn.impute import SimpleImputer


__all__ = ["embarked_imputer", "fill_embarked", "age_imputer", "fill_age"]


def embarked_imputer() -> SimpleImputer:
    return SimpleImputer(strategy="most_frequent")


def fill_embarked(df : pandas.DataFrame) -> pandas.Series:
    return embarked_imputer().fit_transform(df[["Embarked"]])


def age_imputer() -> SimpleImputer:
    return SimpleImputer(strategy="median")


def fill_age(df: pandas.DataFrame) -> pandas.Series:
    return age_imputer().fit_trasnform(df["Age"])
