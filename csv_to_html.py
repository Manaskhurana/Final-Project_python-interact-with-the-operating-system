#!/usr/bin/env python3
import csv
import sys

def csv_to_html(csv_filename, html_filename):
    # Open the CSV file
    with open(csv_filename, mode='r') as csv_file:
        csv_reader = csv.reader(csv_file)
        
        # Read the header row (first row)
        headers = next(csv_reader)
        
        # Start the HTML file
        with open(html_filename, mode='w') as html_file:
            html_file.write('<html>\n')
            html_file.write('<head><title>CSV to HTML</title></head>\n')
            html_file.write('<body>\n')
            html_file.write('<table border="1">\n')
            
            # Add headers to the table
            html_file.write('<tr>\n')
            for header in headers:
                html_file.write(f'<th>{header}</th>\n')
            html_file.write('</tr>\n')
            
            # Add rows to the table
            for row in csv_reader:
                html_file.write('<tr>\n')
                for column in row:
                    html_file.write(f'<td>{column}</td>\n')
                html_file.write('</tr>\n')

            # Close the table and HTML tags
            html_file.write('</table>\n')
            html_file.write('</body>\n')
            html_file.write('</html>\n')
            
    print(f"HTML file '{html_filename}' has been created.")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python csv_to_html.py <csv_file> <html_file>")
        sys.exit(1)
    
    csv_file = sys.argv[1]  # Input CSV file
    html_file = sys.argv[2]  # Output HTML file
    csv_to_html(csv_file, html_file)
