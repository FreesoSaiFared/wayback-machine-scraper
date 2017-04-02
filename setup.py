from setuptools import setup

description = ('A CLI and Scrapy middleware for scraping '
               'Wayback Machine snapshots from archive.org.')
long_description = description + \
        (' For further details, '
         'please see the code repository on github: '
         'https://github.com/sangaline/wayback-machine-scraper')


setup(
    name='wayback_machine_scraper',
    version='1.0.0',
    author='Evan Sangaline',
    author_email='evan@intoli.com',
    description=description,
    license='ISC',
    keywords='archive.org scrapy scraper waybackmachine',
    url="https://github.com/sangaline/wayback-machine-scraper",
    packages=['wayback_machine_scraper'],
    entry_points={
        'console_scripts': [
            'wayback-machine-scraper = wayback_machine_scraper.scraper.__main__:main',
        ],
    },
    long_description=long_description,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Framework :: Scrapy',
        'Topic :: Utilities',
        'License :: OSI Approved :: ISC License (ISCL)',
    ],
    install_requires=[
        'cryptography',
        'scrapy',
        'twisted',
    ]
)