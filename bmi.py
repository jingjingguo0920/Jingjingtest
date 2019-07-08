##g=郭晶晶,z=赵方亮,x=胥非
g_weight = 45
z_weight = 90
x_weight = 80
g_height=1.72
z_height=1.8
x_height=1.9
g=g_weight+1.5
z=z_weight+2.5
x=x_weight+1.5
print('郭晶晶喝完奶茶之后的体重:',g)
print('郭晶晶的身高:',g_height)
print('赵方亮吃完炸鸡的体重:',z)
print('赵方亮的身高:',z_height)
print('胥非吃完锅盔的体重:',x)
print('胥非的身高:',x_height)
print('bmi参考标准:WHO标准-->who,亚洲标准--->asia,中国标准-->china')

bmi=1
def bmi_function(height,weight,item):
   bmi=weight /(height*height)
   if item=='who':

      if bmi<18.5:
          print('偏瘦')
      elif 18.5<=bmi<=24.9:
          print('正常')
      elif 25<=bmi<=29.9:
          print('偏胖')
          print('注意饮食,已经超重啦!')
      elif 30<=bmi<=34.9:
          print('肥胖')
      elif 35<=bmi<=39.9:
          print('重度肥胖')
      else:
          print('极重度肥胖')
      return bmi, item
   elif item=='asia':
       if bmi<18.5:
           print('偏瘦')
       elif 18.5<=bmi<=22.9:
           print('正常')
       elif 23<=bmi<=24.9:
           print('偏胖')
           print('已经超重啦')
       elif 25<=bmi<=29.9:
           print('肥胖')
       else:
           print('重度肥胖')
       return bmi,item
   elif item=='china':
       if bmi <18.5:
           print('偏瘦')
       elif 18.5<=bmi<=23.9:
           print('正常')

       elif 24<=bmi<=26.9:
           print('偏胖')
       elif 27<=bmi<=29.9:
           print('肥胖')
       else:
           print('重度肥胖')
       return bmi, item
   else:
       print('标准输入错误,请重新输入!')
print(bmi_function(float(input('请输入郭晶晶的身高:')),(float(input('请输入郭晶晶的体重:'))),'who'))
print(bmi_function(float(input('请输入赵方亮的身高:')),(float(input('请输入赵方亮的体重:'))),'asia'))
print(bmi_function(float(input('请输入胥非的身高:')),(float(input('请输入胥非的体重:'))),'china'))
