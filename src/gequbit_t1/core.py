import numpy as np

HBAR_J_S = 1.054571817e-34
KB_J_K = 1.380649e-23

def bose_occupation(omega_rad_s, temperature_k):
    if omega_rad_s < 0 or temperature_k < 0:
        raise ValueError("omega and temperature must be nonnegative")
    if temperature_k == 0:
        return 0.0
    x = HBAR_J_S * omega_rad_s / (KB_J_K * temperature_k)
    if x > 700:
        return 0.0
    return 1.0 / np.expm1(x)

def phonon_wavevector(omega_rad_s, sound_velocity_m_s):
    if omega_rad_s < 0 or sound_velocity_m_s <= 0:
        raise ValueError("invalid omega or sound velocity")
    return omega_rad_s / sound_velocity_m_s

def gaussian_form_factor(q_m_inv, confinement_length_m):
    if confinement_length_m <= 0:
        raise ValueError("confinement length must be positive")
    q = np.asarray(q_m_inv, float)
    return np.exp(-0.25 * (q * confinement_length_m) ** 2)

def power_law_relaxation_rate(B_t, prefactor_s_inv_t_pow, exponent, temperature_factor=1.0):
    if B_t < 0 or prefactor_s_inv_t_pow < 0 or temperature_factor < 0:
        raise ValueError("inputs must be nonnegative")
    return prefactor_s_inv_t_pow * B_t ** exponent * temperature_factor

def t1_from_rate(rate_s_inv):
    r = np.asarray(rate_s_inv, float)
    if np.any(r < 0):
        raise ValueError("rate must be nonnegative")
    return np.where(r == 0, np.inf, 1.0 / r)
