# <--- Dependencies --->
import sys
sys.path.append("..")
import ErrorHandler
try:
    import math as mt
except:
    ErrorHandler.ErrorHandle("Missing Dependency: Math",1)
# <--- Dependencies --->
class Base:
    # <-- Mean -->
    def mean(array):
        """ Returns the Average of an Array """
        observations = len(array)
        # ∑ divided by n
        average = (sum(array) / observations)
        return(average)
    # <-- Variance -->
    def variance(array):
        """ Returns the Variance of an Array """
        me = mean(array)
        # ∑ - mu
        sq = sum(array) - me
        # Square ∑ - mu
        squared_mean = sq ** 2
        return(squared_mean)
    # <-- Standard Deviation -->
    def standard_deviation(array):
        """ Returns the Standard Deviation of an Array"""
        mean = mean(array)
        # Subtract mu from ∑
        sq = sum(array) - mean
class Inferential:
    # <-- Student T Test -->
    def student_t(sample,general):
        """ Returns a P value between Sample and General"""
        # Get the mean
        sampmean = Base.mean(sample)
        genmean = Base.mean(general)
        samples = len(sample)
        std = Base.standardize(general)
        t = (sampmean - genmean) / (std / mt.sqrt(samples))
        return(t)
    # <-- Student F Test -->
    def student_f(sample,general):
        """ Returns an F value between Sample and General"""
        totvariance = Base.variance(general)
        sampvar = Base.variance(sample)
        f = sampvar / totvariance
        return(f)
class Bayesian:
    #P = prob, A = prior, B = Evidence,
    # <-- Bayes Theorum -->
    def bay_ther(p,a,b):
        """ Takes three integers, and returns probability as float"""
        psterior = (p * (b | a) * p * (a)) / (p * b)
        return(psterior)
    # <-- Conditional Probability -->
    def cond_prob(p,a,b):
        """ Returns conditional probability as float """
        psterior = bay_ther(p,a,b)
        cond = p * (a | b)
        return(cond)
