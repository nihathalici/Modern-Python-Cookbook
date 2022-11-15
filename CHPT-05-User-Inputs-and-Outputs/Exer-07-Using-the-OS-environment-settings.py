# Exer-07-Using-the-OS-environment-settings

import os, sys
from ch03_r05 import haversine, MI, NM, KM

def get_options(argv=sys.argv):
    default_units = os.environ.get('UNITS', 'KM')
    if default_units not in ('KM', 'NM', 'MI'):
        sys.exit("Invalid value for UNITS, not KM, NM, or MI")
    default_home_port = os.environ.get('HOME_PORT')
