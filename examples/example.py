import numpy as np
from gequbit_t1.core import bose_occupation, phonon_wavevector, gaussian_form_factor

omega = 2*np.pi*5e9
T = 0.05
v = 5000.0
q = phonon_wavevector(omega, v)
print("Bose occupation:", bose_occupation(omega, T))
print("q [1/m]:", q)
print("form factor:", gaussian_form_factor(q, 20e-9))
