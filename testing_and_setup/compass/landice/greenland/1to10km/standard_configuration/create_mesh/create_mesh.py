#!/usr/bin/env python

# This script was generated from setup_testcases.py as part of a config file

import sys
import os
import shutil
import glob
import subprocess


dev_null = open('/dev/null', 'w')

# Run command is:
# python -m jigsaw_to_MPAS.build_mesh --geometry plane
subprocess.check_call(['python', '-m', 'jigsaw_to_MPAS.build_mesh',
                       '--geometry', 'plane'])

# Run command is:
# MpasCellCuller.x base_mesh.nc grid_culled.nc
subprocess.check_call(['MpasCellCuller.x', 'base_mesh.nc', 'grid_culled.nc'])

# Run command is:
# MpasMeshConverter.x grid_culled.nc grid_converted.nc
subprocess.check_call(['MpasMeshConverter.x', 'grid_culled.nc',
                       'grid_converted.nc'])

print("\n\n### Creating LI mesh\n\n")
# Run command is:
# create_landice_grid_from_generic_MPAS_grid.py -i grid_converted.nc -o
# gis_1km_preCull.nc -l 10 -v glimmer
subprocess.check_call(['create_landice_grid_from_generic_MPAS_grid.py', '-i',
                       'grid_converted.nc', '-o', 'gis_1km_preCull.nc', '-l',
                       '10', '-v', 'glimmer'])
print("\n\n### LI mesh creation complete\n\n")

print("\n\n### Setting up initial condition\n\n")
# Run command is:
# interpolate_to_mpasli_grid.py -s
# /Users/trevorhillebrand/Documents/Greenland/greenland_1km_2020_03_04.epsg3413.icesheetonly.nc
# -d gis_1km_preCull.nc -m b -t
subprocess.check_call(['interpolate_to_mpasli_grid.py', '-s',
                       '/Users/trevorhillebrand/Documents/Greenland/greenland_1km_2020_03_04.epsg3413.icesheetonly.nc',
                       '-d', 'gis_1km_preCull.nc', '-m', 'b', '-t'])
print("\n\n### Initial condition setup complete\n\n")

print("\n\n### define cull mask\n\n")
# Run command is:
# define_cullMask.py -f gis_1km_preCull.nc -m distance -d 50.0
subprocess.check_call(['define_cullMask.py', '-f', 'gis_1km_preCull.nc', '-m',
                       'distance', '-d', '50.0'])
print("\n\n### define cull mask complete\n\n")

# Run command is:
# MpasCellCuller.x gis_1km_preCull.nc gis_culled.nc
subprocess.check_call(['MpasCellCuller.x', 'gis_1km_preCull.nc',
                       'gis_culled.nc'])

# Run command is:
# MpasMeshConverter.x gis_culled.nc gis_culled_converted.nc
subprocess.check_call(['MpasMeshConverter.x', 'gis_culled.nc',
                       'gis_culled_converted.nc'])

print("\n\n### Creating LI mesh\n\n")
# Run command is:
# create_landice_grid_from_generic_MPAS_grid.py -i gis_culled_converted.nc -o
# gis_1km.nc -l 10 -v glimmer --beta --thermal --obs --diri
subprocess.check_call(['create_landice_grid_from_generic_MPAS_grid.py', '-i',
                       'gis_culled_converted.nc', '-o', 'gis_1km.nc', '-l',
                       '10', '-v', 'glimmer', '--beta', '--thermal', '--obs',
                       '--diri'])
print("\n\n### LI mesh creation complete\n\n")

print("\n\n### Setting up initial condition\n\n")
# Run command is:
# interpolate_to_mpasli_grid.py -s
# /Users/trevorhillebrand/Documents/Greenland/greenland_1km_2020_03_04.epsg3413.icesheetonly.nc
# -d gis_1km.nc -m b -t
subprocess.check_call(['interpolate_to_mpasli_grid.py', '-s',
                       '/Users/trevorhillebrand/Documents/Greenland/greenland_1km_2020_03_04.epsg3413.icesheetonly.nc',
                       '-d', 'gis_1km.nc', '-m', 'b', '-t'])
print("\n\n### Initial condition setup complete\n\n")

print("\n\n### Setting lat/lon\n\n")
# Run command is:
# set_lat_lon_fields_in_planar_grid.py -f gis_1km.nc -p gis-gimp
subprocess.check_call(['set_lat_lon_fields_in_planar_grid.py', '-f',
                       'gis_1km.nc', '-p', 'gis-gimp'])
print("\n\n### Setting lat/lon complete\n\n")
