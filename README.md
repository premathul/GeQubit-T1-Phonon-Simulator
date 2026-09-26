# GeQubit-T1-Phonon-Simulator

GeQubit-T1-Phonon-Simulator is a research-oriented Python project for modeling spin relaxation in germanium hole-spin qubits when the dominant decay channel is coupling to acoustic phonons. The purpose of the repository is to make the structure of a (T_1) calculation transparent: the qubit energy splitting determines the emitted phonon frequency, the phonon branch determines the wave vector and density of states, the orbital wavefunction determines the form factor, and the spin-orbit or deformation-potential matrix element determines how strongly the qubit couples to that mode. The present code provides a compact starting point for these ingredients and is designed to evolve toward a quantitatively calibrated relaxation model.

For a qubit transition of angular frequency (omega_q), Fermi's golden rule gives a generic relaxation rate
[
Gamma_1=rac{2pi}{hbar}sum_{lambda,mathbf q}
|langle f|H_{mathrm{int}}|iangle|^2
delta(hbaromega_{lambdamathbf q}-hbaromega_q)
left[n_B(omega_q,T)+1ight].
]
The lifetime is (T_1=1/Gamma_1). The current implementation does not claim to provide a complete microscopic Ge hole-phonon Hamiltonian; instead it provides explicit building blocks for Bose occupation, acoustic-phonon dispersion, phonon wave vectors, Gaussian orbital form factors, and power-law relaxation models useful for benchmarking and method development.

The repository is intended to be used alongside detailed device simulations. A future high-fidelity workflow will take Zeeman splittings, orbital states, spin-orbit admixture, and material parameters from a Ge/SiGe device model, then evaluate longitudinal and transverse acoustic-phonon channels separately. This will make it possible to study magnetic-field scaling, field-angle dependence, confinement dependence, and the crossover between low-temperature spontaneous emission and finite-temperature stimulated processes.

Installation is performed with
```bash
git clone https://github.com/premathul/GeQubit-T1-Phonon-Simulator.git
cd GeQubit-T1-Phonon-Simulator
python -m pip install -e .
```
and the test suite can be run with
```bash
python -m pip install -e .[dev]
pytest -q
```.

The current code should be interpreted as a transparent research foundation rather than a publication-ready (T_1) predictor. Quantitative predictions require experimentally or independently validated deformation potentials, sound velocities, mass density, orbital form factors, spin-orbit matrix elements, and the correct multiband hole-state structure. The project will progressively add those layers while retaining simple analytical limits for validation.

## Runnable scientific baseline

The executable baseline maps a chosen magnetic field to a Zeeman angular frequency using ħω = g_eff μ_B B. For each acoustic branch it evaluates an illustrative cubic spectral density multiplied by a Gaussian high-frequency cutoff. The LA and TA terms are displayed separately so that changes in assumed sound velocity and branch strength remain visible. The prefactors in the example are placeholders with units chosen to produce rates in inverse seconds; they are not measured germanium deformation potentials. Replacing them with microscopic coupling requires a normalized orbital form factor, crystal orientation, phonon polarization, density of states, and the actual spin-admixed matrix element.

Run `python src/main.py --g 1.2 --field 0.02 0.05 0.1`. The output includes magnetic field in tesla, Zeeman frequency in gigahertz, individual rates in inverse seconds, and the reciprocal total rate in seconds. The reciprocal is meaningful only within the specific phenomenological model and assumed branch parameters. A physical comparison to experiment also needs all competing relaxation channels and the temperature-dependent absorption terms.

## Validation and scope

The calculations in `src/main.py` are transparent baseline models intended for reproducibility and extension. Inputs and assumptions should be reported alongside outputs; numerical agreement with a plotted trace alone does not validate a material-specific prediction. New physical terms should be accompanied by dimensional checks and independent limiting-case comparisons.

## Contact

**Athul Prem** — [GitHub profile](https://github.com/premathul). For scientific discussion or collaboration, open an issue in this repository or reach out through my GitHub profile.
