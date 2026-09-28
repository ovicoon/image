from PIL import Image, ImageDraw, ImageFont
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

# 1. 배경 이미지 불러오기
bg_img_path = "background.png"  # 배경 이미지 경로
img = Image.open(bg_img_path).convert("RGB")  # RGB로 변환
draw = ImageDraw.Draw(img)

# 폰트 경로
font_path = os.path.join(os.path.dirname(__file__), "font.ttf")
font = ImageFont.truetype(font_path, 300)
s_font = ImageFont.truetype(font_path, 200)


# 텍스트
class Text:
    def __init__(self, text, font, dx, dy):
        self.text = text
        self.font = font

        # 텍스트 크기 계산
        bbox = draw.textbbox((0, 0), text, font=font)
        text_width = bbox[2] - bbox[0]
        text_height = bbox[3] - bbox[1]

        # 중앙 좌표 계산
        self.dx = dx
        self.dy = dy
        self.x = (img.width - text_width) / 2 + self.dx
        self.y = (img.height - text_height) / 2 + self.dy

    def draw(self):
        # 텍스트 그리기
        draw.text((self.x, self.y), self.text, font=self.font, fill="white")


Text("Selement", font, 0, -300).draw()
Text("explore, survive, awaken", s_font, 0, 0).draw()
# 저장
img.save("output\output.png")
