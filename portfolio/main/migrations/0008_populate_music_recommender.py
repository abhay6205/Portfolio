from django.db import migrations

def populate_music_recommender(apps, schema_editor):
    Project = apps.get_model('main', 'Project')
    
    Project.objects.get_or_create(
        title='Emotion-Based Music Recommender System',
        defaults={
            'description': (
                'A real-time emotion-based music recommendation system built with Python. Leveraged MediaPipe '
                'to extract 468 facial landmarks and applied PCA (Principal Component Analysis) to reduce '
                'feature dimensionality by 85%, improving classification speed. Built a K-Means clustering '
                'model to classify emotions across 5 categories — Happy, Sad, Energetic, Calm, and Neutral '
                '— achieving approximately 15% higher accuracy through personalized training data. Implemented '
                'smooth emotion buffering to reduce false detections by 25%, enabling stable, real-time music '
                'recommendations matched to the user\'s current mood.'
            ),
            'tech_stack': 'Python, Machine Learning, PCA, K-Means, MediaPipe, OpenCV',
            'github_link': 'https://github.com/abhay6205/Emotion-Music-Recommender',
            'order': 3,
        }
    )

def remove_music_recommender(apps, schema_editor):
    Project = apps.get_model('main', 'Project')
    Project.objects.filter(title='Emotion-Based Music Recommender System').delete()

class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_populate_certificates'),
    ]

    operations = [
        migrations.RunPython(populate_music_recommender, remove_music_recommender),
    ]
