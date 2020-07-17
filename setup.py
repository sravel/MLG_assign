#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from io import open
import os.path as osp
from setuptools import setup


HERE = osp.abspath(osp.dirname(__file__))
sys.path.insert(0, HERE)
import MLGassign as MLGassign


def main():
    setup(
        name=MLGassign.__name__,
        version=MLGassign.__version__,
        description=MLGassign.__doc__,
        long_description=open(osp.join(HERE, 'README.rst'), encoding='utf-8').read(),
        long_description_content_type='text/x-rst',
        classifiers=[
            'Development Status :: 5 - Production/Stable',
            'Environment :: Other Environment',
            'Intended Audience :: Developers',
            'Intended Audience :: End Users/Desktop',
            'License :: OSI Approved :: LGPL License',
            'Operating System :: POSIX :: Linux',
            'Programming Language :: Python :: 3.7+',
            'Natural Language :: English',
        ],
        author="Sébastien Ravel",
        url="https://github.com/sravel/MLGassign",
        download_url="https://github.com/sravel/MLGassign/archive/{}.tar.gz".format(MLGassign.__version__),
        license='LGPL license',
        platforms=['unix', 'linux'],
        keywords=[
            'MLG',
            'microsatelite',
            'genotyped',
            'genetics'
        ],
        py_modules=['MLGassign'],
        install_requires=[
            'python>=3.7',
            'pandas>=1.0.0',
            'openpyxl>=2.6.0'
        ],
        options={
            'bdist_wheel':
                {'universal': True}
        },
        zip_safe=False,  # Don't install the lib as an .egg zipfile
        entry_points={'MLGassign': ["MLGassign = MLGassign"]},
    )

if __name__ == '__main__':
    main()
