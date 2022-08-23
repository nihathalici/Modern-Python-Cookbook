# Exer-06-Building-complex-strings-with-template-format

id = "IAD"
location = "Dulles Intl Airport"
max_temp = 32
min_temp = 13
precipitation = 0.4

# '{id:3s} : {location:19s} : {max_temp:3d} / {min_temp:3d} / {precipitation:5.2f}'

print( '{id:3s} : {location:19s} : {max_temp:3d} / {min_temp:3d} / {precipitation:5.2f}'.format(
    id=id, location=location, max_temp=max_temp,
    min_temp=min_temp, precipitation=precipitation
) )

###

data = dict(
    id=id, location=location, max_temp=max_temp,
    min_temp=min_temp, precipitation=precipitation
)

print( '{id:3s} : {location:19s} : {max_temp:3d} / {min_temp:3d} / {precipitation:5.2f}'.format_map(data) )

print( '{id:3s} : {location:19s} : {max_temp:3d} / {min_temp:3d} / {precipitation:5.2f}'.format_map(vars()) )

class Summary:
    def __init__(self, id, location, min_temp, max_temp, precipitation):
        self.id = id
        self.location = location
        self.min_temp = min_temp
        self.max_temp = max_temp
        self.precipitation = precipitation
    
    def __str__(self):
        return '{id:3s} : {location:19s} : {max_temp:3d} / {min_temp:3d} / {precipitation:5.2f}'.format_map(vars(self))

s= Summary('IAD', 'Dulles Intl Airport', 13, 32, 0.4)
print(s)
