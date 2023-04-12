Title: PySB v1.14.0 Released
Date: 2022-08-29
Category: news
Tags: pysb-release
Slug: pysb-v1-14-0-released

## New features
* Energy modeling by [@jmuhlich](https://github.com/jmuhlich) in [#553](https://github.com/pysb/pysb/pull/553)
  This adds support for BNG's energy modeling formalism. Models can now contain EnergyPatterns as well as energy-based Rules with the Arrhenius rate law parameterized by activation energy (E₀) and rate distribution (φ). Energy-based models can be simulated directly in PySB or exported to BNGL for use with BioNetGen-based tools.
* Add total_rate option to rules for NFsim compatibility by [@rasi](https://github.com/rasi) in [#559](https://github.com/pysb/pysb/pull/559)

## Improvements
* Fix typo in rule in tutorial by [@mustafaozen](https://github.com/mustafaozen) in [#560](https://github.com/pysb/pysb/pull/560)
* Migrate continuous integration to GitHub Actions by [@yukthi](https://github.com/yukthi)-suresh and [@jmuhlich](https://github.com/jmuhlich) in [#562](https://github.com/pysb/pysb/pull/562)

## Bug fixes
* Fix repr() of single-monomer complexes with compartments  by [@alubbock](https://github.com/alubbock) in [#550](https://github.com/pysb/pysb/pull/550)
