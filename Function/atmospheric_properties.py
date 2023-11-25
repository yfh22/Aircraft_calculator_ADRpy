from ADRpy import atmospheres as at
from ADRpy import unitconversions as co

# Instantiate an atmosphere object: an ISA with a +10C offset
isa = at.Atmosphere(offset_deg=10)

# Query the ambient density in this model at 41,000 feet 
print("ISA+10C density at 41,000 feet (geopotential):", 
      isa.airdens_kgpm3(co.feet2m(41000)), "kg/m^3")