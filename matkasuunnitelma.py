from fpdf import FPDF
import os

# Luodaan romanttinen PDF-suunnitelma otsikolla ja kansikuvalla
class RomanticTravelPDF(FPDF):
    def header(self):
        if self.page_no() == 1:
            return
        if os.path.exists("tausta_haalea.png"):
            self.image("tausta_haalea.png", x=0, y=0, w=210, h=297)

    def footer(self):
        self.set_y(-15)
        self.set_font("DejaVu", "I", 8)
        self.set_text_color(150, 150, 150)
        self.cell(0, 10, f"Sivu {self.page_no()}", 0, 0, "C")

# Aloitetaan PDF
pdf = RomanticTravelPDF()
pdf.add_font("DejaVu", "", "DejaVuSans.ttf", uni=True)
pdf.add_font("DejaVu", "B", "DejaVuSans-Bold.ttf", uni=True)
pdf.add_font("DejaVu", "I", "DejaVuSans-Oblique.ttf", uni=True)
pdf.set_auto_page_break(auto=True, margin=20)

# Kansikuva
pdf.add_page()
if os.path.exists("cover.jpg"):
    pdf.image("cover.jpg", x=0, y=0, w=210)
pdf.ln(160)
pdf.set_font("DejaVu", "B", 16)
pdf.set_text_color(179, 0, 89)  # romanttinen pinkinpunainen
pdf.multi_cell(0, 10,
    "Yhteistä taivalta 27 vuotta takana.\nJospa enemmän on vielä edessäpäin.\nKiitos yhteisistä päivistä rakas ja ihana vaimoni Paula!",
    align="C")

# Esimerkkisivu
pdf.add_page()
if os.path.exists("tausta_haalea.png"):
    pdf.image("tausta_haalea.png", x=0, y=0, w=210, h=297)

pdf.set_font("DejaVu", "B", 14)
pdf.set_text_color(179, 0, 89)
pdf.cell(0, 10, "Päivä 1 – Saapuminen ja lähialue", ln=True)
pdf.set_text_color(0, 0, 0)
pdf.set_font("DejaVu", "", 12)
pdf.ln(5)
pdf.multi_cell(0, 8, "• Vlacherna Monastery – Ilmainen\n  Kaunis pieni luostari sillan päässä.\n• Pontikonisi – 3 €\n  Tunnettu hiirisaari, pieni veneretki.\n\nVaihtoehtoinen kohde:\n• Liston – Ilmainen\n  Romanttinen kävely kahviloiden vieressä.\n\nAikataulu:\n14:00 – Saapuminen ja sisäänkirjautuminen\n16:00 – Vlacherna Monastery\n17:00 – Pontikonisi\n\nRuokailu:\n• Kevyt päivällinen hotellin lähistöllä")

# Tallennus
pdf.output("korfu_matkasuunnitelma_romanttinen.pdf")
