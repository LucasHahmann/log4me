from setuptools import setup, find_packages
 
classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Intended Audience :: Education',
  'Operating System :: Microsoft :: Windows :: Windows 10',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
]
 
setup(
  name='log4me',
  version='0.0.1',
  description='Basic logger for personal python projects',
  long_description=open('README.txt').read() + '\n\n' + open('CHANGELOG.txt').read(),
  url='https://github.com/LucasHahmann/log4me',  
  author='Lucas Hahmann',
  author_email='lucas@hahmann-trier.de',
  license='MIT', 
  classifiers=classifiers,
  keywords='logger', 
  packages=find_packages(),
  install_requires=['datetime'] 
)