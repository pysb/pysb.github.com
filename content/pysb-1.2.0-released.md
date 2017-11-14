Title: PySB v1.2.0 Released
Date: 2016-10-07
Category: news
Tags: pysb-release

# New features
*Brand new Simulator classes and SimulationResult classes in the 
`pysb.simulator` package. The old `pysb.integrate` API is unchanged but has been
 reimplemented using the Simulator class.
* Model import from other types of models in the `pysb.importers` package. 
Currently supports BNGL and SBML model import.

# Bugfixes
* pysb_flat exporter now supports `MatchOnce`.
* Some Python 2 Unicode issues were addressed by eliminating uses of 
`type(...) == str`.
