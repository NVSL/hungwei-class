from cfiddle import *
import cfiddle

from hungwei import HungWeiExecutionMethod

def test_run():
    from hungwei import HungWeiExecutionMethod
    enable_debug()
    cfiddle.set_config("RunnerExecutionMethod_type", HungWeiExecutionMethod)

    foo = """
#include"cfiddle.hpp"
#include<iostream>
#include <unistd.h>

extern "C" int foo() {
   start_measurement();
   char hostname[1024];
   gethostname(hostname, 1024);
   std::cout << "hello from " << hostname <<"\n";
   end_measurement();
   return 42;
}
"""

    b = build(code(foo))
    r = run(b, ["foo"]*4, perf_counters=[["CYCLES", "INSTRUCTIONS"], ["PERF_COUNT_SW_CPU_CLOCK","Cycles"]])
    print(r[0].return_value)
    assert r[0].return_value == 42
