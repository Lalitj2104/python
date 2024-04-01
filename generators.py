def remote_contrtol_next():
    yield "hello"
    yield "how r u"
itr=remote_contrtol_next()
print(itr)
print(next(itr))
print(next(itr))
# print(next(itr))
