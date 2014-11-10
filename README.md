IceChrono
=========

A statistical and physical model to optimize chronologies of deep polar ice cores.


What do I need to run IceChrono?
--------------------------------

IceChrono is a python2 software, using the following modules:
- sys
- os
- time
- math
- numpy
- matplotlib
- multiprocessing
- warnings
- scipy

Usually, all you need to do is to install numpy, scipy and matplotlib. In general, the other modules are included by default with python.
It has been tested on debian 7 (with an update of matplotlib>0.11) and on ubuntu 13.10.


How to download IceChrono?
--------------------------

Go here:
https://github.com/parrenin/IceChrono/releases
and choose the release you want to download (usually the latest one).

How to run IceChrono?
---------------------

Run the following command:

`python IceChrono.py exp_directory`

where `exp_directory` is the name of the directory where you have set up your experiment (it contains the observations, the background scenarios and all the other parameters). For example, you can test IceChrono using the `AICC2012-LR` experiment provided for your convenience:

`python IceChrono.py AICC2012-LR`

It takes about 10 mn to run on a recent computer. It is an AICC2012-like experiment, albeit whith a Low Resolution.


What is the structure of an experiment directory?
-------------------------------------------------

You can have a look at the provided `AICC2012-LR` directory.

You have three general files:
- `parameters.py`                                     : contains general parameters for the experiment
- `parameters-CovariancePrior-AllDrillings-init.py`   : defines the covariance matrices of the background
- `parameters-AllDrillings.py`                        : defines drilling parameters that are the same for all drillings (there are overidded by drilling specific parameters).

Then you have one directory per drilling, which contains:
- `parameters.py`       : all the drilling specific parameters
- `density-prior.txt`   : depth / relative density
- `accu-prior.txt`      : depth / background accu (in m-of-ice/yr)
- `LID-prior.txt`       : depth / background Lock-in-Depth
- `thinning-prior.txt`  : depth / background thinning function
- `ice_age.txt`         : depth / age / sigma for ice age observations
- `gas_age.txt`         : depth / age / sigma for gas age observations
- `Ddepth.txt`          : depth / Delta-depth / sigma for Delta-depth observations

Then you have one directory per drilling couple, which contains:
- `ice_depth.txt`       : depth1 / depth2 / sigma on age for ice-ice stratigraphic links observations
- `gas_depth.txt`       : depth1 / depth2 / sigma on age for gas-gas stratigraphic links observations
- `icegas_depth.txt`    : depth1 / depth2 / sigma on age for ice-gas stratigraphic links observations
- `gasice_depth.txt`    : depth1 / depth2 / sigma on age for gas-ice stratigraphic links observations
- `ice_age_intervals.txt`   : depth\_top / depth\_bottom / duration / sigma for dated ice intervals observations
- `gas_age_intervals.txt`   : depth\_top / depth\_bottom / duration / sigma for dated gas intervals observations

 
What is the structure of the general `parameters.py` file?
--------------------------------------------------------

Have a look at the file `AICC2012-LR/parameters.py`, it is commented.

What is the structure of a drilling `parameters.py` file?
---------------------------------------------------------

Have a look at the files `AICC2012-LR/EDC/parameters.py`, it is commented.

How to set up the `parameters-CovariancePrior-AllDrillings-init.py` file:
-------------------------------------------------------------------------

This is the most difficult part of an experiment. You need to define:

- `self.correlation_corr_a`: the correlation matix for the accu correction function
- `self.correlation_corr_LID`: the correlation matix for the LID correction function
- `self.correlation_corr_tau`: the correlation matix for the thinning correction function
- `self.sigmap_corr_a`: the standard deviation of the accu correction function
- `self.sigmap_corr_LID`: the standard deviation of the LID correction function
- `self.sigmap_corr_tau`: the standard deviation of the thinning correction function

Have a look at the `AICC2012-LR` experiment, it is the easiest way to understand how it works.
Feel free to contact the author if you are blocked.
