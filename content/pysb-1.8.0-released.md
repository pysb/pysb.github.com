Title: PySB v1.8.0 Released
Date: 2018-10-19
Category: news
Tags: pysb-release

# New Features

* Model component names will now tab-complete when accessed as part of a ComponentSet ([#380](https://github.com/pysb/pysb/pull/380)

# General Improvements

* Keyword arguments to `__init__` are now validated by `ScipyOdeSimulator` ([#381](https://github.com/pysb/pysb/pull/381)), `StochKitSimulator` ([#382](https://github.com/pysb/pysb/pull/382)), and `CupSodaSimulator` ([#383](https://github.com/pysb/pysb/pull/383))
* BioNetGen: Extra functions are now supported, including `And`, `Or`, `Floor`, `Ceiling`, `Min`, `Max`, `Abs`, and the constants `pi` and `e` ([#373](https://github.com/pysb/pysb/pull/373))
* SBML exporter: Observables and Expressions are now set by AssignmentRules ([#370](https://github.com/pysb/pysb/pull/370) and [#372](https://github.com/pysb/pysb/pull/372)) 

# Bugfixes

* Fix Simulator initials_dict when set by array ([#377](https://github.com/pysb/pysb/pull/377))
* Fix BNGSimulator when tspan doesn't start at 0 ([#379](https://github.com/pysb/pysb/pull/379))
* Set a default module name for components when `__name__` isn't set ([#374](https://github.com/pysb/pysb/pull/374))
* Fix StochKit export on Python 3 when lxml is installed ([#375](https://github.com/pysb/pysb/pull/375))
* Fix serialization of components that do not have a model weakref set ([#386](https://github.com/pysb/pysb/pull/386))
* Respect `BngSimulator` cleanup flag in `__init__` ([#385](https://github.com/pysb/pysb/pull/385))
