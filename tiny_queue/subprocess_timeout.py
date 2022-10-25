
import threading
import time
import subprocess
import signal

class Command(object):
    def __init__(self, cmd):
        self.cmd = cmd
        self.process = None

    def run(self, **kwargs):
        def target(**kwargs):
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


def main():
    print("started")
    cmd = Command("echo hi ; sleep 3 ; echo bye")
    print("running cmd")
    cmd.run()
    print("sleeping...")
    time.sleep(5)
    print("sending signal")
    cmd.process.send_signal(signal.SIGINT)
    

if __name__ == '__main__':
    main()