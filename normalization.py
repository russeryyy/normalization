def normalize(instance_value, min_value, max_value):
    normalized_value = (instance_value - min_value) / (max_value - min_value)
    return normalized_value
