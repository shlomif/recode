# -*- coding: utf-8 -*-
import common
from common import setup_module, teardown_module, Recode, outer

class Test:

    def test_1(self): # Ensure correct error code returned for invalid input
        request = Recode.Request(outer) # FIXME: Does not work with iconv (outer_iconv): Debian bug #348909
        request.scan('utf-8..latin1')
        task = Recode.Task(request)
        task.set_input("\303\241 \303\247  \316\261 \316\266")
        task.perform()
        assert(task.get_error() == Recode.UNTRANSLATABLE)
