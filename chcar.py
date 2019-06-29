#!/usr/bin/python  
# coding=utf-8  
#本段代码实现树莓派智能小车的超声红外避障效果
#代码使用的树莓派GPIO是用的BOARD编码方式。 
import RPi.GPIO as GPIO  
import time  
import sys

TRIG = 35 
ECHO = 36
#设置in引脚
pin1 = 11
pin2 = 12
pin3 = 15
pin4 = 16

#设置成BOARD编码
GPIO.setmode(GPIO.BOARD)

#忽略警告
GPIO.setwarnings(False)

#将in引脚设置为输出
GPIO.setup(pin1, GPIO.OUT)
GPIO.setup(pin2, GPIO.OUT)
GPIO.setup(pin3, GPIO.OUT)
GPIO.setup(pin4, GPIO.OUT)

#设置红外线引脚
GPIO.setup(37,GPIO.IN)
GPIO.setup(38,GPIO.IN)

#设置初始化PWM实例，频率为50
pwm1 = GPIO.PWM(pin1, 50)
pwm2 = GPIO.PWM(pin2, 50)
pwm3 = GPIO.PWM(pin3, 50)
pwm4 = GPIO.PWM(pin4, 50)

#开始脉宽调制
pwm1.start(0)
pwm2.start(0)
pwm3.start(0)
pwm4.start(0)

#设置超声波输入和输出
def setup():
	GPIO.setup(TRIG, GPIO.OUT)
	GPIO.setup(ECHO, GPIO.IN)

def distance():
	GPIO.output(TRIG, 0)
	time.sleep(0.000002)

	GPIO.output(TRIG, 1)
	time.sleep(0.00001)
	GPIO.output(TRIG, 0)

	
	while GPIO.input(ECHO) == 0:
		a = 0
	time1 = time.time()
	while GPIO.input(ECHO) == 1:
		a = 1
	time2 = time.time()

	during = time2 - time1
	dw = during * 340 / 2 * 100
        return dw

#停止时释放引脚
def destroy():
        pwm1.stop
        pwm2.stop
        pwm3.stop
        pwm4.stop
	GPIO.cleanup()
	
#通过占空比调制速度
def t_stop():
	pwm1.ChangeDutyCycle(0)
	pwm2.ChangeDutyCycle(0)
	pwm3.ChangeDutyCycle(0)
	pwm4.ChangeDutyCycle(0)

def t_up():
	pwm1.ChangeDutyCycle(35)
        pwm2.ChangeDutyCycle(0)
        pwm3.ChangeDutyCycle(35)
        pwm4.ChangeDutyCycle(0)
def t_down():
	pwm1.ChangeDutyCycle(0)
	pwm2.ChangeDutyCycle(0)
	pwm3.ChangeDutyCycle(0)
	pwm4.ChangeDutyCycle(35)

def t_left():
	pwm1.ChangeDutyCycle(35)
	pwm2.ChangeDutyCycle(0)
	pwm3.ChangeDutyCycle(0)
	pwm4.ChangeDutyCycle(35)

def t_right():
	pwm1.ChangeDutyCycle(0)
	pwm2.ChangeDutyCycle(35)
	pwm3.ChangeDutyCycle(35)
	pwm4.ChangeDutyCycle(0)



if __name__=="__main__":
        setup()
        while True:
                try:
                        dis = distance()
                        print(dis, 'cm')
                        print('')
                        time.sleep(0.3)
                
                        if dis < 40:
                                print("back")
                                time.sleep(0.1)
                                t_down()
                

                        elif  GPIO.input(37)==True and GPIO.input(38)==False:
                        #当右侧检测的信号均为低时（右侧遇到障碍物），小车左转直至信号产生变化
                                print ("Left")
                                #time.sleep(0.1)
                                t_left()
                        elif  GPIO.input(37)==False and GPIO.input(38)==True:
                        #当左侧检测的信号均为低时（左侧遇到障碍物），小车左转直至信号产生变化
                                print ("Right")
                                #time.sleep(0.1)
                                t_right()
                        elif GPIO.input(37)==True and GPIO.input(38)==True:
                        #当左右两侧检测的信号均为高时（前方无障碍物），小车前进直至信号产生变化
                                print ("go")
                                #time.sleep(0.1)
                                t_up()
                except KeyboardInterrupt:
                        destroy()


