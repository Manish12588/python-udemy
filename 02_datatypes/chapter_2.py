# Mutable and Immutable
# set is a datatype which is collection of things 

spice_mix = set()
print(f"Initial spice mix id: {id(spice_mix)}")
print(f"set => {spice_mix}")

spice_mix.add("Ginger")
spice_mix.add("cardemom")

print(f"after spice mix id: {id(spice_mix)}")
print(f"set => {spice_mix}")

# Initial spice mix id: 131927117104736
# after spice mix id: 131927117104736