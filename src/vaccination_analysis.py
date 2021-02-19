import os
import matplotlib.pyplot as plt
import pandas as pd
import geopandas as gpd

# all data was gathered on 19th of Feb, 2021
INFO_PATH = "../data/country_info.csv"  # https://www.kaggle.com/koryto/countryinfo?select=covid19countryinfo.csv
VACCINATION_PATH = "../data/country_vaccinations.csv"  # https://www.kaggle.com/gpreda/covid-world-vaccination-progress
SHAPEFILE_PATH = "../shapefiles/ne_10m_admin_0_countries_lakes/ne_10m_admin_0_countries_lakes.shp"  # https://www.naturalearthdata.com/http//www.naturalearthdata.com/download/10m/cultural/ne_10m_admin_0_countries_lakes.zip


if __name__ == "__main__":
    colors = 100
    cmap = 'Blues'
    figsize = (16, 10)
    month_year = "02/2021"
    cols = []
    title = f"COVID-19 Vaccination on {month_year}"
    imgfile = f"../out/images/img_{title}.png"
    description = "If vaccination across various countries remain in the same pace(as of 19th of Feb, 2021), thats how the " \
                  "race goes. " \
                  "Data: Our World in Data - ourworldindata.org • Author: Gabriel Tardochi Salles".strip()
    geo_df = gpd.read_file(SHAPEFILE_PATH)[['ADM0_A3', 'geometry']].to_crs('+proj=robin')
    info_df = pd.read_csv(INFO_PATH, usecols=["country", "alpha3code", "pop"])
    a = info_df[~info_df['pop'].isna()]['pop'].str.replace(",", "").astype(int)
    print(a / 2)


