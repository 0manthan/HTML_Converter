import xml.etree.ElementTree as ET

class XMLToHTMLConverter:
    def __init__(self, xml_file_path, html_file_path):
       
        self.xml_file_path = xml_file_path
        self.html_file_path = html_file_path

    def convert(self):

        try:
            data = self._read_xml()

            html_content = "<html>\n<head>\n<title>XML to HTML</title>\n</head>\n<body>\n"
            html_content += self._parse_xml(data)
            html_content += "\n</body>\n</html>"

            self._write_html(html_content)

            print(f"HTML file has been created at: {self.html_file_path}")

        except Exception as e:
            print(f"An error occurred: {e}")

    def _read_xml(self):
       
        tree = ET.parse(self.xml_file_path)
        return tree.getroot()

    def _write_html(self, content):
       
        with open(self.html_file_path, 'w') as html_file:
            html_file.write(content)

    def _parse_xml(self, element):
        
        html = "<ul>"
        for child in element:
            html += f"<li><strong>{child.tag}:</strong> {self._parse_xml(child)}"  
            if child.text and child.text.strip():
                html += f" {child.text.strip()}"
            html += "</li>"
        html += "</ul>"
        return html
