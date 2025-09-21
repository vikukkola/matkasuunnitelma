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

pdf.add_font("DejaVu", "", "DejaVuSans.ttf", uni=True)
pdf.add_font("DejaVu", "B", "DejaVuSans-Bold.ttf", uni=True)
pdf.add_font("DejaVu", "I", "DejaVuSans-Oblique.ttf", uni=True)
pdf.set_font("DejaVu", "", 11)
pdf.add_page()

place_links = {
    "Vlacherna Monastery": "https://maps.app.goo.gl/bTT7vE6bPavMDriM6",
    "Pontikonisi": "https://maps.app.goo.gl/cS1JjTyPZqVRSZsKA",
    "Old Fortress": "https://maps.app.goo.gl/7ofMhdRJfRUqA2dv8",
    "New Fortress": "https://maps.app.goo.gl/abfGxNEAQkEmyJFc9",
    "Liston": "https://maps.app.goo.gl/VHYAx2Ekm41DeGLY6",
    "Achilleion": "https://maps.app.goo.gl/s3XyD2AvCGLRxJqs5",
    "Benitses Beach": "https://maps.app.goo.gl/h3ZVSRyRDE5vEj6g7",
    "Kapodistrias Museum": "https://maps.app.goo.gl/Cbzj2FUwQAfY3TFo6",
    "Mon Repos": "https://maps.app.goo.gl/3yRK1F6QdcbGBzRj8",
    "Garitsa Bay": "https://maps.app.goo.gl/EgMdU2osUQqP4jU69",
    "Paleokastritsa": "https://maps.app.goo.gl/51N81Zw9UVddf9A68",
    "La Grotta": "https://maps.app.goo.gl/ggxE9nsyTGpyb6tX9",
    "Pantokrator": "https://maps.app.goo.gl/gMSjRrk7B2bAXrb88",
    "Old Perithia": "https://maps.app.goo.gl/TZq6duGqxApXZBsb7"
}

backup_ideas = {
    1: "Vinkki: Jos sataa, käy läheisessä kahvilassa tai pienessä museossa (esim. Casa Parlante).",
    2: "Vinkki: Sadekelillä korvaa Liston kävely museovierailulla (esim. Byzantine Museum).",
    3: "Vaihtoehto: Jos Achilleion on kiinni, käy Kaisers Throne -näköalapaikalla.",
    4: "Sadekeli: Vietä enemmän aikaa Mon Repos -museossa tai käy Archeological Museumissa.",
    5: "Huono sää: Jätä La Grotta väliin ja panosta Paleokastritsan luostariin ja akvaarioon.",
    6: "Huono sää: Käy sisämaassa Corfu Donkey Rescue -paikassa tai viinimaistajaisissa.",
    7: "Vinkki: Lentoa odotellessa voit käydä vielä Mon Reposin puistossa jos aikaa jää."
}

days = [
    {"title": "Päivä 1 - Saapuminen ja lähialue", "route": ["Vlacherna Monastery", "Pontikonisi"]},
    {"title": "Päivä 2 - Korfun vanhakaupunki", "route": ["Old Fortress", "Liston", "New Fortress"]},
    {"title": "Päivä 3 - Achilleion ja ranta", "route": ["Achilleion", "Benitses Beach"]},
    {"title": "Päivä 4 - Kulttuuri ja puistot", "route": ["Kapodistrias Museum", "Mon Repos", "Garitsa Bay"]},
    {"title": "Päivä 5 - Paleokastritsa-retki", "route": ["Paleokastritsa", "La Grotta"]},
    {"title": "Päivä 6 - Pantokrator & Old Perithia", "route": ["Pantokrator", "Old Perithia"]},
    {"title": "Päivä 7 - Lähtöpäivä", "route": ["Pontikonisi"]}
]

for i, day in enumerate(days, 1):
    pdf.set_font("DejaVu", "B", 12)
    pdf.cell(0, 10, f"{day['title']}", ln=True)
    pdf.set_font("DejaVu", "", 11)
    pdf.cell(0, 8, "Kohteet ja linkit:", ln=True)

    for place in day["route"]:
        url = place_links.get(place, "")
        if url:
            pdf.set_text_color(0, 0, 255)
            pdf.cell(0, 8, f"• {place}", ln=True, link=url)
        else:
            pdf.set_text_color(0, 0, 0)
            pdf.cell(0, 8, f"• {place}", ln=True)

    pdf.set_text_color(0, 0, 0)
    if i in backup_ideas:
        pdf.set_font("DejaVu", "I", 10)
        pdf.set_text_color(100, 100, 100)
        pdf.multi_cell(0, 8, f"{backup_ideas[i]}")
        pdf.set_text_color(0, 0, 0)

    pdf.ln(5)

pdf.output("korfu_matkasuunnitelma_laajennettu.pdf")
