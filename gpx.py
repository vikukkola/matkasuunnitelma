from xml.etree.ElementTree import Element, SubElement, ElementTree

def create_gpx_route():
    gpx = Element('gpx', version="1.1", creator="ChatGPT - Korfu Reitti", xmlns="http://www.topografix.com/GPX/1/1")

    # Päivittäiset kohteet (koordinaatit arvioita lähteiden mukaan)
    locations = [
        ("Hotelli", 39.593264, 19.918288),
        ("Vlacherna Monastery", 39.5893, 19.9196),
        ("Pontikonisi", 39.5898, 19.9220),
        ("Old Fortress", 39.6210, 19.9245),
        ("Liston", 39.6200, 19.9215),
        ("New Fortress", 39.6230, 19.9145),
        ("Achilleion Palace", 39.5622, 19.9064),
        ("Benitses Beach", 39.5505, 19.8937),
        ("Kapodistrias Museum", 39.6422, 19.8789),
        ("Mon Repos Palace", 39.6066, 19.9265),
        ("Garitsa Bay", 39.6105, 19.9220),
        ("Paleokastritsa", 39.6763, 19.7051),
        ("La Grotta", 39.6745, 19.7090),
        ("Pantokrator", 39.7441, 19.8506),
        ("Old Perithia", 39.7531, 19.8589),
        ("Lentokenttä", 39.6019, 19.9127)
    ]

    for name, lat, lon in locations:
        wpt = SubElement(gpx, 'wpt', lat=str(lat), lon=str(lon))
        SubElement(wpt, 'name').text = name

    # Tiedoston tallennus
    tree = ElementTree(gpx)
    file_name = "korfu_matkareitti.gpx"
    tree.write(file_name, encoding='utf-8', xml_declaration=True)
    print(f"GPX-tiedosto luotu: {file_name}")

create_gpx_route()
