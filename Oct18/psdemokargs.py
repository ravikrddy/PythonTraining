def tuner(**kwargs):
    """keyword argument parameter"""
    print(kwargs)


tuner()
tuner(brightness=1.2)
tuner(contrast=.8, brightness=.78, hue=.88)  # keyword arguments
