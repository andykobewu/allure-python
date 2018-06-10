import os
from setuptools import setup


PACKAGE = "allure-robotframework"
VERSION = "0.1.3"

classifiers = [
    'Development Status :: 4 - Beta',
    'Framework :: Robot Framework',
    'Framework :: Robot Framework :: Tool',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: Apache Software License',
    'Topic :: Software Development :: Quality Assurance',
    'Topic :: Software Development :: Testing',
]

install_requires = [
    "allure-python-commons==2.3.4b1",
]


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


if __name__ == '__main__':
    setup(
        name=PACKAGE,
        version=VERSION,
        description="Allure Robot Framework integration",
        license="Apache-2.0",
        keywords="allure reporting robotframework",
        packages=['allure_robotframework'],
        package_dir={"allure_robotframework": "src"},
        install_requires=install_requires,
        py_modules=['allure_robotframework'],
        url="https://github.com/allure-framework/allure-python",
        author="Sergey Khomutinin",
        author_email="skhomuti@gmail.com",
        long_description=read('README.rst'),
        classifiers=classifiers,
    )