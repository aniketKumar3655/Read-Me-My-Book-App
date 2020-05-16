from fpdf import FPDF
pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", size = 15)
pdf.cell(200, 10, txt = "Read me book app", ln = 1, align = 'C')
pdf.cell(200, 10, txt = "A FEW REALTIONS  IN EARTH NEVER DIES TAKE FIRST LETTER FROM EACH WORD TO GET THE WORD THAT YOU MEAN TO ME THANKS BEING THE BEST", ln = 2, align = 'C')
pdf.output("GFG.pdf")