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

# Fontit: TTF-tiedostot pitää olla samassa kansiossa
pdf.add_font("DejaVu", "", "DejaVuSans.ttf", uni=True)
pdf.add_font("DejaVu", "B", "DejaVuSans-Bold.ttf", uni=True)
pdf.add_font("DejaVu", "I", "DejaVuSans-Oblique.ttf", uni=True)
pdf.set_font("DejaVu", "", 11)

pdf.add_page()

days = [
    {
        "title": "Päivä 1 - Saapuminen ja lähialue",
        "route": "Hotelli → Vlacherna Monastery → Pontikonisi → Hotelli",
        "mode": "Kävellen (~1.5 km/suunta)",
        "schedule": [
            ("14:00", "Saapuminen ja sisäänkirjautuminen"),
            ("16:00", "Kävely Vlacherna Monasterylle (n. 1 km)"),
            ("17:00", "Näkymät Pontikonisiin"),
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
            ("10:00", "Old Fortress ja Spianada-aukio"),
            ("12:00", "Liston promenadi, kahvitauko"),
            ("13:00", "Lounas: Avli Restaurant"),
            ("14:30", "New Fortress vierailu"),
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
            ("09:30", "Saapuminen ja kierros palatsissa"),
            ("11:00", "Siirtyminen Benitsesin rannalle (~4 km)"),
            ("11:30", "Rentoutumista rannalla"),
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
            ("09:30", "Lähtö Kapodistrias-museoon (~4 km)"),
            ("10:00", "Museokierros ja puutarhat"),
            ("11:30", "Mon Repos -puisto ja museo"),
            ("13:00", "Lounas: Nautilus Café (Garitsa Bay)"),
            ("14:30", "Kävelyä Garitsa Bayssä"),
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
            ("09:30", "Luostari ja näköalat"),
            ("11:00", "La Grotta -rantakallio ja uiminen"),
            ("13:00", "Lounas: Taverna Nausika"),
            ("15:00", "Rentoutumista rannalla / veneretki"),
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
            ("09:00", "Maisemat ja valokuvaus huipulla"),
            ("10:30", "Siirtyminen Old Perithiaan (~8 km)"),
            ("11:00", "Kyläkävely ja historiaa"),
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
            ("09:00", "Viimeinen kävely Pontikonisille"),
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
        pdf.multi_cell(0, 8, f" {time} – {event}")
    pdf.ln(5)

pdf.output("korfu_matkasuunnitelma_unicode_aikataulu.pdf")
