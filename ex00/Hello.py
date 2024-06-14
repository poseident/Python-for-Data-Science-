ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello" : "titi!"}


ft_list[1] = "World!" #Lists are mutable in Python, so you can directly modify elements by index.
ft_tuple = ("Hello", "France!") #tuple immutability can't modify directly like a const;
ft_set.add("Mulhouse!") #unordered list
ft_set.remove("tutu!")
ft_dict["Hello"] = "42Mulhouse!" #key with value


print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)