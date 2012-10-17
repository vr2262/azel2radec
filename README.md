azel2radec
==========

azel2radec is a python module for converting from horizon coordinates (azimuth
and elevation) to celestial coordinates (right ascension and declination).

It provides 3 methods:

jdcnv      : converts a Gregorian time to a Julian Date

ct2lst     : converts Civil Time to Greenwich Sidereal Time

azel2radec : converts from horizon to celestial coordinates

Typically ct2lst is only used internally to azel2radec. The assumed use case is
that one knows the local time (UTC) and uses jdcnv to convert to a Julian Date,
which is fed into azel2radec.

The azel2radec module is based on code available at
http://idlastro.gsfc.nasa.gov/
and
http://cosmology.berkeley.edu/group/
but does NOT replicate all behavior exactly. The numerical results will be the
same, but the input parameters and outputs may differ.

The azel2radec module is vectorized and supports multicore processing thanks to
the numexpr package.

Dependencies:

numpy

numexpr

Viktor Roytman 2012

viktor.roytman@gmail.com
