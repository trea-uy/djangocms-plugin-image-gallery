from setuptools import setup
import os

setup(
    name = "image_gallerys",
    packages = ['image_gallerys',],

    package_data = {
        '': [
            'templates/*.html',
        ]
    },

    version = "0.1",
    description = "Image gallery with caption and link",
    long_description=open(os.path.join(os.path.dirname(__file__), 'README.md')).read(),
    author = "Trea",
    author_email = "trea@trea.uy",
    url = "",
    license = "BSD",
    keywords = ["django", "django-cms", "bootstrap", "image gallery"],
    classifiers = [
        "Programming Language :: Python",
        "Environment :: Web Environment",
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Framework :: Django"
        ],
    include_package_data = True,
    zip_safe = True,
    install_requires = ['Django-CMS>=2.2'],
    )
