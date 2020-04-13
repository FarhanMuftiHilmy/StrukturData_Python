x = {"Afghanistan" : 93,
"Albania" : 355,
"Algeria" : 213,
"Andorra" : 376,
"Angola" : 244,
"Antarctica" : 672}


print("Member name:", list(x.keys())[list(x.values()).index(355)])
print("Member value:", x["Afghanistan"])