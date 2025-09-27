
# pip install astropy astroplan
from astropy.coordinates import SkyCoord, EarthLocation, AltAz, get_body, Angle
from astropy.time import Time
import astropy.units as u
from astroplan import Observer, FixedTarget
from datetime import datetime, timezone, timedelta

# Your location (Copenhagen)
obs = Observer(
    location=EarthLocation(lat=55.6761*u.deg, lon=12.5683*u.deg, height=10*u.m),
    name="Copenhagen",
    timezone="Europe/Copenhagen"
)

# Choose target: "jupiter", "saturn", "vega", etc.
now = Time(datetime.now(timezone.utc))
body = get_body("jupiter", now, obs.location)
target = FixedTarget(name="Jupiter", coord=SkyCoord(body.ra, body.dec))

# Next meridian transit time (upper culmination)
next_transit = obs.target_meridian_transit_time(now, target, which='next')

# Also useful: altitude at transit and current RA/Dec
altaz_at_transit = target.coord.transform_to(AltAz(obstime=next_transit, location=obs.location))
print(f"Next transit (local time): {next_transit.to_datetime(obs.timezone)}")
print(f"RA/Dec now: {target.coord.to_string('hmsdms')}")
print(f"Alt/Az at transit: {altaz_at_transit.alt:.1f}, {altaz_at_transit.az:.1f}")