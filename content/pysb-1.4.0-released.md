Title: PySB v1.4.0 Released
Date: 2017-06-09
Category: news
Tags: pysb-release

# New features
- `StochKitSimulator`, an interface to the stochastic simulator [StochKit](https://github.com/StochSS/StochKit). See `pysb.simulator.stochkit.StochKitSimulator`.
- `InitialsSensitivity`, a tool to perform pairwise sensitivity analysis of initial conditions. See `pysb.tools.sensitivity_analysis.InitialSensitivity`. **EXPERIMENTAL**.
- Import models directly from BioModels from just their ID (BIOMDxxx... or MODELxxx...) with `pysb.importers.sbml.model_from_biomodels()`.

# General improvements
- Faster simulation runs for models with many expressions (~60x speedup for a 200-expression model).
- Improved accuracy and better error reporting when parsing SBML expressions in `pysb.importers.sbml`.
- The Kappa interface has been upgraded to support Kappa version 4. This also means Kappa v3 is no longer supported.

# Bugfixes
- `CupSodaSimulator` now works on Python 3.
- Simulators now fully respect parameter value overrides for initial condition parameters (#252).
- Simulators now allow overriding a non-zero initial condition to zero (#251).
- Simulators no longer have problems with parameter names that are unicode objects (still only ASCII characters are allowed, though) (#278).
- Model components with the same name as a top-level sympy object (anything you would see in `from sympy import *`) no longer cause errors when simulating (#259).
- Applying a compartment condition to a MonomerPattern that already has one now correctly raises an exception (#258).
- `PysbFlatExporter` now works with compartments using inline size declarations (#210).
- `ComplexPattern.is_equivalent_to` now correctly handles certain combinations of compartments that were previously mishandled (#257).
