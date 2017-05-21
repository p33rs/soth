import os
from PIL import Image, ImageDraw, ImageFont

class Generator(object):
  
  def __init__(self, meme, image_path = None, font_path = None):
    self.meme = meme
    if font_path:
      self.font_path = font_path
    else:
      self.font_path = os.path.join(os.getcwd(), 'fonts')
    if image_path:
      self.image_path = image_path
    else:
      self.image_path = os.path.join(os.getcwd(), 'images')

  def generate(self, text):
    font = ImageFont.truetype(os.path.join(self.font_path, self.meme.font))
    bg = self.load_image(self.meme.image)
    fg = self.generate_text(text, font, self.meme.color)
    return self.smash(bg, fg)

  def smash(self, bg, fg):
    max_wide = self.meme.last[0] - self.meme.first[0]
    max_tall = self.meme.last[1] - self.meme.first[1]
    cur_wide, cur_tall = fg.size
    width = max_wide if max_wide < cur_wide else cur_wide
    height = max_tall if max_tall < cur_tall else cur_tall
    fg = fg.resize((width, height)) 
    bg.paste(fg, self.meme.first, fg)
    return bg
  
  def load_image(self, image):
    return Image.open(os.path.join(self.image_path, image))

  def generate_text(self, text, font, color):
    image = Image.new('RGBA', self.calculate_size(text, font), (255,255,255,0))
    d = ImageDraw.Draw(image)
    d.text((0, 0), text, font=font, fill=color)
    return image

  def calculate_size(self, text, font):
    image = Image.new('RGBA', (1, 1), (255,255,255,0))
    d = ImageDraw.Draw(image)
    return d.multiline_textsize(text, font)
