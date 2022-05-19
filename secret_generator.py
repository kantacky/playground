import secrets


def secret_gen(n_bytes):
  return secrets.token_urlsafe(n_bytes)


if __name__ == '__main__':
  n_bytes = input('Bytes (Recommended: 32) >>> ')
  print(secret_gen(int(n_bytes)))
