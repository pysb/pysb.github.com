Title: PySB v1.13.0 Released
Date: 2021-06-02
Category: news
Tags: pysb-release
Slug: pysb-v1-13-0-released

# Removed features

* Remove pure-python exporter ([#543](https://github.com/pysb/pysb/pull/543)). The pure Python exporter was a legacy feature to export a PySB model for use without PySB itself. We recommend using a virtual environment or container as a better alternative (e.g. Ananconda, Docker). Users requiring this feature who cannot use alternatives could copy/paste the exporter code and use it standalone, or use PySB v1.12 for the export process.

# Improvements

* Docs: make readthedocs fail on warning ([#545](https://github.com/pysb/pysb/pull/545))
* Improve documentation on MatchOnce keyword ([#538](https://github.com/pysb/pysb/pull/538))

# Bug fixes

* Docs: Fix sphinx mocks, include JSON export ([#544](https://github.com/pysb/pysb/pull/544))
* Fix altered matplotlib API call ([#541](https://github.com/pysb/pysb/pull/541))
* Fix Anaconda download link in docs ([#542](https://github.com/pysb/pysb/pull/542))
