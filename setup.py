from setuptools import find_packages, setup

package_name = 'ros2_netspeed'

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
    maintainer='Hikaru Yoshida',
    maintainer_email='guangjitian755@gmail.com',
    description='a package for measur network speed',
    license='BSD-3-Clause',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            'measur1 = ros2_netspeed.measur1:main',
            'measur2 = ros2_netspeed.measur2:main',
            'output = ros2_netspeed.output:main',
        ],
    },
)
