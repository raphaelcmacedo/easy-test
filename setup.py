from distutils.core import setup
import os

README = os.path.join(os.path.dirname(__file__), 'README.rst')

setup(
    name='django-easy-test',
    version='1.0',
    long_description=open(README).read(),
    packages=[
        'easy_test',
        'easy_test.cases',
        'easy_test.metas',
        'easy_test.mixins',
        ],
    url='https://github.com/raphaelcmacedo/easy-test',
    license='MIT',
    author='Raphael Macedo',
    author_email='raphaelcmacedo@hotmail.com',
    description='An extension of django tests that contains premade cases with the most comom tests for a web application',
    platforms='any',
    install_requires=[],
    zip_safe=True,
    include_package_data=True,
    classifiers=[
          'Development Status :: 5 - Production/Stable',
          'Framework :: Django',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: MIT License',
          'Natural Language :: English',
          'Operating System :: OS Independent',
          'Programming Language :: Python',
          'Programming Language :: Python :: 3',
          'Topic :: Software Development :: Libraries',
        ],
)
