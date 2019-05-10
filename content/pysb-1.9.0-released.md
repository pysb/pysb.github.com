Title: PySB v1.9.0 Released
Date: 2019-05-10
Category: news
Tags: pysb-release

# New Features

* `MultiState` capability, which enables a single `Monomer` site to be specified with multiple states ([documentation](https://pysb.readthedocs.io/en/stable/modules/core.html#pysb.core.MultiState)) ([#410](https://github.com/pysb/pysb/pull/410))
* `ScipyOdeSimulator` multiprocessing capability, using `n_processors` argument ([documentation](http://docs.pysb.org/en/stable/modules/simulator.html#pysb.simulator.ScipyOdeSimulator.run)) ([#395](https://github.com/pysb/pysb/pull/395))
* Multi-GPU simulations and chunking support (split large simulation sets into GPU-sized blocks) for `CupSodaSimulator` ([#409](https://github.com/pysb/pysb/pull/409))
* Sensitivity analysis class can now work for model parameter sweeps, in addition to initial conditions ([documentation](https://pysb.readthedocs.io/en/stable/modules/tools/sensitivity_analysis.html)) ([#426](https://github.com/pysb/pysb/pull/426))
* Support for fixed concentration species ([#364](https://github.com/pysb/pysb/pull/364))
* Initial condition and parameter sets can now be supplied to Simulator instances as Pandas DataFrames ([#416](https://github.com/pysb/pysb/pull/416))
* Drug binding macro `pysb.macros.drug_binding()` ([documentation](https://pysb.readthedocs.io/en/stable/modules/macros.html#pysb.macros.drug_binding)) ([#387](https://github.com/pysb/pysb/pull/387))
* Support `BngSimulator` early stopping using `stop_if` kwarg (example: `sim.run(stop_if='ObsA>9')`) ([#407](https://github.com/pysb/pysb/pull/407))
* BioNetGen importer improvements, including preserving parameter depdendencies in expressions, the `MoveConnected` keyword, and Observables' species compartments ([#406](https://github.com/pysb/pysb/pull/406))

# Improvements

* `ScipyOdeSimulator` is now faster when using Cython due to customized compiler directives ([#403](https://github.com/pysb/pysb/pull/403))
* When model components experience a validation error on creation, they're no longer added to the model by the `SelfExporter` ([#431](https://github.com/pysb/pysb/pull/431))
* Use the system `PATH` variable to help find external tools like BioNetGen or Kappa ([#389](https://github.com/pysb/pysb/pull/389))
* SBML Exporter: preserve parameter dependency in initial conditions ([#417](https://github.com/pysb/pysb/pull/417)) and specify initial concentrations for all species ([#420](https://github.com/pysb/pysb/pull/420))
* BioNetGen importer now allows relative paths ([#432](https://github.com/pysb/pysb/pull/432))
* StochKit log file contents are now included in error messages ([#429](https://github.com/pysb/pysb/pull/429))
* Clearer error messages when Cython is non-functional on Windows ([#402](https://github.com/pysb/pysb/pull/402))

# Bug fixes

* Corrections to the PySB tutorial ([#422](https://github.com/pysb/pysb/pull/422))
* Fix number of simulations calculation for NFsim ([#445](https://github.com/pysb/pysb/pull/445))
* Fix cupSODA when using models with non-alphanumeric characters ([#404](https://github.com/pysb/pysb/pull/404))
* Fix Exception when calling `expand_obs()` on observables which match no species ([#418](https://github.com/pysb/pysb/pull/418))
* Fix for model name being changed in unit test ([#399](https://github.com/pysb/pysb/pull/399))
* Fix `Model.update_initial_condition_pattern` ([#446](https://github.com/pysb/pysb/pull/446))
* Minor packaging fixes ([#396](https://github.com/pysb/pysb/pull/396), [#411](https://github.com/pysb/pysb/pull/411), [#433](https://github.com/pysb/pysb/pull/433))
* Minor code tidy-ups ([#405](https://github.com/pysb/pysb/pull/405), [#436](https://github.com/pysb/pysb/pull/436))
* Documentation build fixes ([#424](https://github.com/pysb/pysb/pull/424), [#444](https://github.com/pysb/pysb/pull/444))

# Deprecations

* ScipyOdeSimulator's theano backend ([#428](https://github.com/pysb/pysb/pull/428))
