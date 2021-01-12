#!/usr/bin/env python
# coding: utf-8

from types import ModuleType

# ### Modules
# 
# So, modules are instances of the `ModuleType` class.

auth_mod  = ModuleType('Auth',doc='This is an authentication module')

auth_mod

help(auth_mod)


# OK, so now let's add some functionality to it by simply setting some attributes:

from collections import namedtuple


auth_mod.Login = namedtuple('Login', 'username password')





def len_validate(user_name,password):
    if len(user_name) >1 and len(password) > 1:
        print("len matched")
    else:
        raise ValueError("User/Password fields cannot be empty")   


len_validate('','')


auth_mod.lvalidate = len_validate


auth_mod.__dict__


user1 = auth_mod.Login("Steve","s$57*&^")


user1


auth_mod.lvalidate(*user1)





