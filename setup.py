from setuptools import setup

setup(
    name='code-katas',
    package_dir={'': '.'},
    py_modules=['sum_terms',
                'social_golfers',
                'persistent_bugger',
                'esolang_ticker',
                'alt_split',
                'dir_reduct',
                'hightest_word',
                'proper-parenthetics',
                'string-pyramid'],
    author='Megan Flood',
    author_email='mak.flood@comcast.net',
    description='Solutions to kata from Code Wars with the relevant tests.',
    install_requires=[],
    extras_require={'test': ['pytest', 'tox']},
)
