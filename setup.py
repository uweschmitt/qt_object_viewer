from setuptools import setup, find_packages

version = (0, 0, 1)

description = "qt tree model + tree viewre for nestes objects"

setup(name="qt_object_viewer",
      description=description,
      maintainer="Uwe Schmitt",
      maintainer_email="uwe.schmitt@id.ethz.ch",
      platforms=["any"],

      packages=find_packages(exclude=["tests"]),
      #entry_points={
          #"gui_scripts": ["envipy = eawag_gui.main:main"]
      #},
      version="%d.%d.%d" % version,
      include_package_data=True,
      zip_safe=False,
      install_requires=["guidata"]
      )
