import utils

data = utils.output("operations.json")

for string in data:
    print(
        f"{string['date']} {string['description']}\n"
        f"{string['to']} -> {string['to']}\n"
        f"{string['amount']} {string['name']}\n\n"
    )

