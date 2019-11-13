Title: PySB v1.11.0 Released
Date: 2019-11-13
Category: news
Tags: pysb-release
Slug: pysb-v1-11-0-released

# New features

* JSON model import and export ([#469](https://github.com/pysb/pysb/pull/469))

# Improvements

* Models stored in HDF5 files using `SimulationResult.save()` now use JSON, rather than pickle
* Raise a `ValueError` if a rule defined with reverse rate, but expression is not reversible ([#471](https://github.com/pysb/pysb/pull/471))

# Bug fixes

* Fixes for importing certain BNGL and SBML models which previously failed to import ([#470](https://github.com/pysb/pysb/pull/470))
* Fix `SimulationResult.load()` for HDF5 files saved with PySB <1.10, which gave a pickle error when loading on PySB 1.10. Such HDF5 files should be re-saved in order to use the new JSON model format, which should be more durable across PySB versions.
