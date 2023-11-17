import geopandas as gpd
import matplotlib as mtlp

geo = gpd.read_file("Carpeta Prueba\circuitos-electorales.csv")

geo.plot()