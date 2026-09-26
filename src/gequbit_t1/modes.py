import numpy as np
from .core import bose_occupation, phonon_wavevector, gaussian_form_factor

def acoustic_mode_factor(omega_rad_s, temperature_k, sound_velocity_m_s, confinement_length_m):
    q = phonon_wavevector(omega_rad_s, sound_velocity_m_s)
    ff = gaussian_form_factor(q, confinement_length_m)
    thermal = bose_occupation(omega_rad_s, temperature_k) + 1.0
    return float(ff**2 * thermal)

def total_rate(mode_rates_s_inv):
    rates = np.asarray(mode_rates_s_inv, float)
    if np.any(rates < 0):
        raise ValueError("mode rates must be nonnegative")
    return float(np.sum(rates))
