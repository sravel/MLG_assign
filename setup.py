#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from io import open
import os.path as osp
from setuptools import setup, find_packages


HERE = osp.abspath(osp.dirname(__file__))
sys.path.insert(0, HERE)
import MLG_assign


def main():
    setup(
        name=MLG_assign.__name__,
        version=MLG_assign.__version__,
        description="Application to add MLG",
        long_description=open(osp.join(HERE, 'README.rst'), encoding='utf-8').read(),
        long_description_content_type='text/x-rst',
        classifiers=[
            'Development Status :: 5 - Production/Stable',
            'Environment :: Other Environment',
            'Intended Audience :: Developers',
            'Intended Audience :: End Users/Desktop',
            'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
            'Operating System :: POSIX :: Linux',
            'Programming Language :: Python :: 3.7',
            'Natural Language :: English',
        ],
        author="Sébastien Ravel",
        url="https://github.com/sravel/MLG_assign",
        download_url="https://github.com/sravel/MLG_assign/archive/{}.tar.gz".format(MLG_assign.__version__),
        license='LGPL license',
        platforms=['unix', 'linux'],
        keywords=[
            'MLG',
            'microsatelite',
            'genotyped',
            'genetics'
        ],
        packages=find_packages(),
        package_data={
                    'MLG_assign'         : ['*.ini'],
                    'MLG_assign.excel'   : ['*.xlsx'],
                    'MLG_assign.gooey'   : ['./includes/*.png'],
        },
        include_package_data=True,
        install_requires=[
            'pandas>=1.0.0',
            'openpyxl>=2.6.0',
            'gooey>=1.0.4.0'
        ],
        options={
            'bdist_wheel':
                {'universal': True}
        },
        zip_safe=False,  # Don't install the lib as an .egg zipfile
        entry_points={'console_scripts': ["MLG_assign = MLG_assign:main"]},
    )

if __name__ == '__main__':
    main()
