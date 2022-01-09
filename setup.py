from setuptools import setup

package_name = 'ros2_ultrasonic_sensor'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='dominik',
    maintainer_email='dominik.helfenstein@gmx.de',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'talker = ros2_ultrasonic_sensor.publisher_member_function:main',
            'listener = ros2_ultrasonic_sensor.subscriber_member_function:main',
        ],
    },
)
