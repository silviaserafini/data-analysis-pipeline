# data-analysis-pipeline project

<img src="SRC/download.jpg" />

BRIEF DESCRIPTION:

Data analysis of 2018 USA flights delays Database and PDF report generation sent via e-mail.

##CONTENTS:

cleaning.ipynb:

    INPUT: 
        database 2018.csv
        https://www.kaggle.com/yuanyuwendymu/airline-delay-and-cancellation-data-2009-2018#2018.csv

    OUTPUT: 
        cleaned database delays_clean.csv

main.py:

###INPUT:
  -b, --best            flag: show the data related to the fastest operators
                        (if false, show the slowest operators)
                        
  -y, --depDelay        flag: show the data related to departure delays (if
                        False, show arrival delays)
                        
  -a ARRAIRPORT,  --arrAirport ARRAIRPORT       landing airport [IATA code]
                        
                        
  -d DEPAIRPORT,  --depAirport DEPAIRPORT       departure airport [IATA code]
                        
                        
  -c AIRLINECODE, --airlineCode AIRLINECODE     airline [2 characters IATA code]
                        
                        
###OUTPUT:  
    USA DOMESTIC FLIGHTS 2018 DELAYS PDF report, sent via e-mail
        
        
reportL4.py: fuction that crates the report
generatePDF.py: funtion that generates the PDF report
functions.py: other support functions


