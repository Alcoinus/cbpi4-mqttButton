from setuptools import setup

# read the contents of your README file
from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()


setup(name='cbpi4-mqttButton',
      version='0.0.2',
      description='CraftBeerPi Plugin to add an MQTT Button',
      author='Felix Theiß',
      author_email='felix.theiss@outlook.com',
      url='https://github.com/Alcoinus/cbpi4-mqttButton',
      include_package_data=True,
      package_data={
        # If any package contains *.txt or *.rst files, include them:
      '': ['*.txt', '*.rst', '*.yaml'],
      'cbpi4-mqttButton': ['*','*.txt', '*.rst', '*.yaml']},
      packages=['cbpi4-mqttButton'],
      long_description=long_description,
      long_description_content_type='text/markdown'
     )