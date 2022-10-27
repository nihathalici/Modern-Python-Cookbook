# Exer-12-Understanding-variables-references-and-assignment

mutable = [1, 1, 2, 3, 5, 8]
immutable = (5, 8, 13, 21)

mutable_b = mutable
immutable_b = immutable

#print(mutable_b is mutable)
#print(immutable_b is immutable)

mutable += [mutable[-2] + mutable[-1]]

immutable += (immutable[-2] + immutable[-1],)

#print(mutable_b)
#print(mutable is mutable_b)

print(immutable_b)
print(immutable)


