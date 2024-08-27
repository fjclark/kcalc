"""A CLI for ``kcalc``."""

import click

from .conversion import calc_k


@click.command
@click.argument("neg_dg", type=float)
@click.option(
    "--temp",
    type=float,
    default=298.15,
    help="Temperature in Kelvin. Default is 298.15 K.",
)
def main(neg_dg: float, temp: float):
    """
    Calculate Kd from a standard free energy of binding (in kcal/mol).
    The standard free energy of binding should be entered as its negative
    (e.g. enter -10 kcal /mol as '10')."""
    kd = calc_k(-neg_dg, temp)
    print(f"Kd = {kd:.2e} M")
