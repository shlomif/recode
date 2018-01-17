# -*- coding: utf-8 -*-
import common
from common import setup_module, teardown_module, Recode, outer, outer_iconv

class Test:

    def test_1(self): # Ensure correct error code returned for untranslatable input
        request = Recode.Request(outer)
        request.scan('utf-8..latin1')
        task = Recode.Task(request)
        task.set_input("\303\241 \303\247  \316\261 \316\266")
        task.perform()
        assert(task.get_error() == Recode.UNTRANSLATABLE)

    # FIXME: Does not work with iconv for abort_level > UNTRANSLATABLE: Debian bug #348909
    def test_2(self): # Ensure correct error code returned for untranslatable input (with iconv)
        request = Recode.Request(outer_iconv)
        request.scan('utf-8..latin1')
        task = Recode.Task(request)
        task.set_input("\303\241 \303\247  \316\261 \316\266")
        task.set_abort_level(Recode.UNTRANSLATABLE)
        task.perform()
        assert(task.get_error() == Recode.UNTRANSLATABLE)
