from setuptools import setup, find_packages


setup(
    name='explo',
    version='0.1',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='EDSA Sprint 2 Project',
    long_description=open('README.md').read(),
    install_requires=['numpy', 'pandas'],
    url='https://github.com/BossaNostra/explo.git',
    author='Bongane Zitha',
    author_email='bonga.zitha@gmail.com'
)