from setuptools import setup

dependencies = open('requirements.txt').read().split("\n")

setup(
    name='codelessengine',
    version='0.1',
    description=('The engine to simplify writing of microservices,'
                 ' testing, etc'),
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.1',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Intended Audience :: Developers',
        'Topic :: Database',
    ],
    url='https://github.com/sergeyglazyrindev/codelessengine',
    author='Sergey Glazyrin',
    author_email='sergey.glazyrin.dev@gmail.com',
    license='MIT',
    packages=['codelessengine', ],
    include_package_data=True,
    zip_safe=False,
    extras_require={
        'testing': ['nose', 'mock'],
    },
    test_suite='tests',
    keywords=[
        'uml', 'codeless', 'framework', 'standart', 'openapi',
        'microservice'
    ],
    download_url=('https://github.com/sergeyglazyrindev/'
                  'codelessengine/tarball/0.1'),
    install_requires=dependencies
)
