teman_lama = ["wahyu","rasyid","adnin","nunu"]

print("teman lama")
nm = 1
for i in teman_lama:
    print(f"Nama teman ke-{nm} adalah {i}")
    nm += 1 

teman_lama.extend(["fadila","muhammad","adit"])



# print("")
# # ascending dan descending pada python 
# teman_lama.sort()
# print("ascending : ",teman_lama)
# teman_lama.reverse()
# print("descending : ",teman_lama)

# loop 
print("")
print("teman lama dan baru")
nm = 1
for i in teman_lama:
    print(f"Nama teman ke-{nm} adalah {i}")
    nm += 1
nm = ""
print(f"Nama teman ke-{nm} adalah {teman_lama}")

# print("")
# panjang = [pj for pj in teman_lama if len(pj) >= 6 ]
# print("nama yang lebih dari sama dengan 6 adalah : ",panjang)