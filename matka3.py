from fpdf import FPDF

class TravelPDF(FPDF):
    def header(self):
        self.set_font("DejaVu", "B", 14)
        self.cell(0, 10, "7 Päivän Matkasuunnitelma – Korfu", ln=True, align="C")
        self.ln(5)

    def footer(self):
        self.set_y(-15)
        self.set_font("DejaVu", "I", 8)
        self.cell(0, 10, f"Sivu {self.page_no()}", 0, 0, "C")

pdf = TravelPDF()
pdf.set_auto_page_break(auto=True, margin=15)

# Fontit (TTF-tiedostot samassa kansiossa)
pdf.add_font("DejaVu", "", "DejaVuSans.ttf", uni=True)
pdf.add_font("DejaVu", "B", "DejaVuSans-Bold.ttf", uni=True)
pdf.add_font("DejaVu", "I", "DejaVuSans-Oblique.ttf", uni=True)
pdf.set_font("DejaVu", "", 11)
pdf.add_page()

# Päiväkohtainen suunnitelma, sisältäen maksulliset/ilmaiset kohteet
days = [
    {
        "title": "Päivä 1 - Saapuminen ja lähialue",
        "route": "Hotelli → Vlacherna Monastery → Pontikonisi → Hotelli",
        "mode": "Kävellen (~1.5 km/suunta)",
        "schedule": [
            ("14:00", "Saapuminen ja sisäänkirjautuminen"),
            ("16:00", "Kävely Vlacherna Monasterylle (n. 1 km) – ILMAINEN"),
            ("17:00", "Näkymät Pontikonisiin – ILMAINEN"),
            ("18:30", "Paluukävely hotellille"),
            ("19:30", "Illallinen: Captain George Tavern")
        ]
    },
    {
        "title": "Päivä 2 - Korfun vanhakaupunki",
        "route": "Hotelli → Old Fortress → Liston → New Fortress → Hotelli",
        "mode": "Skootteri / bussi (~4-5 km)",
        "schedule": [
            ("09:30", "Lähtö hotellilta vanhaankaupunkiin"),
            ("10:00", "Old Fortress – n. 6 €"),
            ("12:00", "Liston promenadi, kahvitauko – ILMAINEN"),
            ("13:00", "Lounas: Avli Restaurant"),
            ("14:30", "New Fortress – ILMAINEN"),
            ("16:00", "Vapaata kiertelyä kaupungissa"),
            ("18:00", "Paluumatka hotellille"),
            ("20:00", "Illallinen: Rosmarino Bistro")
        ]
    },
    {
        "title": "Päivä 3 - Achilleion ja ranta",
        "route": "Hotelli → Achilleion → Benitses Beach → Hotelli",
        "mode": "Skootteri / taksi (~10 km)",
        "schedule": [
            ("09:00", "Lähtö kohti Achilleionin palatsia"),
            ("09:30", "Achilleion-palatsi – n. 10 €"),
            ("11:00", "Benitses Beach – ILMAINEN"),
            ("13:00", "Lounas: Taverna To Tsipouradiko"),
            ("15:00", "Paluumatka hotellille"),
            ("20:00", "Illallinen hotellilla tai lähistöllä")
        ]
    },
    {
        "title": "Päivä 4 - Kulttuuri ja puistot",
        "route": "Hotelli → Kapodistrias-museo → Mon Repos → Garitsa Bay → Hotelli",
        "mode": "Skootteri / taksi (~6-8 km)",
        "schedule": [
            ("09:30", "Kapodistrias-museo – n. 5 €"),
            ("11:00", "Mon Repos -puisto ja museo – n. 4 €"),
            ("13:00", "Lounas: Nautilus Café (Garitsa Bay)"),
            ("14:30", "Garitsa Bay – ILMAINEN"),
            ("16:00", "Paluumatka hotellille"),
            ("20:00", "Illallinen kaupungissa")
        ]
    },
    {
        "title": "Päivä 5 - Paleokastritsa-retki",
        "route": "Hotelli → Paleokastritsa → La Grotta → Hotelli",
        "mode": "Vuokra-auto (~25 km/suunta)",
        "schedule": [
            ("08:30", "Lähtö Paleokastritsaan"),
            ("09:30", "Luostari – ILMAINEN"),
            ("11:00", "La Grotta -rantakallio – ILMAINEN"),
            ("13:00", "Lounas: Taverna Nausika"),
            ("15:00", "Veneretki luolille – n. 10 €"),
            ("17:00", "Paluumatka hotellille"),
            ("20:00", "Illallinen hotellilla tai keskustassa")
        ]
    },
    {
        "title": "Päivä 6 - Pantokrator & Old Perithia",
        "route": "Hotelli → Pantokrator → Old Perithia → Hotelli",
        "mode": "Vuokra-auto (~30 km/suunta)",
        "schedule": [
            ("08:00", "Lähtö Pantokrator-vuorelle"),
            ("09:00", "Pantokrator – ILMAINEN"),
            ("10:30", "Old Perithia – ILMAINEN"),
            ("13:00", "Lounas: Taverna Foros"),
            ("14:30", "Paluumatka hotellille"),
            ("20:00", "Illallinen: Venetian Well tai muu suosikki")
        ]
    },
    {
        "title": "Päivä 7 - Lähtöpäivä",
        "route": "Hotelli → Pontikonisi näkymä → Lentokenttä",
        "mode": "Kävellen / taksi (~2 km)",
        "schedule": [
            ("08:00", "Aamiainen ja uloskirjautuminen"),
            ("09:00", "Viimeinen kävely Pontikonisille – ILMAINEN"),
            ("10:00", "Matkatavaroiden nouto"),
            ("10:30", "Lähtö lentokentälle")
        ]
    }
]

for day in days:
    pdf.set_font("DejaVu", "B", 12)
    pdf.cell(0, 10, day["title"], ln=True)
    pdf.set_font("DejaVu", "", 11)
    pdf.multi_cell(0, 8, f"Reitti: {day['route']}")
    pdf.cell(0, 8, f"Liikkumistapa: {day['mode']}", ln=True)
    pdf.cell(0, 8, "Aikataulu:", ln=True)
    for time, event in day["schedule"]:
        # Korosta ilmaiset ja edulliset kohteet
        if "ILMAINEN" in event or "n. 5 €" in event or "n. 4 €" in event:
            pdf.set_text_color(0, 128, 0)  # vihreä
        else:
            pdf.set_text_color(0, 0, 0)  # musta
        pdf.multi_cell(0, 8, f" {time} – {event}")
    pdf.set_text_color(0, 0, 0)
    pdf.ln(5)

pdf.output("korfu_matkasuunnitelma_hinnoilla.pdf")
