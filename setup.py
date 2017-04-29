from setuptools import setup, find_packages

setup(
    name='python-text-generator',
    author = 'yaketake08',
    author_email = 'jake-basu@hotmail.co.jp'
    version='1.0',
    packages=find_packages(),
    install_requires=[],
    entry_points={
        'console_scripts': 'python-text-generator=src.main:entry'
    },
    url = "https://github.com/tjkendev/python-text-generator"
    classifiers=[
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: MacOS',
        'Operating System :: POSIX',
        'Programming Language :: Python',
    ],
    test_suite='test',
)
