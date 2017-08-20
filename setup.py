from setuptools import setup
from sphinx.setup_command import BuildDoc
cmdclass = {'build_sphinx': BuildDoc}

name = 'boilerplate'
version = '0.1'
release = '0.1.0'

setup(name=name,
      version=release,
      description='A Python boilerplate project',
      url='http://github.com/notgnoshi/boilerplate',
      author='Austin Gill',
      author_email='notgnoshi@gmail.com',
      license='MIT',
      packages=['boilerplate'],
      test_suite='nose.collector',
      tests_require=[
          'nose',
          'sphinx'
      ],
      install_requires=[
          'nose',
          'sphinx',
      ],
      zip_safe=False,
      cmdclass=cmdclass,
      # these are optional and override conf.py settings
      command_options={
          'build_sphinx': {
              'project': ('setup.py', name),
              'version': ('setup.py', version),
              'release': ('setup.py', release)}}
     )
