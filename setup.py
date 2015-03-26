from setuptools import setup, find_packages
#this is a test
setup(name = 'django-share-me-share-me',
      description = 'Model and front end library for choosing and integrating social media share widgets.',
      version = '1.0',
      url = 'https://github.com/ninapavlich/django-share-me-share-me',
      author = 'Nina Pavlich',
      author_email='nina@ninalp.com',
      license = 'BSD',
      packages=find_packages(exclude=['ez_setup']),
      zip_safe = False,
      include_package_data=True,
      install_requires = ['setuptools', 'Django'],
      classifiers=[
       'Development Status :: 4 - Beta',
       'Environment :: Web Environment',
       'Framework :: Django',
       'Intended Audience :: Developers',
       'License :: OSI Approved',
       'Operating System :: OS Independent',
       'Programming Language :: Python'
      ]
)
