"""
CARPI DAEMON COMMONS
(C) 2018, Raphael "rGunti" Guntersweiler
Licensed under MIT
"""
from logging import Logger
from time import sleep

from daemoncommons.daemon import Daemon, DaemonRunner
from daemoncommons.log import logger


class DemoDaemon(Daemon):
    def __init__(self):
        Daemon.__init__(self, "Demo Daemon")
        self._log: Logger = None

    def startup(self):
        self._log = log = logger(self.__class__.__name__)
        while True:
            log.debug("Demo Daemon is running fine :D")
            sleep(1)
            log.info("Demo Daemon is running fine :D")
            sleep(1)
            log.warning("Demo Daemon is running fine :D")
            sleep(1)
            log.error("Demo Daemon is running fine :D")
            sleep(1)
            log.fatal("Demo Daemon is running fine :D")
            sleep(1)

    def shutdown(self):
        self._log.info("Shutting down Daemon ...")


if __name__ == '__main__':
    dr = DaemonRunner('DEMO_CFG',
                      ['./demo.ini'])
    dr.run(DemoDaemon())
