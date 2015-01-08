from setuptools import setup

setup(name='numerical_analysis',
      version='0.1',
      description="Numerical Analysis",
      long_description="",
      author='Ludovic Charleux, Fabien Formosa',
      author_email='ludovic.charleux@univ-savoie.fr',
      license='GPL v2',
      packages=["dummy"],
      zip_safe=False,
      install_requires=[
          "numpy",
          "scipy",
          "matplotlib"
          ],
      )
