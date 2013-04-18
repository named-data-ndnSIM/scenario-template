Prerequisites
=============

Custom version of NS-3 and specified version of ndnSIM needs to be installed.

The code should also work with the latest version of ndnSIM, but it is not guaranteed.

    mkdir ns-dev
    cd ns-dev

    git clone git://github.com/cawka/ns-3-dev-ndnSIM.git ns-3
    git clone git://github.com/cawka/pybindgen.git pybindgen
    git clone git://github.com/NDN-Routing/ndnSIM.git ns-3/src/ndnSIM

    git clone git://github.com/cawka/ndnSIM-scenario-template.git my-simulations

    cd ns-3
    ./waf configure -d optimized
    ./waf
    sudo ./waf install

    cd ../my-simulations

After which you can proceed to compile and run the code

For more information how to install NS-3 and ndnSIM, please refer to http://ndnsim.net website.

Compiling
=========

To configure in optimized mode without logging **(default)**:

    ./waf configure

To configure in optimized mode with scenario logging enabled (logging in NS-3 and ndnSIM modules will still be disabled,
but you can see output from NS_LOG* calls from your scenarios and extensions):

    ./waf configure --logging

To configure in debug mode with all logging enabled

    ./waf configure --debug

If you have installed NS-3 in a non-standard location, you may need to set up ``PKG_CONFIG_PATH`` variable.
For example, if NS-3 is installed in /usr/local/, then the following command should be used to
configure scenario

    PKG_CONFIG_PATH=/usr/local/lib/pkgconfig ./waf configure

or

    PKG_CONFIG_PATH=/usr/local/lib/pkgconfig ./waf configure --logging

or

    PKG_CONFIG_PATH=/usr/local/lib/pkgconfig ./waf configure --debug

Running
=======

Normally, you can run scenarios either directly

    ./build/<scenario_name>

or using waf

    ./waf --run <scenario_name>

If NS-3 is installed in a non-standard location, on some platforms (e.g., Linux) you need to specify ``LD_LIBRARY_PATH`` variable:

    LD_LIBRARY_PATH=/usr/local/lib ./build/<scenario_name>

or

    LD_LIBRARY_PATH=/usr/local/lib ./waf --run <scenario_name>

To run scenario using debugger, use the following command:

    gdb --args ./build/<scenario_name>


Running with visualizer
-----------------------

There are several tricks to run scenarios in visualizer.  Before you can do it, you need to set up environment variables for python to find visualizer module.  The easiest way to do it using the following commands:

    cd ns-dev/ns-3
    ./waf shell

After these command, you will have complete environment to run the vizualizer.

The following will run scenario with visualizer:

    ./waf --run <scenario_name> --vis

or

    PKG_LIBRARY_PATH=/usr/local/lib ./waf --run <scenario_name> --vis

If you want to request automatic node placement, set up additional environment variable:

    NS_VIS_ASSIGN=1 ./waf --run <scenario_name> --vis

or

    PKG_LIBRARY_PATH=/usr/local/lib NS_VIS_ASSIGN=1 ./waf --run <scenario_name> --vis

Available simulations
=====================

Topology converter
------------------

To convert topologies from RocketFuel format and assign random bandwidths and delays for links, you can run the following:

    ./run.py -s convert-topologies

You can edit ``run.py`` script and ``scenarios/rocketfuel-maps-cch-to-annotaded.cc`` to modifiy topology conversion logic
(e.g., you may want to assign different bandwidth range for "backbone-to-backbone" links).

For more information about Rocketfuel topology files, please refer to http://www.cs.washington.edu/research/networking/rocketfuel/

