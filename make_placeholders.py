# make_placeholders.py
from PIL import Image, ImageDraw
import os

os.makedirs("img", exist_ok=True)

# car image
car_size = (49, 90)
car = Image.new("RGBA", car_size, (20, 140, 20, 255))
draw = ImageDraw.Draw(car)
draw.rectangle([6, car_size[1]-18, car_size[0]-6, car_size[1]-8], fill=(40,40,40,255))
car.save("img/car.png")

# enemy car
enemy_size = (49, 100)
enemy = Image.new("RGBA", enemy_size, (160, 20, 20, 255))
draw = ImageDraw.Draw(enemy)
draw.rectangle([6, enemy_size[1]-18, enemy_size[0]-6, enemy_size[1]-8], fill=(40,40,40,255))
enemy.save("img/enemy_car_1.png")

# background (360x600)
bg_size = (360, 600)
bg = Image.new("RGB", bg_size, (80, 80, 80))
draw = ImageDraw.Draw(bg)
# grass at left and right
draw.rectangle([0,0,24,bg_size[1]], fill=(34,139,34))
draw.rectangle([bg_size[0]-24,0,bg_size[0],bg_size[1]], fill=(34,139,34))
# center dashed stripes
for y in range(0, bg_size[1], 60):
    draw.rectangle([bg_size[0]//2-6, y+18, bg_size[0]//2+6, y+36], fill=(255,255,255))
bg.save("img/back_ground.jpg")

print("Created placeholders: img/car.png, img/enemy_car_1.png, img/back_ground.jpg")
