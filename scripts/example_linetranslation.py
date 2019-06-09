import sys

def sleep_for(y):
  time.sleep(y)

def add_numbers(x):
  result = 0
  for i in range(1, x):
    result += i

  return result

def main():
  x = int(sys.argv[1])
  y = int(sys.argv[2])
  
  result = add_numbers(x)

  sleep_for(y)

  print(f"The sum from 1 to {x} is {result}")

if __name__ == '__main__':
  main()

