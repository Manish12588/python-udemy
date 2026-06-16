chai_type = "Ginger tea"
customer_name = "Manish"
print(f"Order for {customer_name} : {chai_type} please!")

chai_description = "Aromatic and Bold"

# Indexing -> in Aromatic idex 0 is A
# last number is not inclusive
# Slicing
print(f"First word: {chai_description[0:8:1]}")  # here 1 means every character of word
print(
    f"Every Second Character of First Word: {chai_description[0:8:2]}"
)  # here 2 means every second character of word

print(f"Last word: {chai_description[12::]}")  # here 1 means every character of word

print(f"Reverse String: {chai_description[::-1]}")  # [start:stop:step]

label_text = "Chai Spécial"  # for special character we can use encode function
print(f"Non encoded label => {label_text}")
encoded_label = label_text.encode("utf-8")
print(f"encoded label => {encoded_label}")
decoded_label = encoded_label.decode("utf-8")
print(f"decoded label => {decoded_label}")
