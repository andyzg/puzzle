from PIL import Image
import sys


def main(img_path):
    img = Image.open(img_path)
    pixels = img.load()
    width, height = img.size
    grid = []
    for y in xrange(0, height):
        row = []
        for x in xrange(0, width):
            row.append(rgba_to_hex(pixels[x, y]))
        grid.append(''.join(row))
    with open('output.out', 'w') as f:
        f.write('\n'.join(grid))


def rgba_to_hex(rgba):
    return ''.join(map(dec_to_hex, rgba)[0:3])


def dec_to_hex(dec):
    hex_val = hex(dec).split('x')[1]
    if len(hex_val) == 1:
        return '0' + hex_val
    else:
        return hex_val

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print 'Must have 1 argument: python easteregg.py <img_path>'
        sys.exit(1)

    sys.exit(main(sys.argv[1]))
