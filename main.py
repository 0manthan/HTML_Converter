from xml_to_HTML_Converter import xml_to_html
from json_to_HTML_Converter import json_to_html

class main():
    user=0
    while user!=3:
        print("CHOOSE OPERATION\n1.convert XML file to HTML file\n2.convert JSON file to HTML file\n3.EXIT")
        user=int(input("Enter choice:"))
        if user==2:
            converter =json_to_html.JSONToHTMLConverter('D:\zensar.py\HTML_CONVERTER\sample1.json', 'D:\\zensar.py\\HTML_CONVERTER\\converted_files\\jsontohtml.html')
            converter.convert()
        elif user==1:
            converter =xml_to_html.XMLToHTMLConverter('D:\zensar.py\HTML_CONVERTER\sample_CustomersOrders.xml', 'D:\\zensar.py\\HTML_CONVERTER\\converted_files\\xmltohtml.html')
            converter.convert()
        else:
            exit()
c=main()