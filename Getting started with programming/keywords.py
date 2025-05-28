import keyword

print(keyword.kwlist)
print(keyword.softkwlist)
  
key =  input ("Enter a keyword :")
result = keyword.iskeyword(key)
print(result)

