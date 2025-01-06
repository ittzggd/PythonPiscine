ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello" : "titi!"}

#list
ft_list[1] = "World!"

#tuple
#Once a tuple is created, you cannot change its values. 
#Tuples are unchangeable, or immutable as it also is called.
t_list = list(ft_tuple)
t_list[1] = "Republic of Korea!"
ft_tuple = tuple(t_list)

#set
#Set items are unchangeable, meaning that we cannot change the items after the set has been created.
ft_set.remove("tutu!")
ft_set.add("Seoul!")

#dict
ft_dict["Hello"] = "42Seoul!"


#your code here
print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)