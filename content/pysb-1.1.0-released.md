Title: PySB v1.1.0 Released
Date: 2016-04-21
Category: news
Tags: pysb-release

PySB has officially adopted semantic versioning. This means v1.1.0 includes new features as compared to v1.0.x, but is still backwards compatible so you won't have to change any of your models to upgrade to it.

# New features
* Full Python 3 compatibility. All tests pass under Python 3.4 and 3.5.
* BioNetGen 2.2.6 support, and a new API for interfacing with BioNetGen which can execute any BioNetGen commands and operate in batch or interactive mode. The old run_ssa function is still available.
* BioNetGen temporary files are now created in system temporary directories by default.
* Kappa 4.0 support, and a new API here as well. The old run_simulation, contact_map, and influence_map functions are still available. The Kappa install location is now configurable via the KAPPAPATH environment variable. Note that Kappa 4.0 hasn't yet been released, so until it is you will need to use the development version from the Kappa GitHub repository at https://github.com/Kappa-Dev/KaSim.
* Support for models without initial conditions, provided there’s at least one zero-order synthesis rule present, e.g. `Rule(‘Rule1’, None >> A(), Parameter(‘ksynth’, 1))`
* Automatic analytical Jacobian generation in the ODE solver. PySB can now optionally calculate a closed-form expression for the Jacobian of a model's ODEs which can help speed up the solver in some cases.
* pysb_flat exporter which serializes a model to Python/PySB code which can be saved to a file and imported again later. We found this useful for writing out dynamically generated models as "native" PySB model code. The code is just a straight list of all the component definitions so macro calls etc. are lost.

# Other stuff
* Package installation now uses setuptools instead of distutils.
* We are now publishing coverage testing results at https://coveralls.io/github/pysb/pysb .
* Documentation of the PySB requirements and installation procedure has been improved significantly.
* Numerous bugfixes. We will try to be more explicit about enumerating these in future releases.
