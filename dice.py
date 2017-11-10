import random
import time

def main():
	
	min = 1
	max = 6

	roll_again = "yes"
	while roll_again == "yes" or roll_again == "y":
		print("Roling the diced...")
		time.sleep(5)
		print("The value are...")
		time.sleep(2)
		print(random.randint(min,max))
	
		roll_again = input("Roll the dice again? (yes/y or no/n): ")

if __name__ == '__main__':
	main()
