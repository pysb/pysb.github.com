Title: PySB's Python version support policy
Date: 2019-09-24
Category: news
Tags: policies

PySB will support Python 2.7 until January 1, 2020. After that date, PySB's
major version number will be incremented (PySB 2.x). From PySB 2.x onward,
our policy will be to support the three most recent minor versions of Python
(most likely Python 3.6, 3.7, and 3.8 at time of PySB 2.x release).

Upon a new major release of Python, the PySB major version will
be incremented and its support for the previous Python major version will
cease immediately. The previous PySB release will go into Long-Term Support
(LTS) mode, receiving only critical bug fixes while retaining support for
the previous Python release. LTS releases will be maintained for 2 years.

## Background

Python 2.7 will itself become unsupported from January 1, 2020, as per
[PEP 373](https://www.python.org/dev/peps/pep-0373/), therefore our
decision to end Python 2.7 support is in line with this.

We want a Python version support policy that strikes a balance between
taking advantage of new Python features and providing stability.
On the current Python release cycle, support for new versions would last
around five years, which we feel is a reasonable length of time.

We hope this policy helps to provide clarity to PySB users. If you
have comments or questions regarding this policy, please raise them
on the relevant [GitHub issue](https://github.com/pysb/pysb/issues/463).
Support is also available on our
[Gitter chat room](https://gitter.im/pysb/pysb).

-- The PySB Development Team
