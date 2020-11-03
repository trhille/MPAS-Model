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
#subprocess.check_call(['python', '-m', 'jigsaw_to_MPAS.build_mesh',
#                       '--geometry', 'plane'])
#
## Run command is:
## MpasCellCuller.x base_mesh.nc grid_culled.nc
#subprocess.check_call(['MpasCellCuller.x', 'base_mesh.nc', 'grid_culled.nc'])
#
## Run command is:
## MpasMeshConverter.x grid_culled.nc grid_converted.nc
#subprocess.check_call(['MpasMeshConverter.x', 'grid_culled.nc',
#                       'grid_converted.nc'])
#
#print("\n\n### Creating LI mesh\n\n")
## Run command is:
## create_landice_grid_from_generic_MPAS_grid.py -i grid_converted.nc -o
## gis_3km_preCull.nc -l 10 -v glimmer
#subprocess.check_call(['create_landice_grid_from_generic_MPAS_grid.py', '-i',
#                       'grid_converted.nc', '-o', 'gis_3km_preCull.nc', '-l',
#                       '10', '-v', 'glimmer'])
#print("\n\n### LI mesh creation complete\n\n")
#
#print("\n\n### Setting up initial condition\n\n")
## Run command is:
## interpolate_to_mpasli_grid.py -s
## humboldt_1km_2020_04_20.epsg3413.icesheetonly.nc -d gis_3km_preCull.nc -m b
## -t
#subprocess.check_call(['interpolate_to_mpasli_grid.py', '-s',
#                       'humboldt_1km_2020_04_20.epsg3413.icesheetonly.nc',
#                       '-d', 'gis_3km_preCull.nc', '-m', 'b', '-t'])
#print("\n\n### Initial condition setup complete\n\n")
#
#print("\n\n### define cull mask\n\n")
## Run command is:
## define_cullMask.py -f gis_3km_preCull.nc -m distance -d 50.0
#subprocess.check_call(['define_cullMask.py', '-f', 'gis_3km_preCull.nc', '-m',
#                       'distance', '-d', '50.0'])
#print("\n\n### define cull mask complete\n\n")
#
#print("\n\n### Setting lat/lon\n\n")
## Run command is:
## set_lat_lon_fields_in_planar_grid.py -f gis_3km_preCull.nc -p gis-gimp
#subprocess.check_call(['set_lat_lon_fields_in_planar_grid.py', '-f',
#                       'gis_3km_preCull.nc', '-p', 'gis-gimp'])
#print("\n\n### Setting lat/lon complete\n\n")

# Run command is:
# MpasMaskCreator.x gis_3km_preCull.nc humboldt_mask.nc -f Humboldt.geojson
subprocess.check_call(['MpasMaskCreator.x', 'gis_3km_preCull.nc',
                       'humboldt_mask.nc', '-f', 'Humboldt_only.geojson'])

# Run command is:
# MpasCellCuller.x gis_3km_preCull.nc gis_culled.nc -i humboldt_mask.nc
subprocess.check_call(['MpasCellCuller.x', 'gis_3km_preCull.nc',
                       'gis_culled.nc', '-i', 'humboldt_mask.nc'])

print("\n\n### Marking horns \n\n")
# Run command is:
# mark_horns_for_culling.py -f gis_culled.nc
subprocess.check_call(['mark_horns_for_culling.py', '-f', 'gis_culled.nc'])
print("\n\n### Marking horns complete\n\n")

# Run command is:
# MpasCellCuller.x gis_culled.nc gis_dehorned.nc
subprocess.check_call(['MpasCellCuller.x', 'gis_culled.nc', 'gis_dehorned.nc'])

print("\n\n### Setting lat/lon\n\n")
# Run command is:
# set_lat_lon_fields_in_planar_grid.py -f gis_3km_preCull.nc -p gis-gimp
subprocess.check_call(['set_lat_lon_fields_in_planar_grid.py', '-f',
                       'gis_3km_preCull.nc', '-p', 'gis-gimp'])
print("\n\n### Setting lat/lon complete\n\n")

# Run command is:
# MpasMeshConverter.x gis_dehorned.nc gis_dehorned_converted.nc
subprocess.check_call(['MpasMeshConverter.x', 'gis_dehorned.nc',
                       'gis_dehorned_converted.nc'])

print("\n\n### Creating LI mesh\n\n")
# Run command is:
# create_landice_grid_from_generic_MPAS_grid.py -i gis_dehorned_converted.nc -o
# Humboldt_3to30km.nc -l 10 -v glimmer --beta --thermal --obs --diri
subprocess.check_call(['create_landice_grid_from_generic_MPAS_grid.py', '-i',
                       'gis_dehorned_converted.nc', '-o',
                       'Humboldt_hydro_3to30km.nc', '-l', '10', '-v', 'glimmer',
                       '--beta', '--thermal', '--obs', '--diri'])
print("\n\n### LI mesh creation complete\n\n")

print("\n\n### Setting up initial condition\n\n")
# Run command is:
# interpolate_to_mpasli_grid.py -s
# humboldt_1km_2020_04_20.epsg3413.icesheetonly.nc -d Humboldt_3to30km.nc -m b
# -t
subprocess.check_call(['interpolate_to_mpasli_grid.py', '-s',
                       'humboldt_1km_2020_04_20.epsg3413.icesheetonly.nc',
                       '-d', 'Humboldt_hydro_3to30km.nc', '-m', 'b', '-t'])
print("\n\n### Initial condition setup complete\n\n")

# Run command is:
# mark_domain_boundaries_dirichlet.py -f Humboldt_3to30km.nc
subprocess.check_call(['mark_domain_boundaries_dirichlet.py', '-f',
                       'Humboldt_hydro_3to30km.nc'])

print("\n\n### Setting lat/lon\n\n")
# Run command is:
# set_lat_lon_fields_in_planar_grid.py -f Humboldt_3to30km.nc -p gis-gimp
subprocess.check_call(['set_lat_lon_fields_in_planar_grid.py', '-f',
                       'Humboldt_hydro_3to30km.nc', '-p', 'gis-gimp'])
print("\n\n### Setting lat/lon complete\n\n")
