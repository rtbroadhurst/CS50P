# takes two command line arguments
# in sys.argv[1], the name (or path) of a JPEG or PNG to read  as input
# in sys.argv[2], the name (or path) of a JPEG or PNG to write as output
# overlays shirt.png onto the input (after resising and cropping the image to the same size)
# saves this to the output


import sys
from PIL import Image, ImageOps

def get_args():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    input = sys.argv[1]
    output = sys.argv[2]

    ext1 = "." + input.rsplit(".", 1)[1].lower()
    ext2 = "." + output.rsplit(".", 1)[1].lower()

    ALLOWED = [".jpg", ".jpeg", ".png"]

    if ext1 not in ALLOWED or ext2 not in ALLOWED:
        sys.exit("Invalid output")

    if ext1 != ext2:
        sys.exit("Input and output have different extensions")

    return input, output

def overlay_image(input, output):
    input_image = Image.open(input)
    shirt_image = Image.open("shirt.png")
    resized = ImageOps.fit(input_image, shirt_image.size)
    resized.paste(shirt_image, mask=shirt_image)
    resized.save(output)

def main():
    input, output = get_args()
    try:
        overlay_image(input, output)
    except FileNotFoundError:
        sys.exit("Input does not exist")

if __name__ == "__main__":
    main()
