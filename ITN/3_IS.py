# Curiously:

a = 123
b = 123
print(str(a is b))


a = 123.
b = 123.
print(str(a is b))

y = a + b
z = bool(y)
print(str(z))

input()


# Seems a is b being more or less defined as id(a) == id(b). It is easy to make bugs this way:
#
# basename, ext = os.path.splitext(fname)
# if ext is '.mp3':
#     # do something
# else:
#     # do something else
# Some fnames unexpectedly ended up in the else block. The fix is simple, we should use ext == '.mp3' instead,
# but nonetheless if ext is '.mp3' on the surface seems like a nice pythonic way to write this and it's more readable than the "correct" way.
#
# Since strings are immutable, what are the technical details of why it's wrong? When is an identity check better, and when is an equality check better?

# Here is an easy rule (unless you want to go to theory in Python interpreter or building frameworks doing funny things with Python objects):
#
# Use is only for None comparison.
#
# if foo is None
# Otherwise use ==.
#
# if x == 3
# Then you are on the safe side. The rationale for this is already explained int the above comments. Don't use is if you are not 100% sure why to do it.