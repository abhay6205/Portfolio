"""Data migration: populate Projects and Blogs from previously hardcoded content."""

from django.db import migrations
from django.utils import timezone


def populate_data(apps, schema_editor):
    Project = apps.get_model('main', 'Project')
    Blog = apps.get_model('main', 'Blog')

    # ── Projects ─────────────────────────────────────────────────────────
    Project.objects.get_or_create(
        title='Online Mentor Platform',
        defaults={
            'description': (
                'An ML-powered mentor-mentee matching platform built with Python. Uses EDA to '
                'reduce data preprocessing time by 18%, and a clustering-based recommendation '
                'model that analyzes user interests, skills, and expertise to improve match '
                'accuracy by ~20%. Integrates K-Means, TF-IDF, and data preprocessing pipelines '
                'with a Streamlit web interface, boosting user interaction efficiency by 30%.'
            ),
            'tech_stack': 'Python, Machine Learning, K-Means, TF-IDF, Streamlit, EDA',
            'github_link': 'https://github.com/abhay6205/mentor-mentee_matching',
            'live_link': '',
            'order': 1,
        },
    )
    Project.objects.get_or_create(
        title='Real-Time Process Monitoring Dashboard',
        defaults={
            'description': (
                'A real-time monitoring dashboard displaying process states, CPU load, and memory '
                'usage, enabling administrators to detect issues 30% faster. Features a '
                'cross-platform GUI built with Python and Tkinter, integrating os and psutil '
                'modules for seamless system monitoring. Optimized performance by 10% through '
                'efficient filtering, configurable refresh rates, and time-series tracking.'
            ),
            'tech_stack': 'Python, Tkinter, psutil, System Monitoring, GUI',
            'github_link': 'https://github.com/abhay6205/Real-Time-Process-Management-Dashboard',
            'live_link': '',
            'order': 2,
        },
    )

    # ── Blogs ────────────────────────────────────────────────────────────
    Blog.objects.get_or_create(
        title='What I Learned During My AI & ML Industry Training with IBM',
        defaults={
            'content': (
                'This summer, I had the incredible opportunity to undergo an industry training '
                'program in Artificial Intelligence and Machine Learning at Allsoft Solutions, '
                'partnered with IBM. Over two intensive months, I went from understanding basic '
                'data preprocessing to building and evaluating full machine learning models. I '
                'performed EDA using NumPy and Pandas, trained models like Linear Regression, '
                'Decision Trees, K-Means, and Ensemble Methods with Scikit-learn, and applied '
                'feature engineering to boost model performance by 20%. This experience gave me '
                'a solid foundation in applying AI/ML to real-world problems and solidified my '
                'passion for data-driven solutions.'
            ),
            'is_published': True,
        },
    )
    Blog.objects.get_or_create(
        title='My Full Stack Journey: From Python Basics to Cloud Deployment',
        defaults={
            'content': (
                'During my Winter PEP training at LPU with Algotutor, I embarked on a '
                'comprehensive journey through the Python full-stack ecosystem. Starting with '
                'core Python concepts - functions, OOP, exception handling - I quickly progressed '
                'to building web applications with Django, creating REST APIs, setting up CI/CD '
                'pipelines with GitHub Actions, and containerizing applications with Docker. The '
                'most rewarding part was seeing how all these pieces fit together: writing clean '
                'Python code, structuring it into a Django project, exposing it via APIs, and '
                'deploying it to the cloud. This training transformed my understanding of modern '
                'software development workflows.'
            ),
            'is_published': True,
        },
    )


def reverse_data(apps, schema_editor):
    Project = apps.get_model('main', 'Project')
    Blog = apps.get_model('main', 'Blog')
    Project.objects.filter(
        title__in=['Online Mentor Platform', 'Real-Time Process Monitoring Dashboard']
    ).delete()
    Blog.objects.filter(
        title__in=[
            'What I Learned During My AI & ML Industry Training with IBM',
            'My Full Stack Journey: From Python Basics to Cloud Deployment',
        ]
    ).delete()


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_populate_education_experience'),
    ]

    operations = [
        migrations.RunPython(populate_data, reverse_data),
    ]
