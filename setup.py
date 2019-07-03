import setuptools

setuptools.setup(
    name = "brainwallet",
    version = "0.0.1",
    author = "Lukáš Moláček",
    author_email = "lukas@molacek.net",
    packages = setuptools.find_packages(),
    install_requires = ["python-bitcoinlib"],
    entry_points = {
        "console_scripts": [
            "brainwallet = brainwallet:main"
        ]

    }
)
