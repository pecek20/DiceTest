import random
import time

def main():
	
	min = 1
	max = 6

	roll_again = "tak"
	while roll_again == "tak":
		print("Rzucam kostka...")
		time.sleep(2)
		print("Kostka turtla sie...")
		time.sleep(2)
		wynik = random.randint(min,max)		
		print("Wynik to: ", wynik)
	
		roll_again = input("Rzucic kostka jeszcze raz? (tak/nie): ")

if __name__ == '__main__':
	main()
