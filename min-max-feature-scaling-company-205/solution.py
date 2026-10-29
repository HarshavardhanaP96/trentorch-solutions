import numpy as np

def solve(x):
    """Implement min-max-feature-scaling from the mathematical contract in README.md."""

    x=np.array(x,dtype=float);

    x_min=np.min(x)
    x_max=np.max(x)

    if x_max==x_min:
        return [0.0]*len(x)

    scaled=(x-x_min)/(x_max-x_min)
    return scaled.tolist()
    pass
