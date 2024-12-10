import sys
import os
from waveshare_epd import epd2in13_V4
import time
from PIL import Image, ImageDraw, ImageFont
import logging

logging.basicConfig(level=logging.DEBUG)

try:
    logging.info("epd2in13_V4 Demo")

    epd = epd2in13_V4.EPD()
    logging.info("Init and Clear")
    epd.init()
    epd.Clear(0xFF)

    # Load fonts
    picdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'pic')
    font24 = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 24)  # Change size if needed

    # Create a new image to draw on
    image = Image.new('1', (epd.height, epd.width), 255)  # 255: clear the frame
    draw = ImageDraw.Draw(image)

    # Load and paste the BMW logo
    bmw_logo_path = os.path.join(picdir, 'bmw_logo.bmp')
    if not os.path.exists(bmw_logo_path):
        raise FileNotFoundError("BMW logo file not found: " + bmw_logo_path)

    bmw_logo = Image.open(bmw_logo_path)
    image.paste(bmw_logo, (5, 5))  # Adjust the position as necessary

    # Add the text "??????" on the right
    text_position = (100, 40)  # Adjust as needed
    draw.text(text_position, "?????", font=font24, fill=0)

    # Display the image
    epd.display(epd.getbuffer(image))
    time.sleep(2)

    logging.info("Clear...")
    epd.init()
    epd.Clear(0xFF)

    logging.info("Goto Sleep...")
    epd.sleep()

except IOError as e:
    logging.info(e)

except KeyboardInterrupt:
    logging.info("ctrl + c:")
    epd2in13_V4.epdconfig.module_exit(cleanup=True)
    exit()
