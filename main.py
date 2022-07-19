population = 0
change_direction = ""
change_rate = 0
time_scope = 0


def ask_population():
    global population
    population = int(input("Enter population (example: 126_000_000): "))


def ask_change_direction():
    global change_direction
    change_direction = str(input("Enter population change direction (example: +): "))


def ask_change_rate():
    global change_rate
    # Examples of input: https://en.wikipedia.org/wiki/List_of_countries_by_population_growth_rate
    change_rate = float(input("Enter population change rate per year in percentage (example: 0.7): ")) / 100


def ask_time_scope():
    global time_scope
    time_scope = int(input("Enter years for which the simulation is run (example: 20): "))


def calculator():
    global population
    global change_direction
    global change_rate
    global time_scope
    new_population = change_rate * population
    for x in range(time_scope):
        if change_direction == "+":
            population += new_population
        else:
            population -= new_population
        print("Year: ", x + 1, " ", population)


if __name__ == '__main__':
    ask_population()
    ask_change_direction()
    ask_change_rate()
    ask_time_scope()
    calculator()
