import sys
import datetime


def calculate(val):
  num = 2
  num_list = []
  num_dict = {}

  while val >= num:
    if (val % num) == 0:
      num_list.insert(0, num)
      val /= num
    else:
      num += 1

  for num in sorted(num_list):
    num_dict[num] = num_list.count(num)

  return num_dict


def main():
  time = datetime.datetime.now()
  print('Input a integer that is 2 or more.')
  print('If you want to quit, input "q" (or "quit", "exit").')

  available_value = False

  while available_value == False:
    if len(sys.argv) > 1:
      value = sys.argv[1]
      print('>>> ', value)
    else:
      value = input('>>> ')

    try:
      if value == 'q' or value == 'quit' or value == 'exit':
        available_value = True
        continue
      elif int(value) >= 2:
        num = 2
        result = calculate(int(value))

        for num in result:
          if num == list(result.keys())[-1]:
            print('(', num, '^', result[num], ')')
          else:
            print('(', num, '^', result[num], ')', '+', end=' ')

        if len(sys.argv) > 1:
          available_value = True
        else:
          available_value = False
        continue
      elif int(value) < 2:
        raise Exception('The value is not 2 or more. ')
        continue
    except Exception as error:
      print('\nError: The value is not available. ', error, '\n')

      if len(sys.argv) > 1:
        available_value = True
      continue


if __name__ == '__main__':
  main()
