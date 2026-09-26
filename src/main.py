"""Illustrative acoustic-phonon spectral-density relaxation model; not a material prediction."""
import argparse
import math

HBAR = 1.054571817e-34
MU_B = 9.2740100783e-24

def rate(field_t, g_eff, branches):
    """Return rates in s^-1 for (velocity m/s, prefactor s^2, cutoff rad/s).
    Model: Gamma_j = A_j omega^3 exp[-(omega/omega_c,j)^2]/v_j^3.
    A_j absorbs coupling and normalization; it MUST be calibrated separately.
    """
    if field_t < 0 or g_eff <= 0:
        raise ValueError("Require field >= 0 and g_eff > 0")
    omega = g_eff * MU_B * field_t / HBAR
    result = {}
    for name, velocity, strength, cutoff in branches:
        if velocity <= 0 or strength < 0 or cutoff <= 0:
            raise ValueError("Invalid branch parameters")
        result[name] = strength * omega**3 * math.exp(-(omega/cutoff)**2) / velocity**3
    return result

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--g", type=float, default=1.2)
    parser.add_argument("--field", type=float, nargs="+", default=[0.02, 0.05, 0.1, 0.2])
    args = parser.parse_args()
    branches = [("LA", 5400., 1e-14, 8e11), ("TA", 3500., 3e-15, 5e11)]
    print("B_T,frequency_GHz,LA_s-1,TA_s-1,T1_s")
    for b in args.field:
        rates = rate(b, args.g, branches)
        frequency = args.g * MU_B * b / (2 * math.pi * HBAR) / 1e9
        total = sum(rates.values())
        print(f"{b:.6g},{frequency:.6g},{rates['LA']:.6g},{rates['TA']:.6g},{1/total if total else math.inf:.6g}")

if __name__ == "__main__":
    main()
