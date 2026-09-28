from PIL import Image
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

img = Image.open("input.png").convert("RGB")

out = Image.new("RGBA", img.size, (0, 0, 0, 0))

pixels = []
for r, g, b in img.getdata():
    # 흰색에서 얼마나 검은색에 가까운지
    alpha = 255 - round((r + g + b) / 3)

    pixels.append((0, 0, 0, alpha))

out.putdata(pixels)
out.save("output/output.png")
