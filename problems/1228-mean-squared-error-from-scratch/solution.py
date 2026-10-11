import torch

def mse(pred, target):
    """
    Compute mean squared error between pred and target.

    Args:
        pred (torch.Tensor): Predicted values.
        target (torch.Tensor): Ground-truth values (same shape as pred).

    Returns:
        float: Mean of squared differences.
    """
    # TODO

    squared_diff = (pred - target) ** 2

    mean_list = torch.mean(squared_diff)

    return mean_list.item()

