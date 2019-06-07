

from setuptools import setup


setup(
    name='TODO',
    version=open('VERSION').read().strip(),

    description='TODO',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',

    author='Tommaso De Rossi',
    author_email='daer.tommy@gmail.com',
    license='Apache Software License 2.0',

    url='https://github.com/remorses/TODO',
    keywords=['TODO'],
    install_requires=[x for x in open('./requirements.txt').read().strip().split('\n') if x.strip()],
    package_data={'': ['*.yaml', '*.json', '*.yml']},
    include_package_data=True,
    classifiers=[

        'Intended Audience :: Information Technology',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    packages=['module'],
)


