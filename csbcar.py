#!/usr/bin/python  
# coding=utf-8  
#代码使用的树莓派GPIO是用的BOARD编码方式。 
import RPi.GPIO as GPIO  
import time  
import sys
#设置超声波引脚
TRIG = 35
ECHO = 36
TRIG1 = 31
ECHO1= 32
TRIG2 = 37
ECHO2 = 38

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
	GPIO.setup(TRIG1, GPIO.OUT)
	GPIO.setup(TRIG2, GPIO.OUT)
	GPIO.setup(ECHO, GPIO.IN)
	GPIO.setup(ECHO1, GPIO.IN)
	GPIO.setup(ECHO2, GPIO.IN)


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
def distance2():
        GPIO.output(TRIG1, 0)
        time.sleep(0.000002)
	
        GPIO.output(TRIG1, 1)
        time.sleep(0.00001)
        GPIO.output(TRIG1, 0)

	
        while GPIO.input(ECHO1) == 0:               
                b=0
        time3 = time.time()
        while GPIO.input(ECHO1) == 1:
                b = 1
        time4 = time.time()

        during2 = time4 - time3
        dw2 = during2 * 340 / 2 * 100
        return dw2

def distance3():
        GPIO.output(TRIG2, 0)
        time.sleep(0.000002)
                
        GPIO.output(TRIG2, 1)
        time.sleep(0.00001)
        GPIO.output(TRIG2, 0)

	
        while GPIO.input(ECHO2) == 0:               
                c=0
        time5 = time.time()
        while GPIO.input(ECHO2) == 1:
                c = 1
        time6 = time.time()

        during3 = time6 - time5
        dw3 = during3 * 340 / 2 * 100
        return dw3

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
        pwm1.ChangeDutyCycle(45)
        pwm2.ChangeDutyCycle(0)
        pwm3.ChangeDutyCycle(45)
        pwm4.ChangeDutyCycle(0)
def t_down():
	pwm1.ChangeDutyCycle(0)
	pwm2.ChangeDutyCycle(0)
	pwm3.ChangeDutyCycle(0)
	pwm4.ChangeDutyCycle(70)

def t_left():
	pwm1.ChangeDutyCycle(0)
	pwm2.ChangeDutyCycle(55)
	pwm3.ChangeDutyCycle(55)
	pwm4.ChangeDutyCycle(0)

def t_right():
	pwm1.ChangeDutyCycle(55)
	pwm2.ChangeDutyCycle(0)
	pwm3.ChangeDutyCycle(0)
	pwm4.ChangeDutyCycle(55)


if __name__=="__main__":
        setup()
        while True:
                try:
                        dis = distance()
                        #print dis, 'cm'
                        #print''
                        time.sleep(0.05)
                        dis2 = distance2()
                        #print dis2, 'cm'
                        #print''
                        time.sleep(0.05)
                        dis3 = distance3()
                        #print dis3, 'cm'
                        #print''
                        time.sleep(0.05)
    
                        if dis < 40:
                                print("back")
                                time.sleep(0.1)
                                t_down()
                        elif dis2 < 35:
                                print("right")
                                time.sleep(0.1)
                                t_right()
                        elif dis3 < 35:
                                print("left")
                                time.sleep(0.1)
                                t_left()
                
                        else:
                                t_up()
                                print("up")
              
                except KeyboardInterrupt:
                        destroy()
                        
  


