"""Calculate Kd from a standard free energy of binding."""

import numpy as _np
from scipy import constants as _const


def calc_k(dg: float, temp: float = 298.15) -> float:
    """
    Calculate Kd from a standard free energy of binding.

    Parameters
    ----------
    dg : float
        Standard free energy of binding in kcal/mol.
    temp : float, optional
        Temperature in Kelvin. Default is 298.15 K.

    Returns
    -------
    float
        Dissociation constant Kd in M.

    Notes
    -----
    The equation used to calculate Kd is:

    .. math::

            K_d = e^{\\frac{\\Delta G}{RT}}

        where :math:`\\Delta G` is the standard free energy of binding in kcal/mol, :math:`R` is the ideal gas constant in cal/(mol K), and :math:`T` is the temperature in Kelvin.
    """
    return _np.exp(dg * 1000 / ((_const.R / _const.calorie) * temp))
