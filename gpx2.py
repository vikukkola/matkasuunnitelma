import gpxpy
import gpxpy.gpx

locations = [
    ("Vlacherna Monastery", 39.5920, 19.9182),
    ("Pontikonisi", 39.5915, 19.9197),
    ("Old Fortress", 39.6212, 19.9247),
    ("New Fortress", 39.6240, 19.9206),
    ("Liston", 39.6216, 19.9212),
    ("Achilleion", 39.5624, 19.9061),
    ("Benitses Beach", 39.5455, 19.8942),
    ("Kapodistrias Museum", 39.6293, 19.8796),
    ("Mon Repos", 39.6056, 19.9190),
    ("Garitsa Bay", 39.6105, 19.9222),
    ("Paleokastritsa", 39.6726, 19.7058),
    ("La Grotta", 39.6800, 19.7030),
    ("Pantokrator", 39.7489, 19.8690),
    ("Old Perithia", 39.7533, 19.8753)
]

gpx = gpxpy.gpx.GPX()

for name, lat, lon in locations:
    wp = gpxpy.gpx.GPXWaypoint(latitude=lat, longitude=lon, name=name)
    gpx.waypoints.append(wp)

with open("korfu_reitit.gpx", "w", encoding="utf-8") as f:
    f.write(gpx.to_xml())
