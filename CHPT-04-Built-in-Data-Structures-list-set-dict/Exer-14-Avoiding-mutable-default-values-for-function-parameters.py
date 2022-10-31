# Exer-14-Avoiding-mutable-default-values-for-function-parameters

from collections import Counter
from random import randint, seed

def gather_stats(n, samples=1000, summary=Counter()):
    summary.update(
        sum(randint(1, 6) for d in range(n))
             for _ in range(samples))
    return summary

seed(1)
s1 = gather_stats(2)
print(s1)

###

seed(1)
mc = Counter()
gather_stats(2, summary=mc)
print(mc)

###

seed(1)
s3 = gather_stats(2)
print(s3)

print(s1 is s3)
print(s1)

###

def gather_stats(n, samples=1000, summary=None):
    if summary is None: summary = Counter()

###

def create_stats(n, samples=1000):
    return update_stats(n, samples, Counter())
def update_stats(n, samples=1000, summary):
    summary.update(
        sum(randint(1, 6) for d in range(n))
          for _ in range(samples))

###

def gather_stats(n, samples=1000, summary_func=lambda x: Counter(x)):
    summary = summary_func(
        sum(randint(1, 6) for d in range(n))
            for _ in range(samples))
    return summary

###

seed(1)
gather_stats(2, 12, summary_func=list)

###

seed(1)
gather_stats(2, 12)
