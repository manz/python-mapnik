#!/usr/bin/env python
from nose.tools import eq_
from .utilities import run_all
import mapnik

def test_logger_init():
    eq_(mapnik.severity_type.debug,0)
    eq_(mapnik.severity_type.warn,1)
    eq_(mapnik.severity_type.error,2)
    eq_(mapnik.severity_type.none,3)
    default = mapnik.logger.get_severity()
    mapnik.logger.set_severity(mapnik.severity_type.debug)
    eq_(mapnik.logger.get_severity(),mapnik.severity_type.debug)
    mapnik.logger.set_severity(default)
    eq_(mapnik.logger.get_severity(),default)

if __name__ == "__main__":
    exit(run_all(eval(x) for x in dir() if x.startswith("test_")))
