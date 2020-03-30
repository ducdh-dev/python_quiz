class User(object):
    def __init__(self, username, _id, xp, name):
        self.username = username
        self._id = _id
        self.xp = xp
        self.name = name

    def __getattr__(self, name):
        return "{} attribute is not defined".format(name)

    def __bool__(self):
        return all([True, True])


def user_attribute(attribute):
    user = User("anny_master", "1234567", "1500", "anny")
    print(bool(user))
    return getattr(user, attribute)


print(user_attribute("_id"))
print(user_attribute("abc"))
