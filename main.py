from myGui.myApp import MyApp
import datetime

from fpdf import FPDF

from mocks.dummyConsts import detailsFclQuoteDummy as d

fullNameHelper = f"{d.clientName['firstName']} {d.clientName['lastName']}"
textForOpening = f"From {d.portOrigin} to {d.portDestination}"
todayDate = datetime.datetime.now().date()


# ln:
# Indicates where the current position should go after the call. Possible values are:
#
# 0: to the right
# 1: to the beginning of the next line
# 2: below
# Putting 1 is equivalent to putting 0 and calling ln just after. Default value: 0.

# align = 'l' | 'c' | 'r'
def main():
    app = MyApp()
    app.Main_Loop()
    pass


def play():
    print("entered play..")
    pdf = FPDF("P", "mm")
    pdf.add_page()
    pdf.set_font(family='helvetica', style='', size=12)

    # date
    pdf.cell(w=0, h=10, txt=str(todayDate), border=0, ln=True)

    # For title
    pdf.cell(w=0, h=10, txt=" " * 17 + fullNameHelper, border=0, ln=1)
    pdf.cell(w=0, h=10, txt=" " * 17 + d.companyName, border=0, ln=1)

    # Main title
    pdf.cell(w=0, h=10, txt=f'{d.terms}', align='C', border=0, ln=1)
    pdf.cell(w=0, h=10, txt=textForOpening, align='l', border=0, ln=1)

    # FobmMain rate prices
    pdf.set_font(family='helvetica', style='', size=11)
    pdf.cell(w=0, h=10, txt="Freight", align='l', border=0, ln=1)
    pdf.set_font(family='helvetica', style='', size=10)
    for container in d.containerForQuote:
        pdf.cell(w=0, h=10, txt=" " * 10 + container + " " + str(d.ratesForClient[container]) + "$", align='l',
                 border=0, ln=1)

    # Extra taxes
    pdf.set_font(family='helvetica', style='', size=11)
    pdf.cell(w=0, h=10, txt="Extra fees", align='l', border=0, ln=1)
    pdf.set_font(family='helvetica', style='', size=10)
    for _, tax in d.extraTaxes.items():
        pdf.cell(w=0, h=10, txt=" " * 10 + tax['taxName'] + " : " + str(tax['value']) + tax['currency'], align='l',
                 border=0, ln=1)

    pdf.output('pdf1.pdf')

    print("done playing..")


if __name__ == '__main__':
    main()
    # play()
    pass