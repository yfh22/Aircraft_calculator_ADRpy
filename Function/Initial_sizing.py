# Compute the thrust to weight ratio required for take-off, given
# a basic design brief, a basic design definition and a set of 
# atmospheric conditions

from ADRpy import atmospheres as at
from ADRpy import constraintanalysis as ca
from ADRpy import unitconversions as co


# The environment: 'unusually high temperature at 5km' atmosphere
# from MIL-HDBK-310. 

# Extract the relevant atmospheric profiles...
profile_ht5_1percentile, _ = at.mil_hdbk_310('high', 'temp', 5)

# ...then use them to create an atmosphere object 
m310_ht5 = at.Atmosphere(profile=profile_ht5_1percentile)

#====================================================================

# The take-off aspects of the design brief:
designbrief = {'rwyelevation_m':1000, 'groundrun_m':1200}

# Basic features of the concept:
# aspect ratio, engine bypass ratio, throttle ratio 
designdefinition = {'aspectratio':7.3, 'bpr':3.9, 'tr':1.05}

# Initial estimates of aerodynamic performance:
designperf = {'CDTO':0.04, 'CLTO':0.9, 'CLmaxTO':1.6,
              'mu_R':0.02} # ...and wheel rolling resistance coeff.

# An aircraft concept object can now be instantiated
concept = ca.AircraftConcept(designbrief, designdefinition,
                             designperf, m310_ht5)

#====================================================================

# Compute the required standard day sea level thrust/MTOW ratio reqd.
# for the target take-off performance at a range of wing loadings:
wingloadinglist_pa = [2000, 3000, 4000, 5000]

tw_sl, liftoffspeed_mpstas, _ = concept.twrequired_to(wingloadinglist_pa)

# The take-off constraint calculation also supplies an estimate of
# the lift-off speed; this is TAS (assuming zero wind) - we convert 
# it to equivalent airspeed (EAS), in m/s:
liftoffspeed_mpseas = \
m310_ht5.tas2eas(liftoffspeed_mpstas, designbrief['rwyelevation_m'])

print("Required T/W and V_liftoff under MIL-HDBK-310 conditions:")
print("\nT/W (std. day, SL, static thrust):", tw_sl)
print("\nLiftoff speed (KEAS):", co.mps2kts(liftoffspeed_mpseas))