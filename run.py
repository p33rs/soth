from meme import Meme
from generator import Generator

meme = Meme('horse.jpg', (20,20), (120,200), 'comic.otf', (0,0,0,255))

generator = Generator(meme)

generator.generate("Yes hello, \n This is a test.").save('/home/jon/i/testpy.jpg', 'jpeg')



