"""Created on Oct 30, 2018.

Code for dealing with photodetectors
@author: cdleong
"""


class Detector(object):
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
        time_betwixt_samples_sec = 1/self.sample_rate_times_per_second
        return self.integration_time_seconds/time_betwixt_samples_sec


if __name__ == "__main__":
    first_detector_from_slide_20_199 = Detector(sample_rate_times_per_second=44.1*10**3,
                                                integration_time_seconds=1*10**-6)
    first_duty_cycle = first_detector_from_slide_20_199.calculate_duty_cycle()
    print(f"duty cycle (should be <0.045): {first_duty_cycle}")

    second_detector = Detector(sample_rate_times_per_second=30,
                               integration_time_seconds=20*10**-3)
    second_duty_cycle = second_detector.calculate_duty_cycle()
    print(f"duty cycle (should be ~0.6): {second_duty_cycle}")
