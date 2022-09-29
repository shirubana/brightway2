from setuptools import setup

packages = [
    "appdirs",
    "asteval",
    "bw2analyzer<0.10.99",
    "bw2calc==1.8.1",
    "bw2data<3.99",
    "bw2io<0.8.9",
    "bw2parameters>=0.6.5",
    "docopt",
    "eight",
    "flask",
    "future",
    "lxml",
    "numpy",
    "peewee>=3.0",
    "psutil",
    "pyprind",
    "requests",
    "scipy",
    "stats_arrays>=0.6.5",
    "unicodecsv",
    "voluptuous",
    "whoosh",
    "xlrd",
    "xlsxwriter",
]

setup(
    name='brightway2',
    version="2.4.2",
    packages=["brightway2"],
    author="Chris Mutel",
    author_email="cmutel@gmail.com",
    license=open('LICENSE.txt').read(),
    install_requires=packages,
    url="https://github.com/brightway-lca/brightway2",
    long_description=open('README.md', encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: End Users/Desktop',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: BSD License',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 2 :: Only',
        'Topic :: Scientific/Engineering :: Information Analysis',
        'Topic :: Scientific/Engineering :: Mathematics',
        'Topic :: Scientific/Engineering :: Visualization',
    ],

    extras_require={
    'doc': [
        'ipython',
        'sphinx >= 1.8.0',
        'sphinx-autoapi>=1.1.0',
        'pydata-sphinx-theme==0.8.1',
        'nbsphinx==0.8.8',
        # sphinx-gallery is used indirectly for nbsphinx thumbnail galleries; see:
        # https://nbsphinx.readthedocs.io/en/0.6.0/subdir/gallery.html#Creating-Thumbnail-Galleries
        'sphinx-gallery==0.8.1',
    ],
    'all': [
        'ipython',
        'jupyter',
        'pytest'],
    }

)
