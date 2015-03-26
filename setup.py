from setuptools import setup, find_packages
#this is a test
setup(name = 'django-social-share-settings',
      description = 'Model and front end library for choosing and integrating social media share widgets.',
      version = '0.2',
      url = 'https://github.com/ninapavlich/django-social-share-settings',
      author = 'Nina Pavlich',
      author_email='nina@cgparntersllc.com',
      license = 'BSD',
      packages=find_packages(exclude=['ez_setup']),
      zip_safe = False,
      include_package_data=True,
      install_requires = ['setuptools', 'Django'],
      classifiers=[
                   'Development Status :: 5 - Production/Stable',
                   'Environment :: Web Environment',
                   'Framework :: Django',
                   'Intended Audience :: Developers',
                   'License :: OSI Approved',
                   'Operating System :: OS Independent',
                   'Programming Language :: Python'
                  ]
)
