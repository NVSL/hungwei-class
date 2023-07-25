from cfiddle import *
import cfiddle
from delegate_function import *

def HungWeiExecutionMethod():
    return SelfContainedExecutionMethod(SlurmDelegate(temporary_file_root=os.getcwd(), delegate_executable_path="/usr/local/bin/delegate-function-run"))

