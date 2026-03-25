from django.db import migrations

def populate_certificates(apps, schema_editor):
    Certificate = apps.get_model('main', 'Certificate')
    
    certs = [
        {
            'title': 'Advanced Computer Networks',
            'issuer': 'NPTEL',
            'topics': 'TCP/IP, Routing, Congestion Control, Network Security',
            'status': 'Certified',
            'certificate_link': 'https://archive.nptel.ac.in/content/noc/NOC25/SEM1/Ecertificates/106/noc25-cs02/Course/NPTEL25CS02S54750059104197989.pdf',
            'icon': 'fa-solid fa-certificate',
            'order': 0
        },
        {
            'title': 'Fundamental of Python',
            'issuer': 'Coursera',
            'topics': 'Basics of Python',
            'status': 'Certified',
            'certificate_link': 'https://www.coursera.org/account/accomplishments/verify/01D0PCKLLSJ4',
            'icon': 'fa-solid fa-certificate',
            'order': 1
        },
        {
            'title': 'Personality Development Essential Training',
            'issuer': 'Infosys',
            'topics': 'Professional Etiquette, Personality Development, Communication Skills',
            'status': 'Certified',
            'certificate_link': 'https://drive.google.com/file/d/1XGfvqwTczlCwozWVIivYZF6IKQK-hq7A/view',
            'icon': 'fa-solid fa-certificate',
            'order': 3
        }
    ]
    
    for cert_data in certs:
        Certificate.objects.get_or_create(
            title=cert_data['title'],
            issuer=cert_data['issuer'],
            defaults=cert_data
        )

def remove_certificates(apps, schema_editor):
    Certificate = apps.get_model('main', 'Certificate')
    titles = [
        'Advanced Computer Networks',
        'Fundamental of Python',
        'Personality Development Essential Training'
    ]
    Certificate.objects.filter(title__in=titles).delete()

class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_certificate_image'),
    ]

    operations = [
        migrations.RunPython(populate_certificates, remove_certificates),
    ]
