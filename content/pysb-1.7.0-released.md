Title: PySB v1.7.0 Released
Date: 2018-07-23
Category: news
Tags: pysb-release

# New Features

* Python 3.7 now officially supported (in addition to 3.6 and 2.7) (#368)
* Filtering for ComponentSets ([documentation](https://pysb.readthedocs.io/en/stable/modules/core.html#pysb.core.ComponentSet.filter)) (#340)
* SBML export now uses [LibSBML](https://pypi.org/project/python-libsbml/) and supports compartments and expressions (#367)
* On demand observable trajectories without adding them to the model ([documentation](https://pysb.readthedocs.io/en/stable/modules/simulator.html#pysb.simulator.SimulationResult.observable)) (#337)

# General Improvements

* The `<>` operator for reversible rules in Python 2.7 has been formally deprecated. Use `|` instead (#344)
* Products of synthesis rules are enforced to be concrete (#354)
* Monomers' site and state names are validated upon definition (#352)
* Expressions now must be created from sympy.Expr. Previously, unwrapped integers and floats were accepted (#350)
* Capture BNG errors into PySB exception messages (#363)
* Show line numbers in the debug log for BioNetGen language files to aid interpreting BNG error messages (#365)
* Python model exporter now produces Python 3.x compatible code (#366)
* Recover from non-functional Cython/weave compilers on Windows (#353)
* Better tests for PySB exporters, and explicit `ExpressionsNotSupported` and `CompartmentsNotSupported` exceptions where applicable (#357)

# Bugfixes

* Fix export to BNG of expressions containing `log` (#361)
* Fix Kappa export when using parameters with overlapping (substring) names (#346)
