import numpy as np
from gequbit_t1.core import bose_occupation, phonon_wavevector, gaussian_form_factor, t1_from_rate

def test_zero_temperature_bose():
    assert bose_occupation(1e10, 0.0) == 0.0

def test_q_relation():
    assert np.isclose(phonon_wavevector(100.0, 10.0), 10.0)

def test_form_factor_bounds():
    assert 0 < gaussian_form_factor(1e7, 1e-8) <= 1

def test_t1_inverse():
    assert np.isclose(t1_from_rate(4.0), 0.25)
