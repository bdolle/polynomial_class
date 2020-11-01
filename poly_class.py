# Copyright 2020 Brian Dolle bdolle@bu.edu
# Copyright 2020 Poras Shroff pshroff4@bu.edu

class Polynomial():
  """ Modelling Polynomials """

  def __init__(self,seq = [0]):
    "Create a dictionary where values are mapped to"
    "descending indexes and 0s are ignored"
    self.seq = seq
    self.D = dict()
    # print(len(self.seq)-1)
    a_list = []
    for i in range(len(self.seq)):
      a_list.append(self.seq[i])
    #   a_list[i] = self.seq[i]
    a_list.reverse()
    for i in range(len(a_list)):
      if a_list[i] != 0:
        self.D[i] = a_list[i]
    # print(self.D)


  def __repr__(self):
    my_max = max(self.D.keys())
    my_min = min(self.D.keys())
    my_list = []

    if my_min < 0:
      for i in range(my_min, my_max+1):
        if i in self.D:
          my_list.append(self.D[i])
        else:
          my_list.append(0)

    if my_min >= 0:
      for i in range(my_max+1):
        if i in self.D:
          my_list.append(self.D[i])
        else:
          my_list.append(0)

    my_list.reverse()
    return str(my_list)


  def __str__(self):
    my_max = max(self.D.keys())
    my_min = min(self.D.keys())
    my_list = []

    if my_min < 0:
      for i in range(my_min, my_max+1):
        if i in self.D:
          my_list.append(self.D[i])
        else:
          my_list.append(0)

    if my_min >= 0:
      for i in range(my_max+1):
        if i in self.D:
          my_list.append(self.D[i])
        else:
          my_list.append(0)

    my_list.reverse()
    return str(my_list)


  def __getitem__(self, index):
    "getting items"
    self.index = index
    if self.index in self.D:
      return self.D[self.index]
    else:
      return 0


  def __setitem__(self, key, value):
    "Setting items"
    self.D[key] = value


  def __add__(self,value):
    "Return self+value."
    self.b = dict()
    new_p = Polynomial()
    # pull all the non-zero entries in d
    for i in self.D:
      # if there is also an entry of same key in c, add them, but
      # only if adding them doesn't give zero. If it does, skip.
      if i in value.D:
        if self.D[i] + value.D[i] != 0:
          self.b[i] = self.D[i] + value.D[i]
        else:
          pass
      # If there not an entry of same key in c, just set
      else:
        self.b[i] = self.D[i]

    # Now check for all non-zero entries of c
    for i in value.D:
      # If there is a value in d at i, pass, bc did it above 
      if i in self.D:
        pass
      #  If not value in d at i, just set b = c
      else:
        self.b[i] = value.D[i]
    # print(b)
    new_p.D = self.b
    return new_p

  def __sub__(self,value):
    "Return self+value."
    self.b = dict()
    new_p = Polynomial()
    # pull all the non-zero entries in d
    for i in self.D:
      # if there is also an entry of same key in c, add them, but
      # only if adding them doesn't give zero. If it does, skip.
      if i in value.D:
        if self.D[i] - value.D[i] != 0:
          self.b[i] = self.D[i] - value.D[i]
        else:
          pass
      # If there not an entry of same key in c, just set
      else:
        self.b[i] = self.D[i]

    # Now check for all non-zero entries of c
    for i in value.D:
      # If there is a value in d at i, pass, bc did it above 
      if i in self.D:
        pass
      #  If not value in d at i, just set b = c
      else:
        self.b[i] = -value.D[i]
    # print(b)
    new_p.D = self.b
    return new_p


  def __radd__(self,value):
    "Return self+value."
    self.b = dict()
    new_p = Polynomial()
    # pull all the non-zero entries in d
    for i in self.D:
      # if there is also an entry of same key in c, add them, but
      # only if adding them doesn't give zero. If it does, skip.
      if i in value.D:
        if self.D[i] + value.D[i] != 0:
          self.b[i] = self.D[i] + value.D[i]
        else:
          pass
      # If there not an entry of same key in c, just set
      else:
        self.b[i] = self.D[i]

    # Now check for all non-zero entries of c
    for i in value.D:
      # If there is a value in d at i, pass, bc did it above 
      if i in self.D:
        pass
      #  If not value in d at i, just set b = c
      else:
        self.b[i] = value.D[i]
    # print(b)
    new_p.D = self.b
    return new_p


  def __mul__(self, value):
    new_p = Polynomial()
    self.b = dict()
    for i in self.D:
      for j in value.D:
        if (i+j) in self.b:
          self.b[i+j] = self.b[i+j] + (self.D[i] * value.D[j])
        else:
          self.b[i+j] = self.D[i] * value.D[j]
    new_p.D = self.b
    return new_p

  def __rmul__(self, value):
    new_p = Polynomial()
    self.b = dict()
    for i in self.D:
      for j in value.D:
        if (i+j) in self.b:
          self.b[i+j] = self.b[i+j] + (self.D[i] * value.D[j])
        else:
          self.b[i+j] = self.D[i] * value.D[j]
    new_p.D = self.b
    return new_p

  def deriv(self):
    new_p = Polynomial()
    self.b = dict()
    for i in self.D:
      if (i*self.D[i]) != 0:
        self.b[i-1] = (i*self.D[i])
      else:
        pass
    new_p.D = self.b
    return new_p

  def eval(self,arg):
    sum = 0
    for i in self.D:
      sum = sum + self.D[i]*(arg**i)
    return sum

  def __eq__(self, other):
    if len(self.D) != len(other.D):
      return False
    else:
      for i in self.D:
        if i in other.D:
          if other.D[i] != self.D[i]:
            return False
        else:
            return False
      return True


  def __ne__(self, other):
    if len(self.D) != len(other.D):
      return True
    else:
      for i in self.D:
        if i in other.D:
          if other.D[i] != self.D[i]:
            return True
        else:
            return True
      return False
