from PIL import Image, ImageDraw, ImageFont

def calculate_size(text, font):
  image = Image.new('RGBA', (1, 1), (255,255,255,0))
  d = ImageDraw.Draw(image)
  return d.multiline_textsize(text, font)

text = "Fuck Hello Yes Hello\nWhat Warf Wup Dup Wap\nButttttt\nButt\nButt"
font = ImageFont.truetype('fonts/comic.otf', 16)
image = Image.new('RGBA', calculate_size(text, font), (255,255,255,0))
d = ImageDraw.Draw(image)
d.text((0, 0), text, font=font, fill=(0,0,0,255))
image.save('/home/jon/i/testpy.jpg', 'jpeg')

