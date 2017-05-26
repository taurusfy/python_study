#coding=utf-8

#No.4
import random

#这种方法，每次领取红包的时候才会生成红包金额，不会产生预存空间
def redPacket_old(people, money):
    result = []
    remain = people
    max_money = money / people * 2
    #print "max_money=%d" % max_money
    for i in range(people):
        #print "i=%d"% i
        remain -= 1
        #print "remain=%d" % remain
        if remain > 0:
            #print "money - remain = %d" % (money - remain)
            m = random.randint(1, min(money - remain, max_money))
        else:
            m = money
        result.append(m)
        money -= m
    return result

#这种方法，在获取红包总额与个数的时候，就计算了每个随机红包的个数，虽然分配相对平均，但会造成预存空间
def redPacket_new(people, money):
    num = []
    sum_random = 0
    for i in range(0,people):
        a=random.uniform(0,1)
        num.append(a)
        sum_random += a
    m_sum=0
    m_list=[]
    for j in range(0,people):
        m=money*(num[j]/sum_random)
        m_int=round(m)
        m_list.append(m_int)
        m_sum+=m_int
    if m_sum != money:   #小数位数截断产生的误差分给最后一个红包
        m_list[len(m_list)-1] += money-m_sum  
    return m_list
  
if __name__ == "__main__":    
    input_ok = True
    while input_ok:
        try:
            people = int(raw_input("红包个数: ")) # 类型转换
            money = int(raw_input("总金额: ")) # 类型转换
        except EOFError, e:  # 将错误原因放在对象e中 
            print "input is wrong!"
        except IOError, e:
            print "input is wrong!"
        except ValueError, e:  # 数值错误异常处理
            print "input is wrong!"
        else:   # 如果没有异常，则执行
            if type(people) != type(0):
                print "Error! Are you sure it's an int?"
            elif people <=0:
                print "people can't be 0!"
            elif money<=0 or money > 200:
                print "money must between 0 to 200!"  #假设红包总金额不超过200
            else:
                input_ok=False
        finally:
            print " "
    money=money*100
    ret = redPacket_old(people, money)        
    #ret = redPacket_new(people, money)
    print "分配结果："
    temp_sum=0
    for k in range(0,people):
        temp_sum += ret[k]
        print ret[k]*0.01,
