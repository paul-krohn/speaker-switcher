import setuptools


setuptools.setup(
    name="speakerswitcher",
    version="0.0.1",
    author="Paul Krohn",
    author_email="pkrohn@daemonize.com",
    description="",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
        'gpiozero',
        'redis',
    ],
    tests_require=[
        'pytest',
    ],
    scripts=[
        'shell_scripts/switcher-start',
        'shell_scripts/switcher-stop'
    ],
    entry_points={
        'console_scripts': [
            'switcher-listener=speakerswitcher.stuff:listener'
        ]
    }

)
