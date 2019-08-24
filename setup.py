from setuptools import setup

NAME = 'module'
setup(
    name=NAME,
    version=open('VERSION').read().strip(),

    description=NAME,
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',

    author='Tommaso De Rossi',
    author_email='daer.tommy@gmail.com',
    license='Apache Software License 2.0',

    url=f'https://github.com/remorses/{NAME}',
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
    packages=[NAME],
)


