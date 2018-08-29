import numpy.random


class TimeRandomizer:

    def __init__(self, numpy_random_distribution, normal_mean=None, normal_stddev=None, gamma_shape=None,
                 gamma_scale=None, triangle_min=None, triangle_mode=None, triangle_max=None, uniform_min=None,
                 uniform_max=None):
        """Constructor is only setup for common distributions. Refer to numpy.random docs for other dist types,
        and create member variables, constructor params, and modify generate_random_sample() accordingly.

        :param numpy_random_distribution: string
        """

        self.distribution_type = numpy_random_distribution

        self.normal_mean = normal_mean
        self.normal_stddev = normal_stddev

        self.gamma_shape = gamma_shape
        self.gamma_scale = gamma_scale

        self.triangle_min = triangle_min
        self.triangle_mode = triangle_mode
        self.triangle_max = triangle_max

        self.uniform_min = uniform_min
        self.uniform_max = uniform_max

    def generate_random_sample(self):
        """Generates random sample from distribution type using inverse cumulative probability."""
        sample = None

        if self.distribution_type == "normal":
            sample = numpy.random.normal(self.normal_mean, self.normal_stddev, 1)

        elif self.distribution_type == "gamma":
            sample = numpy.random.gamma(self.gamma_shape, self.gamma_scale, 1)

        elif self.distribution_type == "triangular":
            sample = numpy.random.triangular(self.triangle_min, self.triangle_mode, self.triangle_max)

        elif self.distribution_type == "uniform":
            sample = numpy.random.uniform(self.uniform_min, self.uniform_max)

        try:
            val = sample[0]
            return round(val)
        except:
            return round(sample)



