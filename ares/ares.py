import numpy as np


def _intermediate_point(x):
    """Find candidate for interval sub-division"""
    r = (x[-1] - x[0])/(len(x)-1)
    xlin = x[0] + np.arange(len(x)) * r
    abserr = np.abs(x - xlin)
    i = np.argmax(abserr)
    err = abserr[i]
    if i == len(x) - 1:
        i = 0
    return i, err


def adaptive_resampling_index(y, thresholds=0, start_stride=None):
    """Pick sub-samples that preserve overall appearance of the graph"""
    if isinstance(thresholds, (int, float)):
        thresholds = [thresholds]
    thresholds = sorted(thresholds, reverse=True)
    num_scales = len(thresholds)
    if not start_stride:
        start_stride = len(y) - 1    
    idx = np.zeros(len(y))
    idx[::start_stride] = num_scales
    idx[-1] = num_scales
    max_err = np.inf
    for scale, threshold in enumerate(thresholds):
        while max_err > threshold:
            points = np.nonzero(idx)[0]
            max_err = 0
            for start_pt, end_pt in zip(points[:-1], points[1:]):
                rel_idx, err = _intermediate_point(y[start_pt:end_pt+1])
                max_err = max(max_err, err)
                if rel_idx and err > threshold:
                    idx[start_pt + rel_idx] = num_scales - scale
    return idx
