from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string

from .models import Project, Experience, ContactMessage, Blog, Education
from .forms import ContactForm


def _handle_contact_form(request):
    """Validate, save to DB, and send email. Returns (success: bool, form)."""
    form = ContactForm(request.POST)
    if form.is_valid():
        contact = form.save()

        # Send email notification
        subject = f'New Contact Message from {contact.name}'
        body = (
            f"Name: {contact.name}\n"
            f"Email: {contact.email}\n"
            f"Message:\n{contact.message}\n"
        )
        try:
            send_mail(
                subject,
                body,
                settings.DEFAULT_FROM_EMAIL,
                [settings.EMAIL_HOST_USER],
                fail_silently=False,
            )
        except Exception:
            # Email sending failed but the message is already saved in DB
            pass

        # Send confirmation email to the visitor
        try:
            html_content = render_to_string(
                'main/emails/confirmation_email.html',
                {'name': contact.name, 'message': contact.message},
            )
            send_mail(
                'Thank You for Reaching Out — Abhay\'s Portfolio',
                f'Hi {contact.name}, thank you for visiting my portfolio and reaching out. '
                f'I have received your message and will get back to you soon.',
                settings.DEFAULT_FROM_EMAIL,
                [contact.email],
                fail_silently=False,
                html_message=html_content,
            )
        except Exception:
            # Confirmation email failed but the message is already saved
            pass

        return True, form
    return False, form


def home(request):
    if request.method == 'POST':
        success, _ = _handle_contact_form(request)
        if success:
            messages.success(request, 'Your message has been sent successfully!')
        return redirect('home')

    context = {
        'educations': Education.objects.all(),
        'experiences': Experience.objects.all(),
        'projects': Project.objects.all(),
        'blogs': Blog.objects.filter(is_published=True),
    }
    return render(request, 'main/home.html', context)


def about(request):
    experiences = Experience.objects.all()
    return render(request, 'main/about.html', {'experiences': experiences})


def projects(request):
    projects = Project.objects.all()
    return render(request, 'main/projects.html', {'projects': projects})


def contact(request):
    if request.method == 'POST':
        success, form = _handle_contact_form(request)
        if success:
            messages.success(request, 'Your message has been sent successfully!')
            return redirect('contact')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = ContactForm()

    return render(request, 'main/contact.html', {'form': form})


def blog(request):
    blogs = Blog.objects.filter(is_published=True)
    return render(request, 'main/blog.html', {'blogs': blogs})
