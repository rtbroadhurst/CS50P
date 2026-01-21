# Prompts the user for their name and generates a shirt with their name + took cs50 as a PDF

from fpdf import FPDF

def main():
    name = input("Name: ").strip()

    pdf = FPDF(orientation="P", unit="mm", format="A4")
    pdf.add_page()

    pdf.set_font("Helvetica", "B", 36)
    pdf.cell(0, 20, "CS50 Shirtificate", align="C", new_x="LMARGIN", new_y="NEXT")

    img_path = "shirtificate.png"
    img_w = 180 
    x = (pdf.w - img_w) / 2
    y = 60
    pdf.image(img_path, x=x, y=y, w=img_w) 

    pdf.set_font("Helvetica", "B", 24)
    pdf.set_text_color(255, 255, 255)
    pdf.set_xy(0, y + 65)     
    pdf.cell(0, 10, f"{name} took CS50", align="C") 

    pdf.output("shirtificate.pdf")


if __name__ == "__main__":
    main()
