from distutils.core import setup

setup(
    name='anlp_grading',
    version='1.0',
    description='Advanced NLP Grading Tools',
    author='Shubham Phal/Hao Zhu',
    author_email='sphal@cs.cmu.edu',
    packages=['anlp_grading'],
    install_requires=['torch']
)