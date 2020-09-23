# Test Bland-Altman

from bland_altman import bland_altman_plot
import numpy as np
import matplotlib.pyplot as plt

%matplotlib inline
# Seed the random number generator.
# This ensures that the results below are reproducible.
np.random.seed(9999)
m1 = np.random.random(20)
m2 = np.random.random(20)

f, ax = plt.subplots(1, figsize =(8,5))
my_bland_altman_plot = bland_altman_plot(m1, m2, ax = ax)
f.savefig('bland-altman-plot.png')
