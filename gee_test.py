import ee

ee.Initialize(project="urbanheatai-499313")

print("Earth Engine Connected Successfully")

landsat = (
    ee.ImageCollection("LANDSAT/LC08/C02/T1_L2")
    .filterDate("2024-01-01", "2024-12-31")
    .sort("CLOUD_COVER")
)

print("Total Images:",
      landsat.size().getInfo())