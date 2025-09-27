from setuptools import setup, find_packages

setup(
    name='NinjaZipPy',
    version='0.0.1',
    packages=find_packages(),
    install_requires=[
        # This is the key dependency, replacing the native 7z DLL/SO loading (Bit7zLibrary).
        'py7zr',
    ],
    entry_points={
        'console_scripts': [
            # This makes 'ninjazippy' runnable from the terminal
            'ninjazippy = ninja_zip_py.cli:main', 
        ],
    },
    author='Your Name',
    description='A Python utility for zipping and unzipping .7z archives (Functional Migration).',
    license='MPL-2.0',
    python_requires='>=3.6',
)