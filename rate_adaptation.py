class DynamicNebulaRateAdaptation:
    def __init__(self):
        self.base_rate = 1000  # Base data rate in bytes per second
        self.rate_factors = {'excellent': 2.0, 'good': 1.5, 'fair': 1.0, 'poor': 0.5}

    def adjust_rate(self, signal_quality):
        if signal_quality > 80:
            factor = self.rate_factors['excellent']
        elif signal_quality > 60:
            factor = self.rate_factors['good']
        elif signal_quality > 40:
            factor = self.rate_factors['fair']
        else:
            factor = self.rate_factors['poor']
        return int(self.base_rate * factor)
