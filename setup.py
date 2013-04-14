from setuptools import setup

setup(
    name='horace',
    version='0.5',
    packages=['horace' ],
    url='http://github.com/lawrencec/horace',
    license='LICENSE.txt',
    author='Lawrence Carvalho',
    author_email='lawrence@nodetraveller.com',
    description='A page object pattern based web browser automation tool',
    install_requires=[
        'selenium>=2.32.0'
    ]
)
