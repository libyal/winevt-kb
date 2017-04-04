#!/bin/bash
#
# Script to set up Travis-CI test VM.

COVERALL_DEPENDENCIES="python-coverage python-coveralls python-docopt";

PYTHON2_DEPENDENCIES="libbde-python libewf-python libexe-python libfsntfs-python libfvde-python libfwnt-python libqcow-python libregf-python libsigscan-python libsmdev-python libsmraw-python libvhdi-python libvmdk-python libvshadow-python libvslvm-python libwrc-python python-construct python-crypto python-dfdatetime python-dfvfs python-dfwinreg python-pytsk3 python-six";

PYTHON2_TEST_DEPENDENCIES="python-mock";

PYTHON3_DEPENDENCIES="libbde-python3 libewf-python3 libexe-python3 libfsntfs-python3 libfvde-python3 libfwnt-python3 libqcow-python3 libregf-python3 libsigscan-python3 libsmdev-python3 libsmraw-python3 libvhdi-python3 libvmdk-python3 libvshadow-python3 libvslvm-python3 libwrc-python3 python3-construct python3-crypto python3-dfdatetime python3-dfvfs python3-dfwinreg python3-pytsk3 python3-six";

PYTHON3_TEST_DEPENDENCIES="python3-mock";

# Exit on error.
set -e;

if test `uname -s` = "Darwin";
then
	git clone https://github.com/log2timeline/l2tdevtools.git;

	mv l2tdevtools ../;
	mkdir dependencies;

	PYTHONPATH=../l2tdevtools ../l2tdevtools/tools/update.py --download-directory=dependencies --preset=winevt-kb;

elif test `uname -s` = "Linux";
then
	sudo rm -f /etc/apt/sources.list.d/travis_ci_zeromq3-source.list;

	sudo add-apt-repository ppa:gift/dev -y;
	sudo apt-get update -q;
	sudo apt-get install -y ${COVERALL_DEPENDENCIES} ${PYTHON2_DEPENDENCIES} ${PYTHON2_TEST_DEPENDENCIES} ${PYTHON3_DEPENDENCIES} ${PYTHON3_TEST_DEPENDENCIES};
fi
