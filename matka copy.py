from fpdf import FPDF

class TravelPDF(FPDF):
    def header(self):
        self.set_font("Arial", "B", 14)
        self.cell(0, 10, "7 Päivän Matkasuunnitelma  Korfu", ln=True, align="C")
        self.ln(5)

    def footer(self):
        self.set_y(-15)
        self.set_font("Arial", "I", 8)
        self.cell(0, 10, f"Sivu {self.page_no()}", 0, 0, "C")

pdf = TravelPDF()
pdf.set_auto_page_break(auto=True, margin=15)
pdf.add_page()
pdf.set_font("Arial", "", 11)

days = [
    {
        "title": "Päivä 1 - Saapuminen + lähialue tutuksi",
        "route": "Hotelli → Vlacherna Monastery → Pontikonisi näkymä → Hotelli",
        "mode": "Kävellen",
        "highlights": [
            "Saapuminen ja sisäänkirjautuminen",
            "Vlacherna Monastery",
            "Pontikonisi -näköalapaikka",
            "Lounas: Flisvos Seaside Café",
            "Illallinen: Captain George Tavern"
        ]
    },
    {
        "title": "Päivä 2 - Korfun vanhakaupunki & linnoitukset",
        "route": "Hotelli → Old Fortress → Liston → New Fortress → Hotelli",
        "mode": "Skootteri / bussi / taksi",
        "highlights": [
            "Old Fortress & Spianada-aukio",
            "Liston Promenadi",
            "New Fortress",
            "Lounas: Avli Restaurant",
            "Illallinen: Rosmarino Bistro"
        ]
    },
    {
        "title": "Päivä 3 - Achilleion + rantahetki",
        "route": "Hotelli → Achilleion → Benitses Beach → Hotelli",
        "mode": "Skootteri / taksi",
        "highlights": [
            "Achilleion Palace",
            "Benitses Beach",
            "Lounas: Taverna To Tsipouradiko",
            "Illallinen: Flisvos / hotellin oma"
        ]
    },
    {
        "title": "Päivä 4 - Kulttuuria ja puistoelämää",
        "route": "Hotelli → Kapodistrias-museo → Mon Repos → Garitsa Bay → Hotelli",
        "mode": "Skootteri / taksi",
        "highlights": [
            "Kapodistrias Museum & puutarha",
            "Mon Repos Palace & Durrell Garden",
            "Garitsa Bay",
            "Lounas: Nautilus Café",
            "Illallinen: Vanha kaupunki"
        ]
    },
    {
        "title": "Päivä 5 - Päiväretki Paleokastritsaan",
        "route": "Hotelli → Paleokastritsa → La Grotta → Hotelli",
        "mode": "Vuokra-auto",
        "highlights": [
            "Paleokastritsan luostari",
            "Rantapäivä + venematka",
            "Lounas: Taverna Nausika",
            "Illallinen: Hotelli tai kaupunki"
        ]
    },
    {
        "title": "Päivä 6 - Pantokratorin vuori ja kylävierailu",
        "route": "Hotelli → Pantokrator-vuori → Old Perithia → Hotelli",
        "mode": "Vuokra-auto",
        "highlights": [
            "Pantokrator-vuori",
            "Old Perithian kylä",
            "Lounas: Taverna Foros",
            "Illallinen: Venetian Well tai suosikkiuudelleen"
        ]
    },
    {
        "title": "Päivä 7 - Lähtöpäivä",
        "route": "Hotelli → Pontikonisi näkymä → Lentokenttä",
        "mode": "Kävellen / taksi",
        "highlights": [
            "Aamiainen & viimeinen kävely",
            "Kevyt lounas",
            "Lähtö lentokentälle"
        ]
    }
]

for day in days:
    pdf.set_font("Arial", "B", 12)
    pdf.cell(0, 10, day["title"], ln=True)
    pdf.set_font("Arial", "", 11)
    pdf.cell(0, 8, f"Reitti: {day['route']}", ln=True)
    pdf.cell(0, 8, f"Liikkumistapa: {day['mode']}", ln=True)
    pdf.cell(0, 8, "Päivän kohokohdat:", ln=True)
    for item in day["highlights"]:
        pdf.multi_cell(0, 8, f" - {item}")
    pdf.ln(5)

pdf.output("matkasuunnitelma.pdf")
