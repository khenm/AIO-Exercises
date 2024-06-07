def MD_nRE(y: float, y_hat: float, n: int, p: int) -> float:
    """Compute the mean difference of nth Root Error 

    Args:
        y (float): target value
        y_hat (float): predict value
        n (int): n-th root of values
        p (int): p-th power of loss function

    Returns:
        float: loss value
    """
    md_nre_loss: float = (y ** (1 / n) - y_hat ** (1 / n)) ** p
    return md_nre_loss

# example
MD_nRE(y = 100, y_hat = 99.5, n = 2, p = 1)