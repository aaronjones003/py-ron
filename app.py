import requests
from PIL import Image, ImageFont, ImageDraw
from io import BytesIO
from random import randint

clientId = 'SECRET'

def getRandomPhoto():
  randomPhotoEndpoint = 'https://api.unsplash.com/photos/random/?client_id=' + clientId
  randomPhotoData = requests.get(randomPhotoEndpoint).json()
  rawRandomPhoto = requests.get(randomPhotoData['urls']['raw'])
  return Image.open(BytesIO(rawRandomPhoto.content))

def getQuote():
  return requests.get('http://ron-swanson-quotes.herokuapp.com/v2/quotes').json()[0]

def getFontSize(quote, font, width, scale):
  thisFont = ImageFont.truetype(font, width)
  canvas = Image.new('RGBA', (width, width) , (255,255,255,0))
  drawContext = ImageDraw.Draw(canvas)
  overSize = drawContext.textsize(quote, thisFont)
  return int((width * scale) / (overSize[0] / width))

randomPhoto = getRandomPhoto()
quote = getQuote()

r, g, b = randomPhoto.split()
rMod = r.point(lambda i: i / 2)
gMod = g.point(lambda i: i / 2)
bMod = b.point(lambda i: i / 2)
channels = rMod, gMod, bMod
randChannels = channels[randint(0, 2)], channels[randint(0, 2)], channels[randint(0, 2)]
imageMorph = Image.merge('RGB', randChannels).convert('RGBA')

# font
fontPath = 'font.ttf'
fontSize = getFontSize(quote, fontPath, imageMorph.size[0], 0.8)
font = ImageFont.truetype(fontPath, fontSize)

# make a blank image for the text, initialized to transparent text color
textImage = Image.new('RGBA', imageMorph.size, (255,255,255,0))
# get a drawing context
drawContext = ImageDraw.Draw(textImage)
# draw text, full opacity
drawContextTextSize = drawContext.textsize(quote, font)

textPosition = int(imageMorph.size[0] / 2 - drawContextTextSize[0] / 2), int(imageMorph.size[1] / 2 - fontSize)

drawContext.text(textPosition, quote, font=font, fill=(255,255,255,255))

imageWithText = Image.alpha_composite(imageMorph, textImage)

imageWithText.show()
imageWithText.save('image{0}.png'.format(randint(1, 10000000)))
