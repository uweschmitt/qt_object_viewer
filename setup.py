from setuptools import setup, find_packages

description = "qt tree model + tree viewer for nested objects"

long_description = """
This Python package provides a Qt based widget and a dialog class for exploring a
nested object structure.

For examples see: http://github.com/uweschmitt/qt_object_viewer.git
"""

setup(name="qt_object_viewer",
      description=description,
      long_description=long_description,
      maintainer="Uwe Schmitt",
      maintainer_email="uwe.schmitt@id.ethz.ch",
      platforms=["any"],
      version="1.0.1",
      packages=find_packages(exclude=["tests"]),
      include_package_data=True,
      zip_safe=False,
      )
