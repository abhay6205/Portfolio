"""Data migration: populate Education and Experience from previously hardcoded content."""

from django.db import migrations


def populate_data(apps, schema_editor):
    Education = apps.get_model('main', 'Education')
    Experience = apps.get_model('main', 'Experience')

    # ── Education entries ────────────────────────────────────────────────
    Education.objects.get_or_create(
        institution='Lovely Professional University',
        defaults={
            'degree': 'B.Tech in Computer Science and Engineering',
            'duration': 'August 2023 - Present',
            'description': (
                'Currently pursuing my Bachelor\'s degree with a focus on core computer '
                'science subjects, data structures, and algorithms. Maintaining a strong '
                'academic record with a current CGPA of 8.16.'
            ),
            'order': 1,
        },
    )
    Education.objects.get_or_create(
        institution='Kisan College',
        defaults={
            'degree': 'Intermediate (Class XII)',
            'duration': 'March 2020 - March 2022',
            'description': (
                'Completed my Higher Secondary education in Science stream. '
                'Secured 76.6% in the final board examinations.'
            ),
            'order': 2,
        },
    )
    Education.objects.get_or_create(
        institution='Prerna Punj Public School',
        defaults={
            'degree': 'Matriculation (Class X)',
            'duration': 'March 2019 - March 2020',
            'description': (
                'Completed my secondary education with a focus on foundational subjects. '
                'Secured 79% in the final board examinations.'
            ),
            'order': 3,
        },
    )

    # ── Experience entries ───────────────────────────────────────────────
    Experience.objects.get_or_create(
        organization='Algotutor',
        defaults={
            'role': 'Winter Training — Python Full Stack + Cloud Computing',
            'duration': 'January 2026 – February 2026',
            'description': (
                'Comprehensive training covering Python fundamentals (functions, conditional '
                'statements, exception handling, OOP), followed by full-stack web development '
                'with Django and REST APIs. Gained hands-on experience with CI/CD using GitHub '
                'Actions, containerization with Docker, and cloud computing concepts. Built and '
                'deployed multiple real-world applications throughout the program.'
            ),
            'partner_label': 'LPU Winter PEP Training',
            'github_link': 'https://github.com/abhay6205/Winter_pep_training',
            'order': 1,
        },
    )
    Experience.objects.get_or_create(
        organization='Allsoft Solutions',
        defaults={
            'role': 'Industry Training — AI & Machine Learning',
            'duration': 'June 2025 – July 2025',
            'description': (
                'Performed Exploratory Data Analysis (EDA) using NumPy and Pandas, reducing '
                'data preprocessing time by 15%. Developed, trained, and evaluated ML models — '
                'including Linear Regression, Decision Trees, K-Means, and Ensemble Methods '
                'using Scikit-learn, achieving a 10% improvement in model accuracy. Applied '
                'feature engineering techniques that enhanced predictive model performance by 20%.'
            ),
            'partner_label': 'Partnered with IBM',
            'github_link': '',
            'order': 2,
        },
    )


def reverse_data(apps, schema_editor):
    Education = apps.get_model('main', 'Education')
    Experience = apps.get_model('main', 'Experience')
    Education.objects.filter(
        institution__in=['Lovely Professional University', 'Kisan College', 'Prerna Punj Public School']
    ).delete()
    Experience.objects.filter(
        organization__in=['Algotutor', 'Allsoft Solutions']
    ).delete()


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_education_alter_blog_options_and_more'),
    ]

    operations = [
        migrations.RunPython(populate_data, reverse_data),
    ]
