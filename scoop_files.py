import shutil
import glob
import os


def main(dir, ext):
  for folder in os.listdir(dir):
    for file in glob.glob('{}{}/*.{}'.format(dir, folder, ext)):
      shutil.move(file, dir)


if __name__ == '__main__':
  dir = input('Directory >>> ')
  dir = dir.replace('~', os.environ['HOME'])
  if dir[-1] != '/':
    dir += '/'

  ext = input('File Extension >>> ')
  ext = ext.replace('.', '')

  main(dir, ext)
