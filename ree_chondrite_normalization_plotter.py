def normalize_ree_data(input_values, reference_values):
    """
    Normalize REE data using chondrite reference values.
    
    Args:
        input_values (list): List of 14 input values in ppm for La-Lu
        reference_values (list): List of 14 chondrite reference values
    
    Returns:
        list: Normalized values (input/ref)
    """
    if len(input_values) != 14 or len(reference_values) != 14:
        raise ValueError("Both input and reference lists must have exactly 14 values")
    
    normalized = []
    for i in range(14):
        normalized.append(input_values[i] / reference_values[i])
    
    return normalized


def calculate_anomalies(normalized_values):
    """
    Calculate Ce/Ce* and Eu/Eu* anomalies.
    
    Args:
        normalized_values (list): List of 14 normalized REE values
    
    Returns:
        tuple: (Ce anomaly, Eu anomaly)
    """
    if len(normalized_values) != 14:
        raise ValueError("Normalized values list must have exactly 14 values")
    
    # Calculate Ce/Ce* = Ce_N / sqrt(La_N * Pr_N)
    ce_anomaly = normalized_values[1] / ((normalized_values[0] * normalized_values[2]) ** 0.5)
    
    # Calculate Eu/Eu* = Eu_N / sqrt(Sm_N * Gd_N)
    eu_anomaly = normalized_values[5] / ((normalized_values[4] * normalized_values[6]) ** 0.5)
    
    return ce_anomaly, eu_anomaly
