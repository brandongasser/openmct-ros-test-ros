from setuptools import find_packages, setup

package_name = 'telemetry'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='brandon',
    maintainer_email='bgasser12@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'telemetry_source = telemetry.telemetry_source:main',
            'telemetry_server = telemetry.telemetry_server:main'
        ],
    },
)
