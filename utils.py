import numpy as np
from datetime import datetime

def generate_numero():
    now = datetime.now()
    tms = int(datetime.timestamp(now))
    return np.base_repr(tms, base=36)

