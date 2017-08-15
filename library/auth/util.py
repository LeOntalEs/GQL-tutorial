def issuperuser(user):
    return user.is_superuser
def islibstaff(user):
    return user.groups.filter(name__in=['library_staff']).exists()
def isstudent(user):
    return user.groups.filter(name__in=['student']).exists()
