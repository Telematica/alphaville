import os
import sys
import contextlib
from misc.error import FatalError


def env_property(prop, caster=None):
    """
    Read env variables for microservice's sake
    """

    val = os.environ.get(prop)
    if val is None:
        raise FatalError("Enviroment variable {} has not been set !!".format(prop))

    if caster is None:
       return val

    try:
        return caster(val)
    except:
        raise FatalError("Enviroment variable {} could not be casted !!".format(prop))
