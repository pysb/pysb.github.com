Title: PySB v1.5.0 Released
Date: 2017-08-19
Category: news
Tags: pysb-release

# New features
`BngSimulator`, an interface to all simulators provided by BioNetGen: ODE, partitioned-leaping, SSA (stochastic) and NFsim (network-free stochastic). See `pysb.simulator.bng.BngSimulator` (#272).

# General improvements
* Faster and more memory-efficient construction of ODEs from rules (#293).
* `ScipyOdeSimulator` is faster in "pure Python" mode (i.e. without `weave` and a C compiler installed). It now also supports a somewhat broader range of sympy expressions in reaction rates. Also an experimental `use_theano` option has been added which uses [theano](http://deeplearning.net/software/theano/) rather than [weave](https://github.com/scipy/weave) for evaluating differential equation expressions. Note that PySB users who previously depended on `scipy.weave` for fast C translation of ODE expressions must now install the standalone `weave` package, as this module has been removed from scipy (#294).
* `StochKitSimulator` adds support for models with expressions. Also the simulation setup process is now faster.
* Performance benchmarking and regression testing with Airspeed Velocity (#275). We will eventually work out a way to automatically execute the test suite and publish the results, but for now anyone who's interested in this would have to run it themselves.
* Continuous Integration for Windows with AppVeyor (#263).

# Bugfixes
* Accessing `SimulationResult.all` no longer crashes when `unicode` strings are used for observable or expression names under Python 2 (#291, issue #290). We thought we fixed the whole unicode-and-numpy issue here back in #245, but apparently we missed a spot.
* `MatlabExporter` now correctly handles empty observables, i.e. observables whose pattern doesn't match any reachable species (#289).
* Some code errors in the tutorial (module/class names that didn't get updated during a code refactoring) have been corrected (#286). Thanks to Michael Retchin for catching this.
