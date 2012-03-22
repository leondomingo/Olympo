# -*- coding: utf-8 -*-

from setuptools import setup

setup(name='Olympo',
      version='0.0.4',
      author=u'León Domingo',
      author_email='leon.domingo@ender.es',
      description=('A little set of utilities to manage Olympo projects'),
      #license=???,
      keywords='ender olympo',
      classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Topic :: Utilities',
      ],
      url='http://www.ender.es',      
      packages=['olympo',
                #'neptuno.postgres',
                #'neptuno.templates',
      ],
#      package_data={
#            'olympo': ['default/*.*', 
#                      ],
#            #'neptuno.templates': ['*.xml'],
#      },
      install_requires=[
        #'kinterbasdb',
        'SQLAlchemy==0.7.5',
        'lxml',
        'xlrd',
        'xlwt',
        'simplejson==2.2.0',
        'jinja2',
      ],
     )
