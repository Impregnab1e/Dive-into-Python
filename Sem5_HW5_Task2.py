# names = ["Alice", "Bob", "Charlie"]
# salary = [5000, 6000, 7000]
# bonus = ["10%", "5%", "15%"]

result = {name: salary * float(b.replace("%", "")) / 100 for name, salary, b in zip(names, salary, bonus)}
print(result)