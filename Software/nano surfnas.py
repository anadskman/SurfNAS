import time
import board
import neopixel
import psutil
import digitalio
import busio
from PIL import Image, ImageDraw, ImageFont
import adafruit_ssd1306
import os

pixels = neopixel.NeoPixel(board.D18, 1)

button = digitalio.DigitalInOut(board.D17)
button.direction = digitalio.Direction.INPUT
button.pull = digitalio.Pull.UP

i2c = busio.I2C(board.SCL, board.SDA)
display = adafruit_ssd1306.SSD1306_I2C(128, 64, i2c)

width = display.width
height = display.height

image = Image.new("1", (width, height))
draw = ImageDraw.Draw(image)
font = ImageFont.load_default()

while True:

    cpu = psutil.cpu_percent()
    ram = psutil.virtual_memory().percent
    disk = psutil.disk_usage("/").percent
    ip = os.popen("hostname -I").read().strip()

    if cpu < 40:
        pixels[0] = (0, 255, 0)
    elif cpu < 80:
        pixels[0] = (255, 150, 0)
    else:
        pixels[0] = (255, 0, 0)

    draw.rectangle((0,0,width,height), outline=0, fill=0)

    draw.text((0,0), "SurfNAS", font=font, fill=255)
    draw.text((0,15), f"CPU: {cpu}%", font=font, fill=255)
    draw.text((0,30), f"RAM: {ram}%", font=font, fill=255)
    draw.text((0,45), f"Disk: {disk}%", font=font, fill=255)

    display.image(image)
    display.show()

    if not button.value:
        os.system("sudo shutdown now")

    time.sleep(2)