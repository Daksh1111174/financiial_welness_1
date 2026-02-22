import numpy as np

def monte_carlo(initial, years=10, simulations=500):
    mu, sigma = 0.12, 0.2
    results = []

    for _ in range(simulations):
        value = initial
        for _ in range(years):
            value *= (1 + np.random.normal(mu, sigma))
        results.append(value)

    return np.array(results)
