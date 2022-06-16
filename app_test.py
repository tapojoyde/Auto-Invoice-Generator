# +
import requests

url = 'http://127.0.0.1:5000/'
data = {
    'invoice_number': 15665,
    'duedate': 'December 1, 2022',
    'from_addr': {
        'company_name': 'Python Projects',
        'addr1': '18 Mt Alexander Rd, Flemington',
        'addr2': 'Melbourne, VIC 3032'
    },
    'to_addr': {
        'company_name': 'My Company Inc.',
        'person_name': 'Tapojoy De',
        'person_email': 'tdjoy@example.com'
    },
    'items': [{
        'title': 'Brochure Designing',
        'charge': 900.0
    }, {
        'title': 'Hosting (6 months)',
        'charge': 550.0
    }, {
        'title': 'Domain name (1 year)',
        'charge': 200.0
    }]
}

html = requests.post(url, json=data)

with open('invoice_test.pdf', 'wb') as f:
    f.write(html.content)
