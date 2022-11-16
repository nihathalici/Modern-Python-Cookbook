# Exer-07-Using-the-OS-environment-settings

import os, sys
from ch03_r05 import haversine, MI, NM, KM

def get_options(argv=sys.argv):
    default_units = os.environ.get('UNITS', 'KM')
    if default_units not in ('KM', 'NM', 'MI'):
        sys.exit("Invalid value for UNITS, not KM, NM, or MI")
    default_home_port = os.environ.get('HOME_PORT')

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-r', action='store', 
    choices=('NM', 'MI', 'KM'), default=default_units)
parser.add_argument('p1', action='store', type=point_type)
parser.add_argument('p2', nargs='?', action='store', 
    type=point_type, default=default_home_port)
options = parser.parse_args(argv[1:])
if options.p2 is None:
    sys.exit("Neither HOME_PORT nor p2 argument provided.")
return options
