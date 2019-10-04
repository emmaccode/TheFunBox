from DS import Stats
class ArrayScale:
    # <-- ArbitraryRescale -->
    def arbitrary_rescale(array):
        """ Basic Arbitrary Rescaling """
        v = []
        a = min(array)
        b = max(array)
        for i in array:
            x = (a + (i - a * i)) * ((b - a) / (b - a))
            v.append(x)
        return(v)
    # <-- STD based standardization -->
    def standardize(array):
        """ Returns a Standardized Array """
        v = []
        for i in array:
            min = min(array)
            max = max(array)
            x = i
            x = (x - min) / (max - min)
            v.append(x)
        return(v)
    # <-- Mean Normalization -->
    def mean_normalize(array):
        """ Mean Normalize an Array"""
        avg = Stats.Base.mean(array)
        v = []
        a = min(array)
        b = max(array)
        for i in array:
            m = (i-avg) / (b-a)
            v.append(m)
        return(v)
