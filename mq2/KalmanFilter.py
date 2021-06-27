import math


class KalmanFilter:
    _err_measure: float
    _err_estimate: float
    _q: float
    _current_estimate: float
    _last_estimate: float
    _kalman_gain: float

    def __init__(self,  mea_e,  est_e,  q):
        self.mea_e = mea_e
        self.est_e = est_e
        self.q = q
        self._err_measure = 0
        self._err_estimate = 0.1
        self._q = 0
        self._current_estimate = 0
        self._last_estimate = 0
        self._kalman_gain = 0

    def updateEstimate(self, mea):

        _kalman_gain = self._err_estimate / \
            (self._err_estimate + self._err_measure)
        _current_estimate = self._last_estimate + \
            _kalman_gain * (mea - self._last_estimate)
        _err_estimate = (1.0 - _kalman_gain)*self._err_estimate + \
            math.fabs(self._last_estimate-_current_estimate)*self._q
        _last_estimate = _current_estimate

        return _current_estimate

    def setMeasurementError(self, mea_e):
        _err_measure = mea_e

    def setEstimateError(self, est_e):
        _err_estimate = est_e

    def setProcessNoise(self, q):
        _q = q

    def getKalmanGain(self):
        return self._kalman_gain

    def getEstimateError(self):
        return self._err_estimate
