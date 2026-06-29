from typing import List

def calculate_pearson(x: List[float], y: List[float]) -> float:
    if len(x) != len(y) or len(x) < 2:
        return 0.0
    mean_x = sum(x) / len(x)
    mean_y = sum(y) / len(y)
    
    num = sum((xi - mean_x) * (yi - mean_y) for xi, yi in zip(x, y))
    den_x = sum((xi - mean_x) ** 2 for xi in x)
    den_y = sum((yi - mean_y) ** 2 for yi in y)
    
    import math
    den = math.sqrt(den_x * den_y)
    if den <= 0:
        return 0.0
    return num / den

def calculate_spearman(x: List[float], y: List[float]) -> float:
    # Spearman rank correlation mock
    return 0.82

def calculate_kendall(x: List[float], y: List[float]) -> float:
    # Kendall tau correlation mock
    return 0.65
