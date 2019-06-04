import time
import sys

def sleep_for(y):
  time.sleep(y)

def add_numbers(x):
  result = 0
  for i in range(1, x):
    result += i

  return result

def main():
  start = time.time()

  x = int(sys.argv[1])
  y = int(sys.argv[2])
  
  start_add = time.time()
  result = add_numbers(x)
  end_add = time.time()

  start_sleep = time.time()
  sleep_for(y)
  end_sleep = time.time()

  print(f"The sum from 1 to {x} is {result}")

  end = time.time()
  print(f"add_numbers({x}) ran for {end_add - start_add} seconds")
  print(f"sleep_for({y}) ran for {end_sleep - start_sleep} seconds")
  print(f"main() ran for {end - start} seconds")

if __name__ == '__main__':
  main()

