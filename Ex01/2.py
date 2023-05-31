from collections import Counter;from tabulate import tabulate
counts = Counter( [char for char in input("Enter a string: ") if char.strip()]) #receive input from user , remove space character by strip
table = [[key, value] for key, value in counts.items()] # convert counter obj to a list of lists
print(tabulate(table, ["name","frequency"], tablefmt="grid"))