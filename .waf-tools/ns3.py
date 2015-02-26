## -*- Mode: python; py-indent-offset: 4; indent-tabs-mode: nil; coding: utf-8; -*-
'''

When using this tool, the wscript will look like:

	def options(opt):
	        opt.tool_options('ns3')

	def configure(conf):
		conf.load('compiler_cxx ns3')

                conf.check_ns3_modules()

	def build(bld):
		bld(source='main.cpp', target='app', use='CCNX')

Options are generated, in order to specify the location of ccnx includes/libraries.


'''

import waflib
from waflib.Configure import conf
from waflib import Utils,Logs,Errors

@conf
def _check_dependencies(conf, modules, mandatory):
    # Logs.pprint ('CYAN', '  + %s' % modules)
    found = []

    libversion = "optimized"
    if conf.options.debug:
        libversion = "debug"

    if not isinstance(modules, list):
        modules = Utils.to_list (modules)

    for module in modules:
        retval = conf.check_cfg(package = 'libns3-dev-%s-%s' % (module, libversion),
                                args='--cflags --libs', mandatory=mandatory,
                                msg="Checking for ns3-%s" % module,
                                uselib_store='NS3_%s' % module.upper())

        if not retval is None:
            found.append(module)
    import copy
    if not 'NS3_MODULES_FOUND' in conf.env:
        conf.env['NS3_MODULES_FOUND'] = []
    conf.env['NS3_MODULES_FOUND'] = conf.env['NS3_MODULES_FOUND'] + copy.copy(found)

@conf
def check_ns3_modules(conf, modules, mandatory = True):
    import os

    if not 'NS3_CHECK_MODULE_ONCE' in conf.env:
        conf.env['NS3_CHECK_MODULE_ONCE'] = ''

        conf.check_cfg(atleast_pkgconfig_version='0.0.0')

        if conf.options.debug:
            conf.env.append_value('DEFINES', 'NS3_LOG_ENABLE')

    conf._check_dependencies(modules, mandatory)

