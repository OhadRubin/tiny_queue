
# def call(*popenargs, timeout=None, **kwargs):
#     """Run command with arguments.  Wait for command to complete or
#     timeout, then return the returncode attribute.
#     The arguments are the same as for the Popen constructor.  Example:
#     retcode = call(["ls", "-l"])
#     """
#     with Popen(*popenargs, **kwargs) as p:
#         try:
#             return p.wait(timeout=timeout)
#         except:  # Including KeyboardInterrupt, wait handled that.
#             p.kill()
#             # We don't call p.wait() again as p.__exit__ does that for us.
#             raise

# def check_call(*popenargs, **kwargs):
#     """Run command with arguments.  Wait for command to complete.  If
#     the exit code was zero then return, otherwise raise
#     CalledProcessError.  The CalledProcessError object will have the
#     return code in the returncode attribute.
#     The arguments are the same as for the call function.  Example:
#     check_call(["ls", "-l"])
#     """
#     retcode = call(*popenargs, **kwargs)
#     if retcode:
#         cmd = kwargs.get("args")
#         if cmd is None:
#             cmd = popenargs[0]
#         raise CalledProcessError(retcode, cmd)
#     return 0

class Command(object):
    '''
    Enables to run subprocess commands in a different thread
    with TIMEOUT option!

    Based on jcollado's solution:
    http://stackoverflow.com/questions/1191374/subprocess-with-timeout/4825933#4825933
    '''
    def __init__(self, cmd):
        self.cmd = cmd
        self.process = None

    def run(self, **kwargs):
        def target(**kwargs):
            print("inside thread")
            self.process = subprocess.Popen(self.cmd,shell=True,**kwargs)
            self.process.communicate()

        thread = threading.Thread(target=target, kwargs=kwargs)
        thread.start()
        return thread
        # thread.join(timeout)
        # if thread.is_alive():
        #     self.process.terminate()
        #     thread.join()

        # return self.process.returncode

import threading
import time


import subprocess
import signal
def main():
    print("started")
    cmd = Command("echo hi ; sleep 3 ; echo bye")
    print("running cmd")
    thread = cmd.run()
    print("sleeping...")
    time.sleep(5)
    print("sending signal")
    cmd.process.send_signal(signal.SIGINT)
    
    
    # def your_proc_function(next_task):
    #     print("inside proc")
        
    #         subprocess.check_call(next_task,shell=True)
    
    #     def target(**kwargs):
    #         self.process = subprocess.Popen(self.cmd, **kwargs)
    #         self.process.communicate()
    # print("before running proc")

    # proc.start()
    # time.sleep(5)
    # # Terminate the process
    # print("terminating proc")
    # proc._popen.send_signal(signal.SIGINT)
    # # proc.terminate()  # sends a SIGTERM
    # print("terminated proc")
    


if __name__ == '__main__':
    main()