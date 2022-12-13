import numpy as np


np.random.seed(42)

# Version 1: complicated sin thing.
a = 0.2
b = 5
c = 3
d = 0.1
meas_t = np.sort(np.append(
    np.random.uniform(0, 3.8, 57),
    np.random.uniform(8, 20, 250),
))  # The input coordinates must be sorted
yerr = np.random.uniform(0.08, 0.22, len(meas_t))
meas_y = a * (meas_t-b) + np.sin(c*meas_t + d*(meas_t-b)**2) + yerr * np.random.randn(len(meas_t))

true_t = np.linspace(0, 20, 100)
true_y = a * (true_t-b) + np.sin(c*true_t + d*(true_t-b)**2)


true_vals = np.vstack((true_t, true_y))
np.save("true_vals.npy", true_vals)

meas_vals = np.vstack((meas_t, meas_y, yerr))
np.save("meas_vals.npy", meas_vals)