from flask import Flask, request, render_template, send_file
import io
import os
from datetime import datetime
from weasyprint import HTML

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True

@app.route('/', methods = ['GET', 'POST'])
def hello_world():
    posted_data = request.get_json() or {}
    today = datetime.today().strftime("%B %d, %Y")
    default_data = {
        'invoice_number': 25678,
        'duedate': 'August 1, 2023',
        'from_addr': {
            'company_name': 'GitHub Inc.',
            'addr1': '88 Colin P Kelly Jr St',
            'addr2': 'San Francisco, CA 94107'            
        },
        'to_addr': {
            'company_name': 'Stack Overflow Ltd.',
            'person_name': 'Prashanth Chandrasekar',
            'person_email': 'prashanthc@example.com'            
        },
        'items': [{
                'title': 'Website Designing',
                'charge': 1000.0
            },
            {
                'title': 'Hosting (3 months)',
                'charge': 650.0
            },
            {
                'title': 'Domain Name (1 year)',
                'charge': 200.0
            }
        ]
    }
    invoice_number = posted_data.get('invoice_number', default_data['invoice_number'])
    duedate = posted_data.get('duedate', default_data['duedate'])
    from_addr = posted_data.get('from_addr', default_data['from_addr'])
    to_addr = posted_data.get('to_addr', default_data['to_addr'])
    items = posted_data.get('items', default_data['items'])
    
    total = sum([i['charge'] for i in items])

    rendered = render_template('invoice.html', 
                            date = today,
                            invoice_number = invoice_number,
                            duedate = duedate,
                            from_addr = from_addr,
                            to_addr = to_addr,
                            items = items,
                            total = total                            
                            )
    html = HTML(string=rendered)
    print(rendered)
    rendered_pdf = html.write_pdf()
    return send_file(
            io.BytesIO(rendered_pdf),
            download_name='invoice.pdf'
        )

if __name__ == "__main__":
    app.run(debug=True, use_reloader=True)
