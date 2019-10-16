Title: PySB v1.10.0 Released
Date: 2019-10-16
Category: news
Tags: pysb-release

# New features

* Local functions ([#412](https://github.com/pysb/pysb/pull/412), [#464](https://github.com/pysb/pysb/pull/464)) 

  Local functions allow PySB expressions to accept a tagged `MonomerPattern` or `ComplexPattern` as an argument. For example, in the following snippet, `A` synthesizes `C` with rate dependent on bound `B`:

  ```python
  Observable('AB_motif', A(b=1) % B(a=1))
  Tag('x')
  Expression('f_synth', k_synthC * AB_motif(x) ** 2)
  Rule('_R1', A() @ x >> A() @ x + C(), f_synth)
  ```

  See [localfunc.py](https://github.com/pysb/pysb/blob/master/pysb/examples/localfunc.py) for a complete example.

* KappaSimulator ([#447](https://github.com/pysb/pysb/pull/447))

  New simulation interface for Kappa which supports multiple initial condition sets and parameter sets. Replaces `pysb.kappa.run_simulation`. See [KappaSimulator documentation](http://docs.pysb.org/en/stable/modules/simulator.html#pysb.simulator.KappaSimulator) for further details.

# Improvements

* Show `ReusedBondError` when bond connects >2 sites in a reaction pattern ([#466](https://github.com/pysb/pysb/pull/466))
* Add dashed edge when reaction rate is an expression with observables ([#458](https://github.com/pysb/pysb/pull/458))
* Include macros in `rule._function` ([#451](https://github.com/pysb/pysb/pull/451))
* Improved error messages when external tools not found; make Atomizer use `pysb.pathfinder` ([#460](https://github.com/pysb/pysb/pull/460))

# Bug fixes

* Fix reading `MultiState` species from BioNetGen models ([#462](https://github.com/pysb/pysb/pull/462))
* Fix `Expression.get_value()` ([#457](https://github.com/pysb/pysb/pull/457))
* PySBFlatExporter now supports `MultiState` ([#453](https://github.com/pysb/pysb/pull/453))
* Fix `ModelNotDefinedError` when self exporter is used and a model
component is declared before Model() ([#452](https://github.com/pysb/pysb/pull/452))

# Miscellaneous

* Switch from coveralls to codecov ([#454](https://github.com/pysb/pysb/pull/454)) 

