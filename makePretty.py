from fpdf import FPDF 

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