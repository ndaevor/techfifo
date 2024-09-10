class A:
    def f(self):
        # Calls the method g() on the instance self
        return self.g()

    def g(self):
        # Returns the string 'A'
        return 'A'

class B(A):
    def g(self):
        # Overrides the method g() in class A
        return 'B'

a = A()
b = B()

# Calls the method f() on instance a of class A
print(a.f(),  # a.f() calls a.g() which is defined in class A and returns 'A'
      b.f())  # b.f() calls b.g() which is overridden in class B and returns 'B'

# Calls the method g() directly on instances a and b
print(a.g(),  # a.g() is defined in class A and returns 'A'
      b.g())  # b.g() is overridden in class B and returns 'B'
