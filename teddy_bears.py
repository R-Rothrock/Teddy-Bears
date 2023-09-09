#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Author: Roan Rothrock

Description: Small script I made to calculate the usage and effect of teddy

bears in the game Risk of Rain 2.
"""

from functools import partial
import math

import matplotlib.pyplot as plt
import numpy as np

def hyperbolic_stack(percentage: int, denominator: int, iters: int) -> list:
    fraction = percentage/denominator
    while iters > 0:
        yield percentage
        diff = denominator - percentage
        percentage += diff * fraction
        iters -= 1

def round_2(nr: float) -> float:
    # please ignore how horrible this looks.
    return float("%.2f" % round(nr, 2))

def line_graph_series(series: list, title: str = "Series",
                      x_label: str = "x", y_label: str = "y"):
    x = range(0, len(series))
    y = series

    plt.figure(figsize=(5,10))
    plt.plot(x, y)
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.grid()
    plt.yticks(np.arange(min(y), max(y)+1, 5.0))
    plt.show()

if __name__ == "__main__":
    base_percentage   = 15

    denominator  = 100
    iterations   = 35

    #for i in hyperbolic_stack(base_percentage, denominator, iterations):
    #    print(str(round_2(i)))

    line_graph_series(list(hyperbolic_stack(base_percentage, denominator,
                                       iterations)),
                      title="Teddy Bear Effectiveness", x_label="Teddy bears",
                      y_label="Effectiveness")
