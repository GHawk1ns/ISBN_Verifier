import string
#strips any spaces or hyphens then checks ISBN for correct length and characters
# if it meets requirements, the string is returned as a list
def strip_check_list(isbn):
 isbn = isbn.replace('-','')
 isbn = isbn.replace(' ','')
 if len(isbn)==10:
  if isbn[:-1].isdigit ()==True:
   if isbn[9].isdigit()==True or isbn[9]=='x' or isbn[9]=='X':
    isbn_list = list(isbn)
    return isbn_list
 return "ISBN is invalid"
#converts x to 10 then creatse a new list of the partial sums of the isbn
def partial_sum_1(isbn):
 if isbn=="ISBN is invalid":
  pass
 else:
  if isbn[9]=='x':
   isbn.remove('x')
   isbn.append('10')
  if isbn[9]=='X':
   isbn.remove('X')
   isbn.append('10')
  
  s_1=[]
  sum = 0
  for ch in isbn:
   x = int(ch)
   sum = sum + x 
   s_1.append(sum)
   return s_1

def main():
 in_file = open ('isbn.txt','r')
 for line in in_file:
  line = line.rstrip("\n")   
  line = strip_check_list(line)
  print line,
  s1 = partial_sum_1(line)
  print ' is Valid'
 in_file.close()

main()
