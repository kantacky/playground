from pathlib import Path
from PIL import Image

dist = '/Users/kantacky/Downloads/Path-to-Images-Dir'


def convert_jpg_to_webp(source):
  destination = source.with_suffix('.webp')

  image = Image.open(source)
  image.save(destination, format='webp')

  return destination


def main():
  paths = Path(dist).glob('*.JPG')
  for path in paths:
    webp_path = convert_jpg_to_webp(path)
    print(webp_path)


if __name__ == '__main__':
  main()
