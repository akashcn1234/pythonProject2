class A:
    def show(self):
        print("\n A's method")
class B(A):
    def show(self):
     print("B's method")
b=B()
b.show()
