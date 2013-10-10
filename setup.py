from setuptools import setup

packages = [
    "lxml",
    "numpy",
    "scipy",
    "nose",
    "progressbar",
    "voluptuous",
    "fuzzywuzzy",
    "flask",
    "docopt",
    "bw2calc>=0.10.1",
    "bw2ui>=0.7",
    "bw2analyzer>=0.4",
    "bw2data>=0.10.1",
    "requests>=1.1.0",
    "bw-stats-toolkit>=0.7",
]

setup(
    name='brightway2',
    version="0.10",
    packages=["brightway2"],
    author="Chris Mutel",
    author_email="cmutel@gmail.com",
    license=open('LICENSE.txt').read(),
    install_requires=packages,
    url="https://bitbucket.org/cmutel/brightway2",
    long_description=open('README.rst').read(),
    classifiers=[
        'Development Status :: 4 - Beta',
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
)
