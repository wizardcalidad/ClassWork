# x=-2
# # if x == 6 :
# #     print('Is 6')
# #     print('Is Still 6')
# #     print('Third 6')
# # x = 0
# # if x < 2 :
# #     print('Small')
# # elif x < 10 :
# #     print('Medium')
# # else :
# #     print('LARGE')
# # print('All done')
# if x < 2 :
#     print('Below 2')
# elif x >= 2 :
#     print('Two or more')
# else :
#     print('Something else')
# astr = 'Hello Bob'
# istr = int(astr)
# print('First', istr)
# astr = '123'
# istr = int(astr)
# print('Second', istr)
# astr = 'Hello Bob'
# istr = 0
# try:
#     istr = int(astr)
# except:
#     istr = -1
hrs = input("Enter Hours:")
rate = input("Enter rate per hours:")
try:
    h = float(hrs)
    r = float(rate)
except:
    print("please,put numeric values")
    quit()
if h <= 40:
    pay = h * r
    print(pay)
elif h>=40:
    excess = h - 40
    pay = excess * r * 1.5 + 40 * r
    print(pay)