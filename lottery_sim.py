import numpy as np


possible_numbers = list(range(1, 100_001))

prizes = ["Gordo", "Segundo", "Tercero"] + 2 * ["Cuarto"] + 8 * ["Quinto"] + 1_794 * ["Pedrea"]

def sim_lottery(number, possible_numbers, prizes):
    lottery_singleton = np.random.choice(possible_numbers, size=1807, replace=False)
    prize_singleton = np.random.choice(prizes, size=1807, replace=False)

    if number in lottery_singleton:
        return prize_singleton[np.where(lottery_singleton == number)[0][0]]



numero = 36_576

premios = np.array([])

num_simulations = 100_000

for i in range(num_simulations):
    if i % 10_000 == 0:
        print(f"Simulación {i}/{num_simulations}")

    premio = sim_lottery(numero, possible_numbers, prizes)

    if premio is not None:
        premios = np.append(premios, premio)

# Store the array with counts:
np.save("premios.npy", np.unique(premios, return_counts=True))