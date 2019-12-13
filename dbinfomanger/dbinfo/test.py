def use_logging(func):
  def _deco(*args,**kwargs):
    print("%s is running" % func.__name__)
    func(*args,**kwargs)
  return _deco
@use_logging
def bar(a,b):
  print('i am bar:%s'%(a+b))
@use_logging
def foo(a,b,c):
  print('i am bar:%s'%(a+b+c))
bar(1,2)
foo(1,2,3)