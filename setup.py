from setuptools import setup, find_packages

# Python 3.7.2

install_requires = [
    "Django==2.2",
    "djangorestframework==3.12.1",
]

dev_requires = [
    'django-debug-toolbar',
]

test_requires = [
    "pytest",
    "pytest-cov",
    "pytest-django",
]

setup(
    name="flathub",
    version="0.1.0",
    author="Christian Vera",
    author_email="Crvc1998@gmail.com",
    url="https://github.com/CrvcMaestro1/flathub",
    description="DRF Test",

    packages=find_packages(exclude=("tests", "tests.*")),
    include_package_data=True,

    zip_safe=False,

    extras_require={
        "tests": test_requires,
        "dev": dev_requires,
    },
    install_requires=install_requires,
    tests_require=test_requires,
)
