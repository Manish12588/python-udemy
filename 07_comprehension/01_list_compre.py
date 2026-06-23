menu = ["Masala chai", "Iced lemon tea", "Green tea", "Iced peach tea", "Ginger tea"]

# [expression for item in iterable if condition]
# [<expression:tea> for <item:tea> in <iterable:menu> if <condition>]
iced_tea = [tea for tea in menu if "Iced" in tea]
print(iced_tea)
