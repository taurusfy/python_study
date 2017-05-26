#coding=utf-8
 
input_ok = True
while input_ok:
    try:
        your_hight=float(raw_input("enter your hight(单位：米): "))
        your_weight=float(raw_input("enter your weight(单位：公斤): "))
    except EOFError, e:  # 将错误原因放在对象e中 
        print "input is wrong!"
    except IOError, e:
        print "input is wrong!"
    except ValueError, e:  # 数值错误异常处理
        print "input is wrong!"
    else:   # 如果没有异常，则执行
        if type(your_hight) != type(0.0) or type(your_weight)!=type(0.0):
            print u"请输入数值类型！"
        elif your_hight <=0 or your_hight > 2.50:
            print "身高值异常"
        elif your_weight<=0 or your_weight > 200 :
            print "体重值异常"
        else:
            input_ok=False
    finally:
        print " "
    
#print your_hight,your_weight

BMI=your_weight/(your_hight*your_hight)

print u"您的  BMI=%.2f" % BMI

if BMI<18.5:
    print u"您的体重偏轻"
elif BMI >=18.5  and BMI < 24:
    print u"您的体重正常"
elif BMI >= 24:
    print u"您的体重超重"
    
    