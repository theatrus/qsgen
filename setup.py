import ez_setup
ez_setup.use_setuptools()

from setuptools import setup


setup(name = 'qsgen',
      version = '0.1',
      name = 'qsgen',
      description = 'An HTML static site generator for Mako',
      author = 'Yann Ramin',
      install_requires = ['Mako', 'Pygments'],
      license = 'MIT',
      author_email = 'atrus@stackworks.net',
      url = 'http://www.stackfoundry.com/other/qsgen/',
      scripts = ['qsgen'])
