# String formating
# ime_clanka = "Arctic_Ocean"

# url = f"https://en.wikipedia.org/wiki/{ime_clanka}"
# print(url)

# ime = "Gregor"
# starost = 50
# moj_string = f"{ime:!^10} je star {starost:*>e} let."
# print(moj_string)

# ime = "Gregor"
# starost = 50
# moj_string = "Živjo {}. Star si {} let.".format(ime, starost)
# print(moj_string)

# %-formating
ime = "Gregor"
starost = 50.12345678
moj_string = "Živjo %s . Star si %d let." % (ime, starost)
print(moj_string)

# print "hello world"