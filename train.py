import rasterio
import numpy as np
import matplotlib.pyplot as plt

# NDVI files
b4 = rasterio.open("../LC09_L2SP_147039_20250630_20250701_02_T2/LC09_L2SP_147039_20250630_20250701_02_T2_SR_B4.TIF").read(1).astype(float)
b5 = rasterio.open("../LC09_L2SP_147039_20250630_20250701_02_T2/LC09_L2SP_147039_20250630_20250701_02_T2_SR_B5.TIF").read(1).astype(float)

ndvi = (b5 - b4) / (b5 + b4 + 1e-10)

# Temperature
temp = rasterio.open("../LC09_L2SP_147039_20250630_20250701_02_T2/LC09_L2SP_147039_20250630_20250701_02_T2_ST_B10.TIF").read(1)

# Hotspot condition
hotspot = np.where((temp > np.percentile(temp,90)) & (ndvi < 0.2),1,0)

plt.figure(figsize=(8,6))
plt.imshow(hotspot,cmap="Reds")
plt.title("Urban Heat Island Hotspots")
plt.colorbar()
plt.savefig("urban_heat_hotspots.png", dpi=300)
plt.show()