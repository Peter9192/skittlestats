from setuptools import setup

def readme():
    with open('README.rst') as f:
        return f.read()

setup(name='skittlestats',
      version='0.1',
      description='Because no two rainbows are the same',
      long_description=readme(),
      url='https://github.com/Peter9192/skittlestats',
      author='Peter9192',
      license='MIT',
      packages=['skittlestats'],
      install_requires=[
          'numpy', 'pandas', 'xarray', 'matplotlib', 'scikit-learn',
      ],
      test_suite='nose.collector',
      tests_require=['nose'],
      entry_points={
          'console_scripts': ['skittlestats = skittlestats.command_line:main'],
      },
      include_package_data=True,
      zip_safe=False)
