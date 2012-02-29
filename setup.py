# -*- coding: utf-8 -*-

from setuptools import setup

setup(name='Olympo',
      version='0.0.1',
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
      package_data={
            'olympo': ['default/*.*', 
                       'default/update/*.*',
                       'default/update/TODO',
                       'default/update/new-issue',
                       'default/update/ejemplo/*.*',                        
                      ],
            #'neptuno.templates': ['*.xml'],
      },
      install_requires=[
        'kinterbasdb',
        'SQLAlchemy',
        'lxml',
        'xlrd',
        'xlwt',
        'simplejson',
        'jinja2',
      ],
     )
