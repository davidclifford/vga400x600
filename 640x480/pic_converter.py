import json#
# VGA PIC converter
#

from numpy import uint8, uint16
from PIL import Image
import sys
import pygame
from pygame import gfxdraw

filename = 'forest-glade'

def plot(x, y, r, g, b):
    xsize = 2
    ysize = 2
    col = (r << 3, g << 3, b << 3)
    #col = (r, g, b)
    for yy in range(ysize):
        for xx in range(xsize):
            gfxdraw.pixel(screen, x*xsize+xx, y*ysize+yy, col)


pygame.init()
screen = pygame.display.set_mode((1280, 960))

image = Image.open(filename+'.png')
pixels = image.load()

rom_file = open(filename + '.bin', 'wb')

for y in range(525):
    for x in range(800):
        data = 0
        if x < 640 and y < 480:
            pix = pixels[x, y]
            red = pix[0] >> 3
            grn = pix[1] >> 3
            blu = pix[2] >> 3
            colour = red << 10 | grn << 6 | blu << 0
            data = data | uint16(colour)
            # plot(x, y, red, grn, blu)
            plot(x, y, red, grn, blu)

        rom_file.write(uint16(data))

    pygame.display.update()

rom_file.close()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
