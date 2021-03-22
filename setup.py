from setuptools import setup, find_packages

with open('README.md') as readme_file:
    README = readme_file.read()

with open('HISTORY.md') as history_file:
    HISTORY = history_file.read()

setup_args = dict(
    name='quantstyles',
    version='0.1',
    description='Matplotlib styles for scientific usage',
    long_description_content_type="text/markdown",
    long_description=README + '\n\n' + HISTORY,
    license='MIT',
    packages=find_packages(),
    author='Andrii Trelin',
    author_email='andrii.trelin@uni-rostock.de',
    keywords=[],
    url='https://github.com/Trel725/quantstyles',
    download_url='https://pypi.org/project/quantstyles/'
)

install_requires = [
    'numpy',
    'os',
    'matplotlib',
    'glob'
    'urllib'
]

if __name__ == '__main__':
    setup(**setup_args,
          install_requires=install_requires,
          include_package_data=True)