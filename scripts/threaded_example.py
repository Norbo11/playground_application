from threading import Thread
import time


def sleep(x):
	result = 0
	for i in range(1, 99999999):
		result += 1
	#time.sleep(x)


def main():
	start = time.time()
	sleep(1)
	end = time.time()
	print(f"Sequential: {end - start}")


	t1 = Thread(target=sleep, args=(1,))
	t2 = Thread(target=sleep, args=(1,))
	
	t1.start()
	t2.start()

	t1.join()
	t2.join()
	end = time.time()
	print(f"Main ran for: {end - start}")


if __name__ == '__main__':
	main()
