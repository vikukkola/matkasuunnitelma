from fpdf import FPDF
from xml.etree.ElementTree import Element, SubElement, ElementTree
import gpxpy.gpx

# --- Kohteet: nimi, lat, lon, hinta, huomio ---
locations_info = [
    ("Vlacherna Monastery", 39.5920, 19.9182, 0, "Ilmainen pieni luostari sillan päässä – upea valokuvauspaikka."),
    ("Pontikonisi", 39.5915, 19.9197, 3, "Pieni saari – pääsymaksu noin 3 €, veneretki sisältyy."),
    ("Old Fortress", 39.6212, 19.9247, 6, "Historiallinen linnoitus – noin 6 € aikuisilta."),
    ("New Fortress", 39.6240, 19.9206, 0, "Ilmainen ulkoalue – upea näköala."),
    ("Liston", 39.6216, 19.9212, 0, "Ilmainen – tunnettu kahviloistaan."),
    ("Achilleion", 39.5624, 19.9061, 10, "Keisarinna Sisin palatsi – sisäänpääsy n. 10 €."),
    ("Benitses Beach", 39.5455, 19.8942, 0, "Ilmainen ranta – rauhallinen."),
    ("Kapodistrias Museum", 39.6293, 19.8796, 5, "Museo puutarhassa – noin 5 €."),
    ("Mon Repos", 39.6056, 19.9190, 4, "Museo ja puisto – noin 4 €."),
    ("Garitsa Bay", 39.6105, 19.9222, 0, "Rantakävely iltaisin."),
    ("Paleokastritsa", 39.6726, 19.7058, 0, "Luostari ilmainen, akvaario + veneretket lisämaksusta."),
    ("La Grotta", 39.6800, 19.7030, 0, "Pääsy ilmainen, juomat maksullisia."),
    ("Pantokrator", 39.7489, 19.8690, 0, "Korkein kohta – ilmainen näkymä."),
    ("Old Perithia", 39.7533, 19.8753, 0, "Autenttinen kylä – ilmainen tutkia.")
]

location_dict = {name: (lat, lon, price, note) for name, lat, lon, price, note in locations_info}

# --- Päiväkohtaiset suunnitelmat + varakohteet + ruokailut + aikataulu ---
days = [
    {
        "title": "Päivä 1 – Saapuminen ja lähialue",
        "places": ["Vlacherna Monastery", "Pontikonisi"],
        "varakohteet": ["Liston"],
        "schedule": [("14:00", "Check‑in ja majoittuminen"), ("16:00", "Vlacherna Monastery"), ("17:00", "Pontikonisi")],
        "meals": ["Kevyt päivällinen hotellin lähistöllä"],
    },
    {
        "title": "Päivä 2 – Korfun vanhakaupunki",
        "places": ["Old Fortress", "Liston", "New Fortress"],
        "varakohteet": ["Garitsa Bay"],
        "schedule": [("09:30", "Lähtö vanhaankaupunkiin"), ("10:00", "Old Fortress"), ("12:00", "Liston (lounas)"),
                     ("14:00", "New Fortress"), ("16:00", "Paluu")],
        "meals": ["Lounas Liston‑alueella", "Illallinen kaupungilla"],
    },
    {
        "title": "Päivä 3 – Achilleion ja ranta",
        "places": ["Achilleion", "Benitses Beach"],
        "varakohteet": ["Mon Repos"],
        "schedule": [("09:00", "Aamupäivä Achilleionissa"), ("11:30", "Benitses Beach (uintia ja lounas)"), ("15:00", "Paluu hotellille")],
        "meals": ["Rantaravintola lounaaksi", "Kevyt illallinen"],
    },
    {
        "title": "Päivä 4 – Kulttuuri ja puistot",
        "places": ["Kapodistrias Museum", "Mon Repos", "Garitsa Bay"],
        "varakohteet": ["Old Fortress"],
        "schedule": [("09:00", "Kapodistrias Museum"), ("11:00", "Mon Repos ja puisto"), ("13:30", "Garitsa Bay kävely"),
                     ("15:00", "Rentoa aikaa keskustassa")],
        "meals": ["Museokahvila", "Illallinen Garitsa Bay ‑alueella"],
    },
    {
        "title": "Päivä 5 – Paleokastritsa‑retki",
        "places": ["Paleokastritsa", "La Grotta"],
        "varakohteet": ["Pantokrator"],
        "schedule": [("09:00", "Vuokra-auto ja lähtö"), ("10:00", "Paleokastritsa (luostari, veneretki)"),
                     ("13:00", "La Grotta (lounas ja uinti)"), ("16:00", "Paluu hotellille")],
        "meals": ["Lounas La Grottassa", "Mahdollinen päivällinen hotellilla"],
    },
    {
        "title": "Päivä 6 – Pantokrator & Old Perithia",
        "places": ["Pantokrator", "Old Perithia"],
        "varakohteet": ["Paleokastritsa"],
        "schedule": [("09:00", "Ajo Pantokratoriin"), ("11:00", "Old Perithia (kävelyä ja lounas)"), ("15:00", "Paluu hotellille")],
        "meals": ["Lounas Old Perithiassa", "Illallinen Corfussa"],
    },
    {
        "title": "Päivä 7 – Lähtöpäivä",
        "places": ["Pontikonisi"],
        "varakohteet": ["Vlacherna Monastery"],
        "schedule": [("09:00", "Aamukävely Pontikonisille"), ("11:00", "Check‑out")],
        "meals": ["Aamiainen hotellilla", "Mahdollinen kevyt lounas matkalla"],
    },
]

# --- PDF-luokka ulkoasuparannuksin ---
class TravelPDF(FPDF):
    def header(self):
        # ei perus headeri joka sivulla (varaa tilaa kansikuvassa)
        pass

    def footer(self):
        self.set_y(-15)
        self.set_font("DejaVu", "I", 8)
        self.set_text_color(128,128,128)
        self.cell(0, 10, f"Sivu {self.page_no()}", 0, 0, "C")

pdf = TravelPDF()
pdf.add_font("DejaVu", "", "DejaVuSans.ttf", uni=True)
pdf.add_font("DejaVu", "B", "DejaVuSans-Bold.ttf", uni=True)
pdf.add_font("DejaVu", "I", "DejaVuSans-Oblique.ttf", uni=True)
pdf.set_auto_page_break(auto=True, margin=20)

# --- Kansikuva sivu ---
pdf.add_page()
# oletetaan, että kansikuva on tiedostona 'cover.jpg' samassa hakemistossa
pdf.image("cover.jpg", x=0, y=0, w=210)  # A4 leveys mm ≈210
pdf.ln(160)  # tyhjää tilaa kuvan jälkeen
pdf.set_font("DejaVu", "B", 16)
pdf.set_text_color(0, 51, 102)  # tumma sininen
pdf.cell(0, 10, "Yhteistä taivalta 27 vuotta takana.", ln=True, align="C")
pdf.cell(0, 10, "Jospa enemmän on vielä edessäpäin.", ln=True, align="C")
pdf.set_font("DejaVu", "", 14)
pdf.ln(10)
pdf.set_text_color(0, 0, 0)

# --- Aloitetaan sisältösivuista ---
for day in days:
    pdf.add_page()
    pdf.set_font("DejaVu", "B", 14)
    pdf.set_text_color(0, 51, 102)
    pdf.cell(0, 10, day["title"], ln=True)
    pdf.ln(2)

    pdf.set_font("DejaVu", "B", 12)
    pdf.set_text_color(0, 0, 0)
    pdf.cell(0, 8, "Aikataulu:", ln=True)
    pdf.set_font("DejaVu", "", 11)
    for time, action in day["schedule"]:
        pdf.cell(0, 6, f"  {time} – {action}", ln=True)

    pdf.ln(4)
    pdf.set_font("DejaVu", "B", 12)
    pdf.cell(0, 8, "Kohteet:", ln=True)
    pdf.set_font("DejaVu", "", 11)
    total_price = 0
    for place in day["places"]:
        lat, lon, price, note = location_dict[place]
        maps_url = f"https://maps.google.com/?q={lat},{lon}"
        price_text = f"{price} €" if price > 0 else "Ilmainen"
        price_color = (0, 150, 0) if price == 0 else (0, 0, 0)
        pdf.set_text_color(*price_color)
        pdf.cell(0, 8, f"• {place} – {price_text}", ln=True, link=maps_url)
        pdf.set_text_color(80, 80, 80)
        pdf.set_font("DejaVu", "I", 10)
        pdf.multi_cell(0, 6, f"   {note}")
        pdf.set_font("DejaVu", "", 11)
        total_price += price

    pdf.ln(2)
    pdf.set_text_color(0, 0, 0)
    pdf.set_font("DejaVu", "B", 11)
    pdf.cell(0, 8, f"Arvioitu päivän kokonaiskustannus: {total_price} €", ln=True)

    # Varakohteet
    if day.get("varakohteet"):
        pdf.ln(2)
        pdf.set_font("DejaVu", "B", 11)
        pdf.set_text_color(100, 100, 100)
        pdf.cell(0, 8, "Vaihtoehtoiset kohteet / varapäivät:", ln=True)
        pdf.set_font("DejaVu", "", 11)
        for alt_place in day["varakohteet"]:
            lat, lon, price, note = location_dict[alt_place]
            maps_url = f"https://maps.google.com/?q={lat},{lon}"
            price_text = f"{price} €" if price > 0 else "Ilmainen"
            pdf.cell(0, 6, f"• {alt_place} – {price_text}", ln=True, link=maps_url)
        pdf.set_text_color(0, 0, 0)

    # Ruokailut
    pdf.ln(4)
    pdf.set_font("DejaVu", "B", 11)
    pdf.set_text_color(0, 51, 102)
    pdf.cell(0, 8, "Ruokailu:", ln=True)
    pdf.set_font("DejaVu", "", 11)
    pdf.set_text_color(0, 0, 0)
    for meal in day["meals"]:
        pdf.cell(0, 6, f"• {meal}", ln=True)

    # Paljon tilaa seuraaville sivuille
    pdf.ln(10)

# --- Tallennus ---
pdf.output("korfu_matkasuunnitelma_ulkoasu.pdf")
