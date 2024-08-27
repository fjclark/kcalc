"""A CLI for ``kcalc``."""

import click

from .conversion import calc_k


@click.command
@click.argument("dg", type=float)
@click.option(
    "--temp",
    type=float,
    default=298.15,
    help="Temperature in Kelvin. Default is 298.15 K.",
)
def main(dg: float, temp: float):
    """Calculate Kd from a standard free energy of binding (in kcal/mol)."""
    kd = calc_k(dg, temp)
    print(f"Kd = {kd:.2e} M")
