from setuptools import setup, find_packages

setup(
    name='kirana_store_management',           # Name of the package
    version='0.1',                            # Initial version
    packages=find_packages(),                 # Automatically find and include all packages
    install_requires=[],                      # Dependencies (add external libraries if needed)
    entry_points={
        'console_scripts': [
            'kirana-store=kirana_store.main:main',  # Command line shortcut for running the app
        ],
    },
    include_package_data=True,                # Include non-Python files (e.g., images, data files)
    description='Kirana Store Management System using Tkinter',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Sayed Mahfuze',
    author_email='sayed@yahoo.com',
    url='https://github.com/WalleEve/git-repo/tree/main/Python/TK_INTER_PROJECTS/kirana_store_management',  # Replace with your GitHub repo
)
5