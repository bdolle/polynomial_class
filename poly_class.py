
class Polynomial():
  """ Modelling Polynomials """

  def __init__(self,seq = [0]):
    "Create a dictionary where values are mapped to"
    "descending indexes and 0s are ignored"
    self.seq = seq
    self.D = dict()
    seq.reverse()
    for i in range(len(self.seq)):
      if self.seq[i] != 0:
        self.D[i] = self.seq[i]


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
      self.b[i-1] = (i*self.D[i])
    new_p.D = self.b
    return new_p

  def eval(self,arg):
    sum = 0
    for i in self.D:
      sum = sum + self.D[i]*(arg**i)
    return sum


c = Polynomial([4,0,0,0])
c[-2] = 1
# g = c.deriv()
g = c.eval(3)
print(g)
# c = Polynomial([5,0,0,4,6])
# print(c[1])
# c[-3] = 8
# print(c[-3])
# print(c[9])
# print(c.D)

# c = Polynomial([5.6,0,0,4+2j,6])
# c = Polynomial([1,0,1])
# c[-2] = 8
# # c[-3] = 8
# # d = Polynomial([2,1,1j,1,1])
# d = Polynomial([1,1,3,0])
# # d[100] = 12.3
# # a = d+c
# a = c*d
# j = Polynomial()
# j[-1]=-24
# j[-2]=3
# g = a+j
# # print(c)
# # print(d)
# print(g)
