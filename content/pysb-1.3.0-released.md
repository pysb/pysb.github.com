Title: PySB v1.3.0 Released
Date: 2017-03-24
Category: news
Tags: pysb-release

# New features
- CupSodaSimulator, a wrapper for the [cupSODA](https://github.com/aresio/cupSODA) GPU-based ODE integrator. No special Python libraries are necessary since cupSODA comes as a standalone binary, but if PyCUDA is installed then PySB can auto-detect the configuration details of your GPU. See the documentation in `pysb.simulator.CupSodaSimulator` for more.
- Simulators can now support multiple parameter sets and/or initial condition sets, especially helpful for internally parallel simulators such as CupSodaSimulator.
- PySB internals now use the `logging` module to emit diagnostics, making debugging (or silencing output) easier. This is exposed externally through the `PYSB_LOG` environment variable -- set it to one of the standard logging levels (DEBUG, INFO, etc.) to control which messages are printed.

# Bugfixes
- BNGL and SBML importers now work on Windows.
- Observables and Expressions with unicode objects for names (rather than strings) no longer trigger an internal numpy exception in the PySB Simulator code on Python 2. An exception will still be raised if the unicode names do contain non-ascii-safe characters, but the error message is now more intelligible.
