import rasterio
import matplotlib.pyplot as plt

temp_path = r"../LC09_L2SP_147039_20250630_20250701_02_T2/LC09_L2SP_147039_20250630_20250701_02_T2_ST_B10.TIF"

with rasterio.open(temp_path) as src:
    temp = src.read(1)

plt.figure(figsize=(8,6))
plt.imshow(temp, cmap="hot")
plt.colorbar(label="Temperature")
plt.title("Surface Temperature Map")
plt.savefig("temperature_map.png", dpi=300)
plt.show()