from flask import render_template, request, flash, redirect, url_for, send_file
from app import app
from forms import ContactForm
import os

@app.route('/')
def index():
    form = ContactForm()
    return render_template('index.html', form=form)

@app.route('/contact', methods=['POST'])
def contact():
    form = ContactForm()
    if form.validate_on_submit():
        # In a real application, you would send an email or save to database
        flash('Thank you for your message! I will get back to you soon.', 'success')
        return redirect(url_for('index') + '#contact')
    else:
        for field, errors in form.errors.items():
            for error in errors:
                flash(f'Error in {field}: {error}', 'error')
        return redirect(url_for('index') + '#contact')

@app.route('/download-resume')
def download_resume():
    try:
        return send_file('static/assets/resume.pdf', 
                        as_attachment=True,
                        download_name='Seema_Devi_Resume.pdf',
                        mimetype='application/pdf')
    except FileNotFoundError:
        flash('Resume file not found. Please contact me directly.', 'error')
        return redirect(url_for('index'))
