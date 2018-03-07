Title: PySB v1.6.0 Released
Date: 2018-03-07
Category: news
Tags: pysb-release

# New Features

* New reversible rule operator `|`; the previous `<>` operator is now pending deprecation (#309)
* Saving and loading of `SimulationResult` objects with metadata in HDF5 format (#292)
* PySB now supports Kappa 4, including custom rate laws with PySB `Expression`s. Kappa 3 support has been dropped (#334)
* Rule pattern matching and new model test suite (#285)
* Model components can now be accessed as attributes (#213)
* Importing models from BioModels can now use either the EBI mirror (default) or the CalTech one (#325)
* Cython support for `ScipyOdeSimulator`; this allows efficient simulation on Python 3, where `weave` is no longer an option (#320)

# General Improvements

* Native Python 3 compatibility for the whole PySB codebase (#312)
* Internal species for tracking synthesis/degradation rules `__source` and `__sink` have been removed (#317)
* Specifying a pattern with a dangling bond now causes an error (#328)
* Simulator `run()` arguments are no longer persistent (#314)
* State values in patterns are now verified (#322)
* Frequently Asked Questions added to documentation (#331)
* Loading `CupSodaSimulator` no longer initializes the GPU on import; instead it wait until instantiation (#332).
* `pysb.tools.sensitivity_analysis` code updated for compatibility with matplotlib 2.1 (#303)
* Improvements to `ScipyOdeSimulator`'s `weave` interface, including better control of console output (#299) and ensuring C code is cacheable when unicode variable names are used (#301).
* Graph objects in the Kappa interface (e.g. contact maps) are now returned as `networkx` graphs, not `pygraphviz`. `pygraphviz` support for reading .dot files in the Kappa interface has been replaced with `pydot` (#335).

# Bugfixes

* Fix component rename when not using Self Exporter (#321)
* `ComplexPattern.__call__` now raises a `DuplicateMonomerError` when duplicate monomers are present (#323)
* Fixes for `ComplexPattern.is_concrete()` (#307)
* Reversible `Rule.is_synth()` and `is_deg()` now work for reversible patterns (#326)
* Fix error when running Tyson model with `CupSodaSimulator` (#332)
