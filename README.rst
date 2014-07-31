============================
Setup Guide
============================

**Pysub** is a Python Script to download subtitle for movies and TV Series in english from the terminal. 
Based on **Python3**.


Installation (Tested on Ubuntu)
-------------------------------

Python3 is now available by default on new versions of linux distributions. 

**Step 1:** Download or clone the repo.

**Step2:** Install pip3 for Python3

``sudo apt-get install python3-pip``

**Step 3:** Install Dependencies:

``sudo pip3 install python-magic``

``sudo pip3 install requests [May be available by default]``

**Step 4:** Move the whole directory to /opt/:

``sudo mv pysub /opt/``

**Step 5:** Add the PATH to .bashrc:

``export PATH="$PATH:/opt/pysub/pysub"``

Reload the terminal and that's it.

Usage
--------------------

``sub file_name``


.. image:: https://raw.githubusercontent.com/sachitad/sachitad.github.io/master/relative_path_pysub_example.png
    :alt: Pysub demo
    :align: center



**Absolute Path Demo:**


.. image:: https://raw.githubusercontent.com/sachitad/sachitad.github.io/master/absolute_path_pysub_example.png
    :alt: Pysub Absolute Path demo
    :align: center
