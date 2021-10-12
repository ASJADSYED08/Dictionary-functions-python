d1={"ASJAD":"BBQ","ANSAR":"CHAPLI KABAB","ALI":"CHINEESE",
    "ZARRAR":{"ROTI":"FISH","B":"PRAWN"}}
d1["AFFAN"]="pizza"    
print(d1)
print(d1.keys())
print(d1.items())
del d1["AFFAN"]
print(d1)
d1.update({"SYED":"BIRYANI"})
print(d1)
