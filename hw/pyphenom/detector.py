"""Created on Oct 30, 2018.

Code for dealing with photodetectors
@author: cdleong
"""


class detector(object):
    """It's a detector.

    It knows or can calculate things like:
        * duty cycle
        * integration time
        * sampling rate
        * quantum efficiency
    """

    def __init__(self, quantum_efficiency=1.0,
                 sample_rate_times_per_second=1.0,
                 integration_time_seconds=0.1):
        """Constructor.

        Unless otherwise specified it has a perfect quantum efficiency,
        samples at a rate of once per second
        and has a 0.1s integration time
        """
        self.quantum_efficiency = quantum_efficiency
        self.sample_rate_times_per_second = sample_rate_times_per_second
        self.integration_time_seconds = integration_time_seconds

    def calculate_duty_cycle(self):
        """Calculate duty cycle."""
        return self.integration_time_seconds/self.sample_rate_times_per_second
