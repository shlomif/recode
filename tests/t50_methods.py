# -*- coding: utf-8 -*-
import common
from common import setup_module, teardown_module
from __main__ import py

import os, sys
input_name = '%s/../COPYING' % os.path.dirname(sys.argv[0])
with open(input_name) as f:
    input = f.read()

def test_1():
    # No step at all.
    yield validate, 'texte..texte'

    # One single step.
    yield validate, 'latin1..ibmpc/'

    # One single step and a surface
    yield validate, 'latin1..ibmpc'

    # One single step.
    yield validate, 'texte..latin1'

    # Two single steps.
    yield validate, 'texte..bangbang'

    # Two single steps and a surface.
    yield validate, 'texte..ibmpc'

    # Three single steps.
    yield validate, 'texte..iconqnx'

    # Four single steps, optimized into three (with iconv) or two (without).
    yield validate, 'ascii-bs..ebcdic'

def validate(request):
    before, after = request.split('..')

    # With a pipe
    if os.name == 'nt':
        py.test.skip()
    command = ('$R --quiet --force < %s %s'
               '| $R --quiet --force %s..%s'
               % (input_name, request, after, before))
    print(command)
    output = common.external_output(command)
    common.assert_or_diff(output, input)

    # With an intermediate file
    with open(common.run.work, 'w') as f:
        f.write(input)
    command1 = ('$R --quiet --force %s %s'
                % (request, common.run.work))
    command2 = ('$R --quiet --force %s..%s %s'
                % (after, before, common.run.work))
    print(command1)
    print(command2)
    common.external_output(command1)
    common.external_output(command2)
    with open(common.run.work) as f:
        output = f.read()
    common.assert_or_diff(output, input)
