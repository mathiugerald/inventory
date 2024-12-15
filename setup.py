from setuptools import setup, find_packages

setup(
    name='inventory_tracking_system',
    version='1.0.0',
    description='An inventory tracking system with authentication, concurrency control, and report generation',
    author='mwika mathiu',
    author_email='nsinn333@gmail.com',
    packages=find_packages(),
    include_package_data=True,   # Include non-Python files (like the database)
    install_requires=[
        'bcrypt',
        'pandas',
        'openpyxl',
        # Note: 'tkinter' is included with most Python installations by default
    ],
    entry_points={
        'console_scripts': [
            'inventory_app=main:main',  # Allows the app to be run from command line
        ],
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',  # Specify the minimum Python version required
)

