# Spanish Christmas Lottery Simulation

## Introduction

The Spanish Christmas Lottery, also known as "El Gordo", is one of the largest and oldest lotteries in the world. This project aims to simulate the lottery to approximate the probabilities of winning different prizes, using computational methods. This was cooked up in 1-2 days after noticing the incredible popularity the lottery has in Spain during Christmas. The popularity sparked my curiosity and I wanted to know what was the probability of winning the lottery, but I quickly noticed the probability was not easy to calculate in an analytical way. 

The probability of winning the first price (the "Gordo de Navidad") is not straightforward, due to the fact that the probability changes with each draw. One can calculate such probability, but you would need an awful lot of pieces of paper just to write the combinations. It's an easy thing, but I'm more of a programmer than a mathematician so I thought it would be both simpler and more compelling to simulate the lottery versus manually deriving the analytical formula.

But, before we get to that, I think we need to understand how the Spanish lottery works.

## How the Lottery Works

The Spanish Christmas Lottery is quite unique in its structure, at least to me:

There are a total of **1807 prizes**.
The prizes are categorized as follows: 1 "Gordo" (grand prize), 1 "Segundo" (second prize), 1 "Tercero" (third prize), 2 "Cuarto" (fourth prizes), 8 "Quinto" (fifth prizes), and 1794 "Pedrea" (consolation prizes).
Each prize is drawn from a pool of 100,000 numbers that go from 00000 to 99,999.

During the day of the show, the numbers are drawn from two drums containing the balls. The smaller one contains balls labelled with the 1,807 prizes, one of which is "el Gordo", while the second one contains the 100,000 balls labelled with the numbers that participate in the lottery. Numbers are drawn simultaneously from the two drums, and the number is matched with the prize, so if the second prize comes out of the first drum and the number 17,431 comes out of the second one, then that number wins the second prize. **No drawn balls are replaced in the drum.**

## The Challenge

There is a common misconception that winning the first prize ("el Gordo") is 1 in 100,000, due to the fact that there are 100,000 numbers and that you own **one** of those numbers, being sampled at random. But this isn't the case, and I'm here to convince you reader that this is not the case. I would agree that the 1/100,000 is the **lower bound** of the probability, but it's a little more complicated than that. The 1/100,000 is actually the probability of winning the first prize on the first go. The number of balls in the drum is reduced every time a ball is drawn, so it's actually better for you the later the first prize is drawn, provided that your number hasn't come out yet.

Calculating the probabilities of winning each prize manually is a daunting task due to the sheer number of possible combinations and prize categories. Traditional methods would require complex combinatorial calculations, making it impractical to calculate by hand. The reasoning goes as follows: To estimate the probability of winning the first prize you need to win it in one of the 1,807 draws. The probability of winning the first prize can be computed as the sum of the following probabilities:

- The probability of winning the first prize on the first go.
- + the probability of winning the first prize on the second go, given that you didn't win on the first go.
- + the probability of winning the first prize on the third go, given that you didn't win on the first or second go.
- ...
- + the probability of winning the first prize on the last go, given that you didn't win on the previous go's.

## Computational Approach

To overcome this challenge, several computational methods were employed:

**Brute Force Method:** Utilizes nested loops to simulate the lottery process. While straightforward, this method is computationally intensive and inefficient.

**Numpy Arrays with Loop:** Improves upon the brute force method by using NumPy arrays for generating lottery numbers and a loop to check for winning numbers. This method offers better performance but still has limitations.

**Vectorized Computations:** The most elegant and efficient solution. It leverages NumPy's vectorized operations to generate simulations and check for winning numbers, significantly reducing computation time. In tests, for 10,000 lottery simulations, this method was approximately 20 times faster than the brute force approach.

# Next Steps

## Future enhancements to this project will include:

- **Implementing Multiprocessing/Multithreading:** To further improve the efficiency of simulations, especially for very large numbers of simulations.
- **Statistical Analysis and Visualization:** Analyzing the simulation data in-depth and visualizing the probability distributions and other relevant statistics.
- **Deployment:** Deploy a batch process that can be run on demand. Deploy with CI/CD
