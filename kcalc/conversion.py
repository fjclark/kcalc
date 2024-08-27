"""Functions for converting between free energy and dissociation constant."""

import numpy as _np
from scipy import constants as _const


def calc_k(dg: float, temp: float = 298.15) -> float:
    """
    Calculate the dissociation constant (Kd) from the standard free energy of binding (ΔG).

    Args:
        dg (float): Standard free energy of binding in kcal/mol.
        temp (float, optional): Temperature in Kelvin. Default is 298.15 K.

    Returns:
        float: Dissociation constant Kd in M.

    Notes:
        The equation used to calculate Kd is:

        $$
        K_d = e^{\\frac{\\Delta G}{RT}}
        $$

        where $\\Delta G$ is the standard free energy of binding,
        $R$ is the gas constant, and $T$ is the temperature in Kelvin.
    """
    return _np.exp(dg * 1000 / ((_const.R / _const.calorie) * temp))
