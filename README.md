Prerequisites
=============

Custom version of NS-3 and specified version of ndnSIM needs to be installed.

The code should also work with the latest version of ndnSIM, but it is not guaranteed.

    git clone git@github.com:cawka/ns-3-dev-ndnSIM.git -b ns-3.16-ndnSIM ns-3
    git clone git@github.com:NDN-Routing/ndnSIM.git -b v0.2.2 ns-3/src/ndnSIM

    cd ns-3
    ./waf configure
    ./waf install

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


When running using ./waf, it is possible to run scenario with visualizer:

    ./waf --run <scenario_name> --vis

To run scenario using debugger, use the following command:

    gdb --args ./build/<scenario_name>

Available simulations
=====================

*put here information how to run scenarios, and if available, brief description*