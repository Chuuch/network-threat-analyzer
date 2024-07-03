from setuptools import setup, find_packages

setup(
    name='networkscanner',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'requests',
        'python-dotenv'
    ],
    entry_points={
        'console_scripts': [
            'networkscanner-cli = networkscanner.scanner:port_scan'
        ]
    }
)
