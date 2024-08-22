from setuptools import setup, find_packages

setup(
    name='utils_package',
    version='0.1',
    packages=find_packages(),
    install_requires=[],
)
RECALCULATE_TABLE = os.getenv('ETL_RECALCULATE_DB_TABLE', 'sc_valencia.immission_recalculation')
