Title: PySB v1.17.0 Released
Date: 2026-02-17
Category: news
Tags: pysb-release
Slug: pysb-v1-17-0-released

This version of PySB is compatible with Python 3.11+.

## Improvements

* Fix installation, dot compatibility and remove leftover distutils code by [@FFroehlich](https://github.com/FFroehlich) in [#608](https://github.com/pysb/pysb/pull/608)
* PySB now supports numpy 2.0  - Adapt to numpy 2.0 by [@bgyori](https://github.com/bgyori) in [#595](https://github.com/pysb/pysb/pull/595)
* Enable pattern matching with compartments by [@FFroehlich](https://github.com/FFroehlich) in [#570](https://github.com/pysb/pysb/pull/570)
* Support PyBioNetGen provided BNGPATH by [@FFroehlich](https://github.com/FFroehlich) in [#600](https://github.com/pysb/pysb/pull/600)
* Support for explicit time dependency in expressions by [@FFroehlich](https://github.com/FFroehlich) in [#601](https://github.com/pysb/pysb/pull/601)

## Other changes

* Disable GitHub Actions fail-fast by [@jmuhlich](https://github.com/jmuhlich) in [#587](https://github.com/pysb/pysb/pull/587)
* fix: CI failures with updated BNG/NFsim by [@alubbock](https://github.com/alubbock) in [#589](https://github.com/pysb/pysb/pull/589)
* Switch MacOS CI runner to ARM by [@jmuhlich](https://github.com/jmuhlich) in [#588](https://github.com/pysb/pysb/pull/588)
* Resolve test failures caused by NumPy update by [@FFroehlich](https://github.com/FFroehlich) in [#603](https://github.com/pysb/pysb/pull/603)

**Full Changelog**: https://github.com/pysb/pysb/compare/v1.16.0...v1.17.0
