from setuptools import setup, find_packages

setup(
    name='Future Rockstars',
    version='1.0',
    long_description=__doc__,
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'certifi==2017.11.5',
        'chardet==3.0.4',
        'click==6.7',
        'coverage==4.4.2',
        'coveralls==1.2.0',
        'docopt==0.6.2',
        'Flask==0.12.2',
        'Flask-Script==2.0.6',
        'Flask-Testing==0.6.2',
        'Flask-WTF==0.14.2',
        'idna==2.6',
        'itsdangerous==0.24',
        'Jinja2==2.9.6',
        'MarkupSafe==1.0',
        'requests==2.18.4',
        'tinydb==3.5.0'.
        'urllib3==1.22',
        'Werkzeug==0.12.2',
        'WTForms==2.1'
    ]
)