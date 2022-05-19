import uuid
import argparse
import pyperclip as pc


def uuid_gen():
  s = str(uuid.uuid4()).replace('-', '')

  return s


if __name__ == '__main__':
  parser = argparse.ArgumentParser()
  parser.add_argument(
      '-c', help='copy generated uuid to clipboard', action="store_true")
  args = parser.parse_args()

  s = uuid_gen()

  print(s)

  if args.c:
    pc.copy(s)
    print("Copied to Clipboard!")
