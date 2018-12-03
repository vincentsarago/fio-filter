fio-filter
==========

Filter a dataset using a geojson feature.

.. code-block::

    $ fio filter --help
    Usage: fio filter [OPTIONS] SRC_DST FEATURES...

      Filter data.

    Options:
      --sequence / --no-sequence      Write a LF-delimited sequence of texts
                                      containing individual objects or write a
                                      single JSON text containing a feature
                                      collection object (the default).
      --ops [intersects|overlaps|touches|crosses|disjoint|within|contains|almost_equals|equals]
                                      Binary Relationship (see https://shapely.readthedocs.io/en/stable/manual.html#predicates-and-relationships)
      --help                          Show this message and exit.

Installation
============

.. code-block::

    pip install fio-filter


Exemple
=======

.. code-block::

    cat tz_world.geojson | fio filter canada.geojson > tz_canada.geojson
