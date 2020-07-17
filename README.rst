=============================
Multi-Locus Genotypes assign
=============================

|PythonVersions| |PypiPackage|

Multi-Locus Genotypes (MLGs) are frequently used to carry out population
genetics of clonal organisms. Tools to assign genotyped individuals to
MLGs were integrated in some genetic software. However, these tools
usually fail to appropriately deal with missing data. Missing data lead
sometimes lead to potentially assign a individual genotype to several
MLGs. For example, the multilocus genotype 100/200/999 (where 999 is a
missing data) could be assigned to MLG 100/200/300 and to MLG
100/200/302. Despite this ambiguity, most tools assign the genotype with
missing dat to one or the other MLG.
We developed a script that :

* group in the same MLG individuals with no missing data and with the same genotype,
* mark as unassigned individuals with missing data that could be assigned to more than one MLG.


.. csv-table:: Exemple of multilocus genotype table
   :widths: 10,10,10,10,10,10,10,10,10,10,10,10,10
   :header-rows: 1

    "","Pymrs47","Pyrms427","Pyrms657","Pyrms77B","Pyrms63","Pyrms83B","Pyrms607","Pyrms37","Pyrms233","Pyrms319","Pyrms99B","Pyrms43B"
    "MD2249","163","211","168","200","151","115","284","197","253","284","241","350"
    "MD2245","163","211","168","202","151","115","284","197","253","284","241","999"
    "MD2129","163","211","168","194","151","115","284","197","253","284","241","999"
    "MD2125","163","211","168","194","151","115","284","197","253","284","241","999"
    "MD2124","163","211","168","194","151","115","284","197","253","284","241","999"
    "MD1936","163","211","168","194","151","115","284","197","253","284","241","999"
    "MD1832","163","213","168","194","151","115","284","197","253","284","241","999"
    "MD1831","163","213","168","194","151","115","284","197","253","284","241","999"
    "MD1826","163","213","168","194","151","115","284","197","253","284","241","999"
    "MD1708","163","211","168","194","151","999","281","197","253","284","241","328"
    "MD1689","163","211","168","194","151","999","278","197","253","284","241","999"

Install
-------

::

    # not working yet, in development
    pip3 install MLGassign


Usage
-----


.. code-block:: bash

    # see help
    MLGassign.py -h

    Input infos not mandatory:
      -v, --version         Use if you want to know which version of
                            MLGassign.py you are using
      -h, --help            show this help message and exit
      -d, --debug           enter verbose/debug mode

    Input mandatory infos for running:
      -e <path/to/file/Excel>, --excel <path/to/file/Excel>
                            Matrix excel file
      -s sheet name>, --sheet sheet name>
                            Name of sheet in excel file

    # run script
    MLGassign.py -e Test_MLG.xlsx -s test




.. |PythonVersions| image:: https://img.shields.io/badge/python-3.7+-blue.svg
   :target: https://www.python.org/downloads
   :alt: Python /3.7+

.. |PypiPackage| image:: https://badge.fury.io/py/MLGassign.svg
   :target: https://pypi.org/project/MLGassign
   :alt: PyPi package
