Title: PySB v1.12.0 Released
Date: 2021-03-17
Category: news
Tags: pysb-release
Slug: pysb-v1-12-0-released

This version of PySB supports Python 3.6-3.9. Python 2.7 is no longer supported.

# New features

* Implement reversible synthesis rules ([#499](https://github.com/pysb/pysb/pull/499))

# Improvements

* ScipyOdeSimulator speedup through refactoring, use of partial ([#531](https://github.com/pysb/pysb/pull/531), [#483](https://github.com/pysb/pysb/pull/483))
* Use double precision for BNG and Kappa parameters ([#490](https://github.com/pysb/pysb/pull/490))
* Allow constant expressions for compartment sizes ([#525](https://github.com/pysb/pysb/pull/525))
* Faster SimulationResult loading: use slices ([#491](https://github.com/pysb/pysb/pull/491))
* Implement BNG boolean treatment within expressions, e.g. evaluate `(2 > 1)` as `True` ([#494](https://github.com/pysb/pysb/pull/494))
* Import ABC from collections.abc instead of collections for Python 3.9 compatibility ([#485](https://github.com/pysb/pysb/pull/485))
* Implement the assumption that all symbolic variables in a model only take real values. The user can specify integer and non-negative enforced assumptions about parameter values. Changes are relevant for any simplifications of symbolic expressions in the model ([#475](https://github.com/pysb/pysb/pull/475))
* Update tested Python versions on CI ([#479](https://github.com/pysb/pysb/pull/479))
* Remove weave and theano support from ScipyOdeSimulator ([#482](https://github.com/pysb/pysb/pull/482))
* Remove Python 2 support ([#486](https://github.com/pysb/pysb/pull/486), [#487](https://github.com/pysb/pysb/pull/487))
* Update docs with Python version support ([#492](https://github.com/pysb/pysb/pull/492))
* Update docs with stubs on calibration and PySB modules to tutorial ([#509](https://github.com/pysb/pysb/pull/509))
* Update deprecated pandas call in CupSodaSimulator ([#523](https://github.com/pysb/pysb/pull/523))
* Remove deprecated sympy.boolalg calls ([#526](https://github.com/pysb/pysb/pull/526))
* Specify Python>=3.6 requirement in setup.py ([#536](https://github.com/pysb/pysb/pull/536))

# Bug fixes

* Fix sympy 1.6 compatibility ([#505](https://github.com/pysb/pysb/pull/505))
* Fix observable trajectories on HDF5 load ([#502](https://github.com/pysb/pysb/pull/502))
* Fix reading of error messages from cupSODA ([#510](https://github.com/pysb/pysb/pull/510))
* Fix SBML export with unset compartment size ([#513](https://github.com/pysb/pysb/pull/513))
* Fix eqn_mode='python' for models with local functions ([#495](https://github.com/pysb/pysb/pull/495))
* Fix typehints in core ([#507](https://github.com/pysb/pysb/pull/507), [#520](https://github.com/pysb/pysb/pull/520))
* Fix BNG code generation for `Eq` and `Ne` ([#528](https://github.com/pysb/pysb/pull/528))
* Fix StochKit export of certain PySB rate Expressions ([#521](https://github.com/pysb/pysb/pull/521))
* Copy annotations when creating model from base ([#493](https://github.com/pysb/pysb/pull/493))
* Fix SimulationResult loads when `include_obs_exprs=True` and model has no observables or expressions ([#481](https://github.com/pysb/pysb/pull/481))
* Fix an error when using ScipyOdeSimulator with the num_processors
option >1 (i.e. use multiprocessing) together with compiler='python' ([#480](https://github.com/pysb/pysb/pull/480))
* Fix usage of super in multiple inheritance of sympy.Symbol ([#474](https://github.com/pysb/pysb/pull/474))
* Fix readthedocs error with updated mock ([#489](https://github.com/pysb/pysb/pull/489))
* Fix slice IndexError in tutorial ([#529](https://github.com/pysb/pysb/pull/529))
* Fix tutorial typos ([#511](https://github.com/pysb/pysb/pull/511))
* Fix DeprecationWarning leading to test failure with new versions of h5py ([#537](https://github.com/pysb/pysb/pull/537))
