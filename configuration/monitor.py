'''This file contain a overview of how the monitors are configured.'''

from __future__ import print_function

BACKEND_PYGLET = "pyglet"
BACKEND_PYGAME = "pygame"

import json

class Monitor(dict):
    '''Contains the general information about how the monitors are configured
    '''

    BACKEND = "backend"
    TEST_MONITOR = "test-monitor"

    def __init__(self, backend=BACKEND_PYGLET, Dict=None):
        '''Initializes a Monitor configuration
        '''
        if (not Dict):
            self[Monitor.BACKEND] = backend
            self[Monitor.TEST_MONITOR] = 0
        else:
            super(Monitor, self).__init__(Dict)

    @staticmethod
    def from_json(json_str):
        '''Loads a monitor configuration from a json formatted string'''
        d = json.loads(json_str)
        return Monitor(Dict=d)

    def as_json(self, pretty=True, sort_keys=True):
        '''Return self as json serialized.'''
        s = json.dumps(self, indent=4 if pretty  else None, sort_keys=True)
        return s
    
    def backend(self):
        '''Returns the backend that is going to be used'''
        return self[self.BACKEND]
    
    def test_monitor(self):
        '''Returns the monitor where the testwindow should be displayed'''
        return self[self.TEST_MONITOR]

if __name__ == "__main__":
    m = Monitor()
    jstr = m.as_json()
    mcopy = Monitor.from_json(jstr)
    assert(mcopy == m)
    print (jstr)

