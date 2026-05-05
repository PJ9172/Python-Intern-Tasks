x = 1
def func():
    x = 10
    print("Printing local x : ",x)

# global keyword

print("Printing global x : ",x)
func()
def changing_global():
    global x
    x += 1
changing_global()
print("After changing global : ",x)


# nonlocal keyword
def myfunc1():
  x = "Jane"
  def myfunc2():
    nonlocal x
    x = "hello"
  myfunc2()
  return x

print(myfunc1())