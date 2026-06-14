import rasterio
import numpy as np
import matplotlib.pyplot as plt

b4_path = r"../LC09_L2SP_147039_20250630_20250701_02_T2/LC09_L2SP_147039_20250630_20250701_02_T2_SR_B4.TIF"

b5_path = r"../LC09_L2SP_147039_20250630_20250701_02_T2/LC09_L2SP_147039_20250630_20250701_02_T2_SR_B5.TIF"

with rasterio.open(b4_path) as red:
    red_band = red.read(1).astype(float)

with rasterio.open(b5_path) as nir:
    nir_band = nir.read(1).astype(float)

ndvi = (nir_band - red_band) / (nir_band + red_band + 1e-10)

plt.imshow(ndvi, cmap="RdYlGn")
plt.colorbar(label="NDVI")
plt.title("NDVI Map")
plt.savefig("ndvi_map.png", dpi=300)
plt.show()