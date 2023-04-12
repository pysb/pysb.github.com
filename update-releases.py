from __future__ import unicode_literals
import json
import dateutil.parser
import os
import re

RELEASE_URL = 'https://api.github.com/repos/pysb/pysb/releases'
RELEASE_TEMPLATE = '''Title: PySB {tag_name} Released
Date: {release_date}
Category: news
Tags: pysb-release
Slug: pysb-{tag_slug}-released

{release_notes}
'''
TARGET_FILENAME = 'content/pysb-{}-released.md'

try:
    # Python 3
    from urllib.request import urlopen
    with urlopen(RELEASE_URL) as rel:
        data = json.loads(rel.read().decode())
except ImportError:
    # Python 2
    import urllib
    rel = urllib.urlopen(RELEASE_URL)
    data = json.loads(rel.read())
    rel.close()

for release in data:
    tgt_filename = TARGET_FILENAME.format(release['tag_name'][1:])
    if os.path.exists(tgt_filename):
        print('Skipping release {}, file exists'.format(release['tag_name']))
        continue

    release_notes = release['body']

    if release_notes.strip() == '':
        release_notes = 'PySB {} has been released'.format(release['tag_name'])

    release_date = dateutil.parser.parse(release['published_at'])
    page = RELEASE_TEMPLATE.format(
        tag_name=release['tag_name'],
        tag_slug=release['tag_name'].replace('.', '-'),
        release_date=release_date.isoformat()[0:10],
        release_notes=release_notes
    )
    # Hyperlink usernames
    page, _ = re.subn('(\s+)@(\w+)', '\\1[@\\2](https://github.com/\\2)', page)
    # Hyperlink to github PRs
    page, _ = re.subn('https://github.com/pysb/pysb/pull/(\d+)', '[#\\1](https://github.com/pysb/pysb/pull/\\1)', page)
    page, _ = re.subn('(\s+)#(\d+)', '\\1[#\\2](https://github.com/pysb/pysb/pull/\\2)', page)

    with open(tgt_filename, 'w') as f:
        f.write(page)

    print('Release notes for {} created'.format(release['tag_name']))
