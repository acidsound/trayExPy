from pystray import Icon as icon, Menu as menu, MenuItem as item
from PIL import Image, ImageDraw
import sys

color1 = 0xffffff
color2 = 0x000000
width = 16
height = 16

def create_image():
    image = Image.new('RGB', (width, height), color1)
    dc = ImageDraw.Draw(image)
    dc.rectangle(
        (width // 2, 0, width, height // 2),
        fill=color2)
    dc.rectangle(
        (0, height // 2, width // 2, height),
        fill=color2)
    return image

def exitApp(icn):
    icn.visible = False
    icn.stop()
    sys.exit()

ic = icon('unka', create_image())
ic.menu = menu(
    item('Exit', lambda: exitApp(ic))
)
ic.title = "unkara"
ic.run()
