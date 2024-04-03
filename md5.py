import hashlib
str2hash = "484"
result = hashlib.md5(str2hash.encode())
m = hashlib.sha256(str2hash.encode())
print(result.hexdigest())
print(result.digest_size)
print("The hexadecimal equivalent of hash using sha256 is :",end="")
print(m.digest())
print(m.hexdigest())
print(m.digest_size)
items = [b'Hello',b' ',b'world']
h = hashlib.md5()
for item in items:
    h.update(item)
    print("Hash Update Demo:", h.hexdigest())
    print("Iteratively updated hash digetsSize", h.digest_size)
