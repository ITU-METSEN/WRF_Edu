import cdsapi

c = cdsapi.Client()

YEAR = '2026'
MONTH = '01'
DAY = ["1", "2"]

# Sol-üst nokta kord.(lat,lon), Sağ-alt nokta kord.(lat,lon)
# [North_Lat, West_Lon, South_Lat, East_Lon]
AREA = [65, 5, 25, 60]
# 65N,5E noktasından 25N,60E noktasına

c.retrieve(
    'reanalysis-era5-pressure-levels',
    {
        'product_type': 'reanalysis',
        'format': 'grib',
        'pressure_level': [
            '1', '2', '3',
            '5', '7', '10',
            '20', '30', '50',
            '70', '100', '125',
            '150', '175', '200',
            '225', '250', '300',
            '350', '400', '450',
            '500', '550', '600',
            '650', '700', '750',
            '775', '800', '825',
            '850', '875', '900',
            '925', '950', '975',
            '1000',
        ],
        'variable': [
            'geopotential', 'relative_humidity', 'temperature',
            'u_component_of_wind', 'v_component_of_wind'
        ],
        'year': YEAR,
        'month': MONTH,
        'day': DAY,
        'time':'00/to/23/by/1', 
        'area': AREA,
    },
    'ERA5_PL.grib')

c.retrieve(
    'reanalysis-era5-single-levels',
    {
        'product_type': 'reanalysis',
        'variable': [
            'sea_surface_temperature',
        ],
        'year': YEAR,
        'month': MONTH,
        'day': DAY,
        'time':'00/to/23/by/1', 
        'area': AREA,
        'format': 'grib',
    },
    'ERA5_SST.grib')

c.retrieve(
    'reanalysis-era5-single-levels',
    {
        'product_type': 'reanalysis',
        'variable': [
            '10m_u_component_of_wind', '10m_v_component_of_wind','2m_dewpoint_temperature',
            '2m_temperature', 'land_sea_mask', 'mean_sea_level_pressure',
            'sea_ice_cover', 'sea_surface_temperature', 'skin_temperature',
            'snow_density', 'snow_depth', 'soil_temperature_level_1','geopotential',
            'soil_temperature_level_2', 'soil_temperature_level_3', 'soil_temperature_level_4',
            'soil_type', 'surface_pressure', 'volumetric_soil_water_layer_1',
            'volumetric_soil_water_layer_2', 'volumetric_soil_water_layer_3', 'volumetric_soil_water_layer_4',
        ],
        'year': YEAR,
        'month': MONTH,
        'day': DAY,
        'time':'00/to/23/by/1', 
        'area': AREA,
        'format': 'grib',
    },
    'ERA5_SFC.grib')
