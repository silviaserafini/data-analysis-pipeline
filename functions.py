import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import email, smtplib, ssl
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from fpdf import FPDF 

def plotTime(df_analysis):
    df_analysis["2MONTHS_BINS"] = pd.cut(df_analysis.MONTH, bins=[0,2,4,6,8,10,12],
                     labels=['01-02','03-04','05-06','07-08','09-10','11-12'])
    res = df_analysis.groupby("2MONTHS_BINS").agg({"ARR_DELAY": "mean","DEP_DELAY":"mean"})
    res1=res.plot.bar()
    fig=res1.get_figure()
    fig.subplots_adjust(bottom=0.2)
    plt.title('Avarage dealays [2 months bins]')
    plt.show()
    fig.savefig('SRC/plot.jpg')
    res.to_csv("SRC/2monthsbins.csv")
    
    return res
    
def plotAirline(df1):
    res=df1.groupby("AIRLINE_NAME").agg({"ARR_DELAY": "mean","DEP_DELAY":"mean"}).reset_index().set_index('AIRLINE_NAME').sort_values('ARR_DELAY')
    res1=res.plot.bar()
    fig=res1.get_figure()
    fig.subplots_adjust(bottom=0.5)
    ax_list = fig.axes
    plt.title('Airlines avarage Delays')
    plt.show()
    fig.savefig('SRC/plotAirline.jpg')
    res.to_csv("SRC/airlines.csv")
    
    return res

def plotBestAirport(df1):
    res=df1.groupby("AIRPORT_NAME").agg({"ARR_DELAY": "mean","DEP_DELAY":"mean"}).reset_index().set_index('AIRPORT_NAME').sort_values('ARR_DELAY')[0:5]
    res1=res.plot.bar()
    fig=res1.get_figure()
    fig.subplots_adjust(bottom=0.5)
    plt.title('BestAirport avarage Delays')
    plt.show()
    fig.savefig('SRC/airport.jpg')
    res.to_csv("SRC/airport.csv")
    
    return res

def plotWorstAirport(df1):
    res=df1.groupby("AIRPORT_NAME").agg({"ARR_DELAY": "mean","DEP_DELAY":"mean"}).reset_index().set_index('AIRPORT_NAME').sort_values('ARR_DELAY',ascending=False)[0:5]
    res1=res.plot.bar()
    fig=res1.get_figure()
    fig.subplots_adjust(bottom=0.5)
    plt.title('WorstAirport avarage Delays')
    plt.show()
    fig.savefig('SRC/airport.jpg')
    res.to_csv("SRC/airport.csv")
    return res

def tableColumns(df):
    for col in df.columns:
        yield col

def tableValues(df):
    for _,row in df.iterrows():
        yield row

# Create an instance of `FPDF` to use it's methods
# It is created outside of the function, because otherwise
# it would generate a new object every time you called `fit_word`
ver = FPDF()
def fit_word(string,cell_w,font_type):
    ver.set_font(**font_type)
    width = ver.get_string_width(string)
    if ver.get_string_width(string)<cell_w:
        return string
    while ver.get_string_width(string)>=cell_w:
        string = string[:-1]
    string = string[:-3] + "..."
    return string 
    
# Dictionaries for 2 font settings and 3 color settings
# Usefull for changing settings without having to go through code.
font_type_table_header = {"family":"Arial", "style":"B", "size":12}
font_type_table_body = {"family":"Arial", "style":"", "size":8}
white= (255,255,255)
green = (10,188,87)
yellow = (250,239,133)

def sendMail(mailAddress, filename, bodyText):
    subject = "An email with attachment from Python"
    body = bodyText
    sender_email = "tzvuccyseraf@gmail.com"
    receiver_email = "tzvuccyseraf@gmail.com"
    password = input("Type your password and press enter:")

    # Create a multipart message and set headers
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject
    message["Bcc"] = receiver_email  # Recommended for mass emails

    # Add body to email
    message.attach(MIMEText(body, "plain"))

    # Open PDF file in binary mode
    with open(filename, "rb") as attachment:
        # Add file as application/octet-stream
        # Email client can usually download this automatically as attachment
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read())

    # Encode file in ASCII characters to send by email    
    encoders.encode_base64(part)

    # Add header as key/value pair to attachment part
    part.add_header(
        "Content-Disposition",
        f"attachment; filename= {filename}",
    )

    # Add attachment to message and convert message to string
    message.attach(part)
    text = message.as_string()

    # Log in to server using secure context and send email
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, text)

    