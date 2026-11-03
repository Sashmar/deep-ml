import numpy as np

def compute_norm(arr: np.ndarray, norm_type: str) -> float:
    """
    Compute the specified norm of the input array.

    'l1', 'l2' and 'linf' are entrywise norms and accept a 1D or 2D array.
    'frobenius' is a matrix norm and must raise a ValueError if arr is not 2D.

    Args:
        arr: Input numpy array (1D or 2D)
        norm_type: Type of norm ('l1', 'l2', 'linf', or 'frobenius')

    Returns:
        The computed norm as a float
    """
    # Your code here


    if norm_type == 'l1':
        return float(np.abs(arr).sum())

    elif norm_type == 'l2':
        new_arr = arr * arr
        sum_new = np.sum(new_arr)
        sqr_arr = np.sqrt(sum_new)
        return float(sqr_arr)

    elif norm_type == 'linf':
        return float(np.abs(arr).max())


    elif norm_type == 'frobenius':
        if arr.shape != (2,2):
            raise ValueError

        else:
            new_arr = arr * arr
            sum_new = np.sum(new_arr)
            sqr_arr = np.sqrt(sum_new)
            return float(sqr_arr)

    else:
        raise ValueError
