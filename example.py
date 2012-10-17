#===============================================================================
# This is an example of a script making use of azel2radec to create 2 streams
# of RA and dec data for a telescope operating at 100 Hz and moving in a sine
# wave in azimuth and elevation (physically unusual, but mathematically valid).
#===============================================================================

import azel2radec as a2r
import numpy as np

# Location of the telescope
latitude = np.radians(30.0) # 30 degrees North
longitude_deg = 60.0 # 60 degrees East

# Date and time at which the scan begins (UTC)
# Inputs are year, month, day, hour (float)
start_time = a2r.jdcnv(2012, 10, 16, 15)

# Duration of scan in seconds
duration = 2 * 60 * 60 # 2 hours

# Sampling rate in Hz
rate = 100

# Number of data points
big_n = int(duration * rate + 1)

# Array of sample times per beam
times = np.linspace(0, duration, big_n)
time_data = start_time + a2r.second_jul * times

# scan speed in degrees per second
speed = 5

# Peak amplitude for sine oscillations
peak_amplitude = 5.0

frequency = 2 * np.pi * speed / (4 * peak_amplitude)

# azimuth data
azimuth = peak_amplitude * np.sin(frequency * times)
azimuth_rad = np.radians(azimuth)

# elevation data
elevation = peak_amplitude * np.sin(frequency * times) + 45.0
elevation_rad = np.radians(elevation)

ra, dec = a2r.azel2radec(time_data, azimuth_rad, elevation, \
                         latitude, longitude_deg)

np.save('ra.npy', ra)
np.save('dec.npy', dec)
