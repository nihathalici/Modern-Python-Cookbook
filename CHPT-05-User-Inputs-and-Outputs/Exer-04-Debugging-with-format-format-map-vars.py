# Exer-04-Debugging-with-format-format-map-vars

import statistics

size = [2353, 2889, 2195, 3094,
725, 1099, 690, 1207, 926,
758, 615, 521, 1320]

mean_size = statistics.mean(size)
std_size = statistics.stdev(size)
sig1 = round(mean_size + std_size, 1)
#print([x for x in size if x > sig1])

print(
    "mean={mean_size:.2f}, std={std_size:.2f}".format_map(vars())
)

print(
    "mean={mean_size:.2f}, std={std_size:.2f},"
    " limit2={sig2:.2f}"
    .format( sig2=mean_size+2*std_size, **vars() )
)
