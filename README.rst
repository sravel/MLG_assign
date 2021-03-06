=============================
Multi-Locus Genotypes assign
=============================

.. contents:: Table of Contents
   :depth: 2



About this package
------------------


|PythonVersions| |PypiPackage|

Multi-Locus Genotypes (MLGs) are frequently used to carry out population
genetics of clonal organisms. Tools to assign genotyped individuals to
MLGs were integrated in some genetic software. However, these tools
usually fail to appropriately deal with missing data. Missing data
sometimes lead to potentially assign a individual genotype to several
MLGs. For example, the multilocus genotype 100/200/999 (where 999 is a
missing data) could be assigned to MLG 100/200/300 and to MLG
100/200/302. Despite this ambiguity, most tools assign the genotype with
missing data to one or the other MLG.
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

    pip3 install MLG_assign


Usage
-----

Running MLG_assign with GUI
^^^^^^^^^^^^^^^^^^^^^^^^^^^

* To run the gui, just call program

::

    MLG_assign
    # or
    MLG_assign gui



Running MLG_assign with command line
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

::

    # see help
    MLG_assign cmd -h

    usage: MLG_assign cmd [-h] -e <path/to/file/Excel> -s sheet name>

    optional arguments:
      -h, --help            show this help message and exit

    Input mandatory infos for running:
      -e <path/to/file/Excel>, --excel <path/to/file/Excel>
                            Matrix excel file
      -s sheet name>, --sheet sheet name>
                            Name of sheet in excel file

    # run script
    MLG_assign cmd -e Test_MLG.xlsx -s test

Test data
---------

Data test avail at: https://github.com/sravel/MLG_assign/blob/master/Test_MLG.xlsx

::

    wget https://github.com/sravel/MLG_assign/blob/master/Test_MLG.xlsx


.. |PythonVersions| image:: https://img.shields.io/badge/python-3.7+-blue.svg
   :target: https://www.python.org/downloads
   :alt: Python /3.7+

.. |PypiPackage| image:: https://badge.fury.io/py/MLG-assign.svg
   :target: https://badge.fury.io/py/MLG-assign
   :alt: PyPi MLG-assign
