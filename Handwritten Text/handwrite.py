from PIL import Image, ImageDraw, ImageFont

txt = """Python is a high-level programming language known 
for its simple and readable syntax."""

img = Image.new("RGB", (900, 300), "white")
draw = ImageDraw.Draw(img)

font = ImageFont.truetype("C:/Windows/Fonts/segoesc.ttf", 26)

draw.text((20, 20), txt, fill=(0, 0, 138), font=font)

img.save("handtxt.png")

print("END")