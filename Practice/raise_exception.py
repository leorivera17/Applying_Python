# Trace the following function
# def myfunc(n):
#     try:
#         if (n < 0):
#             raise TypeError
#             print('n<0 : ', n)
#         print('after if n<')
#         if (n == 0 or n == 15):
#             raise ValueError
#     except TypeError:
#         print('My Type Error! n=',n)
#     except ValueError:
#         print('My value Error! n=',n)
#     finally:
#         print('Done. ')
#     print('After Finally!')
#
# myfunc(0)
# myfunc(-1)
# myfunc(25)
#
#
# def calc(a: int, b: int) -> float:
#     try:
#         if b == 5:
#             raise ZeroDivisionError()
#         if b == 1.0:
#             raise ValueError()
#         c = a + 1 / b
#         if c > 100:
#             raise OverflowError()
#         else:
#             return c
#     except ZeroDivisionError:
#         print('in zero division....')
#     except ValueError:
#         print('in value error ....')
#     except OverflowError:
#         print('in OverflowError ... ')
#     finally:
#         print('in finaly....')
#     return a
#
#
# print('a = 7, b = 2: ', calc(7, 2))
# print('a = 1, b = 5: ', calc(1, 5.0))
# print('a = 110, b = 2: ', calc(110, 2))





