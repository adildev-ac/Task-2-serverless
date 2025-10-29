#!/usr/bin/env python
"""
Script to create initial blog categories
"""
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'medical_portal.settings')
django.setup()

from blog.models import BlogCategory

categories = [
    'Mental Health',
    'Heart Disease',
    'COVID-19',
    'Immunization'
]

for category_name in categories:
    category, created = BlogCategory.objects.get_or_create(name=category_name)
    if created:
        print(f"✓ Created category: {category_name}")
    else:
        print(f"✓ Category already exists: {category_name}")

print("\nAll categories are ready!")
print("Blog categories in database:")
for cat in BlogCategory.objects.all():
    print(f"  - {cat.name}")
