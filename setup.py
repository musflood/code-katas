from setuptools import setup

setup(
    name='code-katas',
    package_dir={'': '.'},
    py_modules=['sum_terms, social_golfers, persistent_bugger'],
    author='Megan Flood',
    author_email='mak.flood@comcast.net',
    description='Solutions to kata from Code Wars with the relevant tests.',
    install_requires=[],
    extras_require={'test': ['pytest', 'tox']},
)
