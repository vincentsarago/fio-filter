import json

import click
import cligj

from shapely.geometry import shape


@click.command()
@click.argument("src_dst", type=click.Path(exists=True), nargs=1)
@click.pass_context
@cligj.features_in_arg
@cligj.sequence_opt
@click.option(
    "--ops",
    type=click.Choice([
        "intersects",
        "overlaps",
        "touches",
        "crosses",
        "disjoint",
        "within",
        "contains",
        "almost_equals",
        "equals",
    ]),
    default="intersects",
    help="Binary Relationship (see https://shapely.readthedocs.io/en/stable/manual.html#predicates-and-relationships)",
)
def filter(ctx, src_dst, features, sequence, ops):
    """Filter data."""
    with open(src_dst, "r") as f:
        geom = shape(json.loads(f.read())['geometry'])

    for f in features:
        if ops == "intersects":
            tag = shape(f['geometry']).intersects(geom)
        elif ops == "overlaps":
            tag = shape(f['geometry']).overlaps(geom)
        elif ops == "touches":
            tag = shape(f['geometry']).touches(geom)
        elif ops == "crosses":
            tag = shape(f['geometry']).crosses(geom)
        elif ops == "disjoint":
            tag = shape(f['geometry']).disjoint(geom)
        elif ops == "within":
            tag = shape(f['geometry']).within(geom)
        elif ops == "contains":
            tag = shape(f['geometry']).contains(geom)
        elif ops == "almost_equals":
            tag = shape(f['geometry']).almost_equals(geom)
        elif ops == "equals":
            tag = shape(f['geometry']).equals(geom)
        else:
            raise Exception("Not sure how see happened")
        if tag:
            click.echo(json.dumps(f))
