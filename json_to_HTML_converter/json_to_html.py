import json

class JSONToHTMLConverter:
    def __init__(self, json_file_path, html_file_path):
        
        self.json_file_path = json_file_path
        self.html_file_path = html_file_path

    def convert(self):
        
        try:
            data = self._read_json()
            html_content = "<html>\n<head>\n<title>JSON to HTML</title>\n</head>\n<body>\n"

            html_content += self._parse_json(data)
            html_content += "\n</body>\n</html>"

            self._write_html(html_content)

            print(f"HTML file has been created at: {self.html_file_path}")

        except Exception as e:
            print(f"An error occurred: {e}")

    def _read_json(self):

        with open(self.json_file_path, 'r') as json_file:
            return json.load(json_file)

    def _write_html(self, content):
    
        with open(self.html_file_path, 'w') as html_file:
            html_file.write(content)

    def _parse_json(self, data):
       
        if isinstance(data, dict):
            html = "<ul>"
            for key, value in data.items():
                html += f"<li><strong>{key}:</strong> {self._parse_json(value)}</li>"
            html += "</ul>"
            return html
        elif isinstance(data, list):
            html = "<ol>"
            for item in data:
                html += f"<li>{self._parse_json(item)}</li>"
            html += "</ol>"
            return html
        else:
            return str(data)
