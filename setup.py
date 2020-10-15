import setuptools

from pyforhandbook import version

setuptools.setup(
    name="pyforhandbook",
    version=version.__version__,
    author=version.__author__,
    author_email="python@chapinb.com",
    description="Handbook of Python functions for rapid development "
                "of forensic tools.",
    url="https://chapinb.com/python-forensic-handbook",
    packages=setuptools.find_packages(),
    install_requires=[
        'yarp @ git+https://github.com/msuhanov/yarp@1.0.28#egg=yarp',
        'python-evtx==0.6.1',
        'lxml==4.5.2',
    ],
    classifiers=[
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3 :: Only",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Telecommunications Industry",
        "Intended Audience :: System Administrators",
        "Intended Audience :: Other Audience",
        "Intended Audience :: Information Technology",
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "Natural Language :: English",
        "Topic :: Scientific/Engineering :: Information Analysis",
        "Topic :: Security",
        "Topic :: Utilities",
        "Topic :: Documentation",
        "Topic :: Software Development :: Documentation"
    ]
)
