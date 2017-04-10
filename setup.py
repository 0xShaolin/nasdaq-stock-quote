from setuptools import setup

try:
    with open('LICENSE.txt', 'r') as f:
        _license = f.read()
except:
    _license = ''

setup(
  name='nasdaq-stock-quote',
  version='0.1',
  description='NASDAQ Common Stock Quote & Summary Data Scraper',
  author='Andrew Porter',
  author_email='porter.r.andrew@gmail.com',
  license=_license,
  url='https://github.com/AndrewRPorter/nasdaq-stock-quote',
  download_url='https://github.com/AndrewRPorter/nasdaq-stock-quote/archive/0.1.tar.gz',
  install_requires=['setuptools', 'requests', 'lxml'],
 )