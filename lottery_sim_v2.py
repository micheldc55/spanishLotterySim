import json

import numpy as np


def optimized_sim_lottery_corrected(
        your_number: int, 
        num_simulations: int, 
        possible_numbers: list, 
        prizes: list
    ) -> dict:
    """Run a lottery with a given number of simulations and return the cumulative number of prizes won for each 
    one of the prizes in the "prizes" list.

    Args:
        your_number (int): Number you "select" during the simulation
        num_simulations (int): Number of simulations you want to run simultaneously
        possible_numbers (list): List of possible numbers in the lottery
        prizes (list): List of prizes in the lottery

    Returns:
        dict: A dictionary with the count for the number of prizes won by the selected number in each category.
    """
    lottery_matrix = np.array([np.random.choice(possible_numbers, size=1807, replace=False)
                               for _ in range(num_simulations)])

    prize_matrix = np.array([np.random.choice(prizes, size=1807, replace=False)
                             for _ in range(num_simulations)])

    your_number_indices = np.where(lottery_matrix == your_number)

    winning_prizes = prize_matrix[your_number_indices]

    prize_counts = dict(zip(*np.unique(winning_prizes, return_counts=True)))

    return prize_counts

def run_simulations_in_batches(
        your_number: int, 
        num_batches: int, 
        simulations_per_batch: int, 
        possible_numbers: list, 
        prizes: list
    ) -> dict:
    """Runs the lottery simulations in batches and returns the cumulative number of prizes won for each one of the 
    prizes in the "prizes" list.

    Args:
        your_number (int): Your selected number
        num_batches (int): Number of sets of simulations_per_batch simulations you want to run
        simulations_per_batch (int): Number of simulations you want to run in each batch
        possible_numbers (list): Possible numbers a user can select from in the lottery
        prizes (list): List of prizes in the lottery

    Returns:
        dict: A dictionary with the count for the number of prizes won by the selected number in each prize category.
    """
    cumulative_prize_counts = {}

    for batch in range(num_batches):
        batch_prize_counts = optimized_sim_lottery_corrected(your_number, simulations_per_batch, possible_numbers, prizes)

        for prize, count in batch_prize_counts.items():
            cumulative_prize_counts[prize] = cumulative_prize_counts.get(prize, 0) + count

        print(f"Batch {batch + 1}: Current cumulative prize counts: {cumulative_prize_counts}")

    return cumulative_prize_counts



#TODO: Implement the function optimized_sim_lottery with parallel processing (multithreading or multiprocessing)

if __name__ == "__main__":
    num_batches = 10
    simulations_per_batch = 100_000
    your_number = 36576
    possible_numbers = list(range(1, 100001))
    prizes = ["Gordo", "Segundo", "Tercero"] + 2 * ["Cuarto"] + 8 * ["Quinto"] + 1794 * ["Pedrea"]

    final_cumulative_prize_counts = run_simulations_in_batches(your_number, num_batches, simulations_per_batch, possible_numbers, prizes)

    print(final_cumulative_prize_counts)
