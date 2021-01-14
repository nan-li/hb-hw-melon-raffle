"""Randomly pick customer and print customer info"""

# Add code starting here

# Hint: remember to import any functions you need from
# other files or libraries

import customers
from random import choice

def pick_winner(filename):
	all_customers = customers.get_customers_from_file(filename)
	winner = choice(all_customers)
	print(f'{winner.name} with email {winner.email} who lives at {winner.street}, {winner.city}, {winner.zipcode} won')

if __name__ == '__main__':
	pick_winner('customers.txt')