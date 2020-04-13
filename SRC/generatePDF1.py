    
from fpdf import FPDF 
import pandas as pd
# importing modules
from SRC.functionsToGenerateReportAndSendMail import *

def generatePDF1():

    #load the dataframe datas
    data = pd.read_csv (r"SRC/2monthsbins.csv", encoding='latin-1')
    df1 = pd.DataFrame(data)

    data = pd.read_csv (r"SRC/airlines.csv", encoding='latin-1')
    df2 = pd.DataFrame(data)

    data = pd.read_csv (r"SRC/airport.csv", encoding='latin-1')
    df3 = pd.DataFrame(data)

    # Generate FPDF object and add page
    # FPDF(orientation, unit, format)
    pdf = FPDF("P","mm","A4")
    pdf.add_page()

    pdf.set_font("Arial", "B", 16)
    pdf.cell(0,10,"USA DOMESTIC FLIGHTS DELAYS 2018",1,1,"C")

    pdf.set_font("Arial", "B", 14)
    pdf.cell(95,10,"",0,1,"C")
    pdf.cell(45,10,"Avarage Delays [minutes]",0,1,'L')
    pdf.cell(95,10,"",0,1,"L")

    #print the table df1

    cols = list(tableColumns(df1))
    num_cols = len(cols)
    A4_width = 210
    l_margin = 10
    r_margin = 10
    useful_page_width = A4_width-l_margin-r_margin

    pdf.set_font(**font_type_table_header)
    cell_width = useful_page_width/num_cols

    # Printing Header
    for col in cols:
        pdf.cell(cell_width,8,col.upper(),1,0,"C")
    # Add line break after printing whole line
    pdf.ln()

    # Printing Body
    # Set border width
    pdf.set_line_width(0.1)
    pdf.set_font(**font_type_table_body)
    for row in tableValues(df1): 
        for val in row:
            pdf.cell(cell_width,5,fit_word(str(val),cell_width,font_type_table_body),1,0,"C")
        pdf.ln()

    pdf.set_xy(25,120)
    pdf.image("SRC/plot.jpg", x = 25, y = None, w = 160, h = 0)

    #####################################################################
    pdf.add_page()
    pdf.set_font("Arial", "B", 16)
    pdf.cell(0,10," Avarage Delays/Airlines [minutes]",1,1,"C")

    pdf.set_font("Arial", "B", 14)
    pdf.cell(95,10,"",0,1,"C")
    pdf.cell(45,10,"Avarage Delays/Airlines [minutes]",0,1,'L')
    pdf.cell(95,10,"",0,1,"L")

    #print the table df2

    cols = list(tableColumns(df2))
    num_cols = len(cols)
    A4_width = 210
    l_margin = 10
    r_margin = 10
    useful_page_width = A4_width-l_margin-r_margin

    pdf.set_font(**font_type_table_header)
    cell_width = useful_page_width/num_cols

    # Printing Header
    for col in cols:
        pdf.cell(cell_width,8,col.upper(),1,0,"C")
    # Add line break after printing whole line
    pdf.ln()

    # Printing Body
    # Set border width
    pdf.set_line_width(0.1)
    pdf.set_font(**font_type_table_body)
    for row in tableValues(df2): 
        for val in row:
            pdf.cell(cell_width,5,fit_word(str(val),cell_width,font_type_table_body),1,0,"C")
        pdf.ln()

    pdf.set_xy(25,155)
    pdf.image("SRC/plotAirline.jpg", x = 25, y = None, w = 160, h = 0)


    #####################################################################
    pdf.add_page()
    pdf.set_font("Arial", "B", 16)
    pdf.cell(0,10," Avarage Delays/Airports [minutes]",1,1,"C")

    pdf.set_font("Arial", "B", 14)
    pdf.cell(95,10,"",0,1,"C")
    pdf.cell(45,10,"Avarage Delays/Airports [minutes]",0,1,'L')
    pdf.cell(95,10,"",0,1,"L")

    #print the table df3

    cols = list(tableColumns(df2))
    num_cols = len(cols)
    A4_width = 210
    l_margin = 10
    r_margin = 10
    useful_page_width = A4_width-l_margin-r_margin

    pdf.set_font(**font_type_table_header)
    cell_width = useful_page_width/num_cols

    # Printing Header
    for col in cols:
        pdf.cell(cell_width,8,col.upper(),1,0,"C")
    # Add line break after printing whole line
    pdf.ln()

    # Printing Body
    # Set border width
    pdf.set_line_width(0.1)
    pdf.set_font(**font_type_table_body)
    for row in tableValues(df2): 
        for val in row:
            pdf.cell(cell_width,5,fit_word(str(val),cell_width,font_type_table_body),1,0,"C")
        pdf.ln()

    pdf.set_xy(25,155)
    pdf.image("SRC/airport.jpg", x = 25, y = None, w = 160, h = 0)

    # Save File
    pdf.output("OUTPUT/report.pdf","F")