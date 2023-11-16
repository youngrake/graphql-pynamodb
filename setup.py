from setuptools import find_packages, setup

setup(
    name='graphene-pynamodb',
    version='2.3.1',

    description='Graphene PynamoDB integration',
    long_description=open('README.rst').read(),

    url='https://github.com/yfilali/graphql-pynamodb',

    author='Yacine Filali',
    author_email='yfilali@gmail.com',

    license='MIT',

    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: Implementation :: PyPy',
    ],

    keywords='api graphql protocol rest relay graphene pynamodb dynamodb',

    packages=find_packages(exclude=['tests']),

    install_requires=[
        'six>=1.12.0',
        'promise==2.3',
        'graphql-core < 3.0, >=2.0',
        'graphene <= 3.0b6, >= 2.0',
        'botocore >= 1.12.54',
        'pynamodb >= 4.0.0, < 5.0.0',
        'singledispatch>=3.4.0.3',
        'wrapt>=1.10.8'
    ],
    setup_requires=['pytest-runner'],
    tests_require=[
        'pytest>=3.6',
        'mock'
    ],
    test_suite="graphene_pynamodb.tests",

)
