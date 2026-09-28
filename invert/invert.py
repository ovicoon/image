from PIL import Image, ImageOps
import os
import numpy as np

os.chdir(os.path.dirname(os.path.abspath(__file__)))

img = Image.open("input.png").convert("RGBA")

arr = np.array(img)

# RGB만 반전
arr[:, :, :3] = 255 - arr[:, :, :3]

# Alpha(arr[:, :, 3])는 건드리지 않음

result = Image.fromarray(arr)
result.save("output/output.png")
