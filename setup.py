
from codecs import open as codecs_open
from setuptools import setup, find_packages

with codecs_open('README.rst', encoding='utf-8') as f:
    long_description = f.read()

# Runtime requirements.
inst_reqs = ["Fiona", "click", "cligj", "shapely"]

extra_reqs = {
    "test": ["pytest", "pytest-cov"],
}

setup(name='fio-filter',
      version='0.0.1',
      description="Fiona CLI plugin to filter geomtry",
      long_description="Fiona CLI plugin to filter geometry",
      classifiers=[],
      keywords='fiona',
      author=u"",
      author_email='',
      url='https://github.com/vincentsarago/fio-filter',
      license='BSD-3',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=inst_reqs,
      extras_require=extra_reqs,
      entry_points="""
      [fiona.fio_commands]
      extent=fio_filter.scripts.cli:filter
      """)
