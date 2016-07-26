from PIL import Image
import sys
import re


def main():
    size = (600, 100)
    img = Image.new('RGB', size)
    with open('output.out', 'r') as f:
        lines = f.readlines()
        x = 0
        for line in lines:
            y = 0
            for val in rgb_from_line(line):
                r, g, b = rgb_from_val(val)
                img.putpixel((y, x), (r, g, b))
                y += 1
            x += 1
        img.show()


def rgb_from_val(val):
    return (map(lambda x: int(x, 16), re.findall('..', val)))

def rgb_from_line(line):
    for block in re.findall('......', line):
        yield block


def rgba_to_hex(rgba):
    return ''.join(map(dec_to_hex, rgba)[0:3])


def dec_to_hex(dec):
    hex_val = hex(dec).split('x')[1]
    if len(hex_val) == 1:
        return '0' + hex_val
    else:
        return hex_val

if __name__ == '__main__':
    sys.exit(main())
