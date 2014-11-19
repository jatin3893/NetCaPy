from setuptools import setup, find_packages

setup(
    name='NetCaPy',
    version = "1.0.0",
    author='Jatin Parekh, Shubham Kankaria, Anshuli Patil, Rajat Jain, Srinivas Rishindra',
    author_email='jatinparekh93@gmail.com, shubhamkank@gmail.com, anshulipatil8@gmail.com, rajat13jain@gmail.com, Sririshindra@gmail.com',
    url='https://github.com/jatin3893/NetCaPy',
    license=open('docs/LICENSE.txt', 'r').read(),
    description='ScaPy and PyQt based network packet capturing and analysis tool',
    long_description=open('README.md', 'r').read(),
    install_requires=[  "matplotlib >= 1.3.1",
                        "scapy",
                        "netifaces"],
    packages=find_packages(),
    package_data={
        'NetCaPy': [
            '*.ui'
        ],
        'NetCaPy.Others' : [
            '*.ui',
            '*.png',
            '*.jpg'
        ],
        'NetCaPy.Analysis' : [
            '*.ui',
            '*.png',
            '*.jpg'
        ],
        'NetCaPy.Filter' : [
            '*.ui',
            '*.png',
            '*.jpg'
        ],
        'NetCaPy.Help' : [
            '*.ui',
            '*.png',
            '*.jpg'
        ],
        'NetCaPy.Input' : [
            '*.ui',
            '*.png',
            '*.jpg'
        ],
        'NetCaPy.Output' : [
            '*.ui',
            '*.png',
            '*.jpg'
        ],
    },
    include_package_data=True,
    entry_points = {'console_scripts': ['netcapy = NetCaPy.Application:main',],},
)