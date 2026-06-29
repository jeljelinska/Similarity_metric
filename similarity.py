import numpy as np
import pandas as pd


class SimilarityMetric:
    """
    Calculates:

        A = exp( - ( product(|x_j - y_j|) ) ** (1/n) )

    where:
        x_j and y_j are paired values from two lists,
        n is the number of values,
        d(x_j, y_j) = |x_j - y_j|
    """

    def __init__(self, zero_handling="epsilon", epsilon=1e-12):
        self.zero_handling = zero_handling
        self.epsilon = epsilon

    def calculate(self, first_list, second_list):
        first = np.asarray(first_list, dtype=float)
        second = np.asarray(second_list, dtype=float)

        if len(first) != len(second):
            raise ValueError("Both lists must have the same length.")

        if len(first) == 0:
            raise ValueError("Input lists cannot be empty.")

        differences = np.abs(first - second)

        if self.zero_handling == "epsilon":
            differences = np.where(differences == 0, self.epsilon, differences)

        elif self.zero_handling == "keep":
            pass

        else:
            raise ValueError("zero_handling must be either 'epsilon' or 'keep'.")

        n = len(differences)

        product_term = np.prod(differences)
        geometric_difference = product_term ** (1 / n)

        A = np.exp(-geometric_difference)

        return A
