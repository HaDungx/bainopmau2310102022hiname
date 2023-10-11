#region debai
"""
--- ma debai / id
hi(name)

--- nopbai
00 fork tu bainopmau tren replit tu trang web duoiday 
   https://replit.com/@NamG1/bainopmau2310102022hiname

01 lam bai vao tep s00_bailam.py, chay Run de co ketqua tatca la 1
02a tao github repo, mo kiemtra tep s00_bailam.py, va lay diachi/url aka githubrepourl

02b dan diachi githubrepourl tu trang web duoiday
    https://forms.gle/UuuL3NCyCKLVFPiF8

--- debai / problem
Hay viet ham hi(name) xuat ra cau chao theo mota benduoi

--- vidu mau / testcase
Khi chay voi input           | Ketqua output
---------------------------- | -----------------
hi('Mom')                    | Hi Mom!
hi('')                       | Hi!
hi()                         | Hi!
hi(None)                     | Hi!
hi(name='Mom')               | Hi Mom!

------------------- mucdo: kho -----------------
hi('Mom', 'Dad')             | Hi Mom, and Dad!
hi('A', 'B', 'C')            | Hi A, B, and C!
hi('1', '22', '333', '4444') | Hi A, B, and C!
"""
#endregion debai

#region bailam
#             **kwargs to allow calling hi(name='xx') without error > TypeError: hi() got an unexpected keyword argument 'name'
def hi(*args, **kwargs):
  if len(args)==0:  # hi()  --> args = (,)
    if not kwargs:
      return 'Hi!'
    else:
      name = kwargs.get('name')
      if name:
        return f'Hi {name}!'
      else:
        return 'Hi!'

  if len(args)==1 and args[0] is None:  # hi(None)  --> args = (None,)
    return 'Hi!'

  if len(args)==1:  # hi('Mom') hi('')
    name = args[0]
    if name:
      return f'Hi {name}!'
    else:
      return 'Hi!'

  if len(args)>1:  # hi('Mom', 'Dad')
    namestr = ', '.join(args[0:-1])
    namestr = f'{namestr}, and {args[-1]}'
    return f"Hi {namestr}!"

if __name__=='__main__':
  print( hi('Mom') )  # Hi Mom!
  print( hi()      )  # Hi!
  print( hi(None)  )  # Hi!

  print( hi('Mom', 'Dad') )                # Hi Mom, and Dad!
  print( hi('A', 'B', 'C')  )              # Hi A, B, and C!
  print( hi('1', '22', '333', '4444')   )  # Hi A, B, and C!

  print( hi(name='Mom')   )  # Hi Mom!

#endregion bailam
