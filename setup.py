from setuptools import setup, find_packages

requires = [
    'requests'
]

tests_require = [
    'pytest',
]

setup(
    name='freenas-api-client',
    version='0.1',
    description='FreeNAS REST API Client',
    long_description=open('README.rst').read(),
    classifiers=[
        "Programming Language :: Python",
        'Programming Language :: Python :: 3.6',
    ],
    author='Gatsby Lee',
    url='https://github.com/Gatsby-Lee/freenas-api-client',
    keywords='gatsby freenas',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=requires,
    extras_require={
        'testing': tests_require,
    },
)
