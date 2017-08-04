class Container(object):
    """ Holds hashable objects. Objects may occur 0 or more times """
    def __init__(self):
        """ Creates a new container with no objects in it. I.e., any object
            occurs 0 times in self. """
        self.vals = {}
    def insert(self, e):
        """ assumes e is hashable
            Increases the number times e occurs in self by 1. """
        try:
            self.vals[e] += 1
        except:
            self.vals[e] = 1
    def __str__(self):
        s = ""
        for i in sorted(self.vals.keys()):
            if self.vals[i] != 0:
                s += str(i)+":"+str(self.vals[i])+"\n"
        return s


class Bag(Container):

    def remove(self, e):
        if e not in self.vals:
            return
        self.vals[e] -= 1

       # if self.vals[e] < 1:
          #  del (self.vals[e])



    def count(self, e):
        """ assumes e is hashable
            Returns the number of times e occurs in self. """
        # write code here
        return self.vals.get(e, 0)

    def __add__(self, other):
        result = self.__class__()
        result.vals.update(self.vals)
        for value, count in other.vals.items():
            for _ in range(count):
                result.insert(value)
        return result


class ASet(Container):

    def remove(self, e):
        if e not in self.vals:
            return
        self.vals[e] -= 1

        if self.vals[e] < 2:
         del (self.vals[e])


    def is_in(self, e):
        """assumes e is hashable
           returns True if e has been inserted in self and
           not subsequently removed, and False otherwise."""
        if e in self.vals:
            return True
        else:
            return False


d1 = ASet()
d1.insert(4)
d1.insert(4)

d1.remove(2)
print(d1)

d1.remove(4)
print(d1)



d1 = ASet()
d1.insert(4)
d1.insert(4)
d1.insert(4)
d1.remove(4)
print(d1.is_in(4))