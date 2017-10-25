
from setuptools import setup


setup(
    name='ppdecode',
    version='1.0.0',
    url='https://github.com/spyoungtech/ppdecode.git',
    author='warquel',
    description='Proofpoint URL Decoder',
    packages=['ppdecode'],
    platforms='any',
    install_requires=[],
    entry_points='''
        [console_scripts]
        ppdecode=ppdecode.ppdecode.main
    '''
)