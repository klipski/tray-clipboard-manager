# -*- coding: utf-8 -*-

from setuptools import setup

with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='trayclipboardmanager',
    version='0.1',
    description='Simple clipboard manager as tray icon.',
    url='http://github.com/klipski/tray-clipboard-manager',
    long_description=readme,
    author='Kamil Lipski',
    author_email='lipskikamil94@gmail.com',
    license=license,
    packages=['trayclipboardmanager'],
    install_requires=['PyQt5', 'PyQt5-sip'],
)
