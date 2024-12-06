#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import rospy
from geometry_msgs.msg import Twist

def eskenarUcgenCizdirme():
    rospy.init_node('eşkenarÜçgenÇizme', anonymous=True)
    pub = rospy.Publisher('/cmd_vel', Twist, queue_size=20)
    hiz_msg = Twist()

    kenarUzunluk = 3.0
    hiz = 0.1  
    donusAcisi = 2 * 3.14159 / 3  #radyan cinsi
    donusHizi = 0.2 
    rospy.sleep(1) 
    rospy.loginfo("1. Kenar Çiziliyor")  
    hiz_msg.linear.x = hiz  #robotun düz hızını eşitledik
    hiz_msg.angular.z = 0.0 #robotun açısal hızını sıfırladık
    pub.publish(hiz_msg)
    rospy.sleep(kenarUzunluk / hiz)
    rospy.loginfo("1. Kenar Çizildi")
    hiz_msg.angular.z = 0.0
    hiz_msg.linear.x = 0.0  #robotu durdurduk
    pub.publish(hiz_msg)
    rospy.sleep(1)
    rospy.loginfo("1. Dönüş Yapiliyor")   
    hiz_msg.angular.z = donusHizi
    pub.publish(hiz_msg)
    rospy.sleep(donusAcisi / donusHizi)
    hiz_msg.angular.x = 0.0
    hiz_msg.angular.z = 0.0
    pub.publish(hiz_msg)
    rospy.sleep(1)
    rospy.loginfo("1. Dönüş Yapildi") 
    rospy.loginfo("2. Kenar Çiziliyor")
    hiz_msg.linear.x = hiz
    hiz_msg.angular.z = 0.0
    pub.publish(hiz_msg)
    rospy.sleep(kenarUzunluk / hiz)
    hiz_msg.angular.z = 0.0
    hiz_msg.linear.x = 0.0
    pub.publish(hiz_msg)
    rospy.sleep(1)
    rospy.loginfo("2. Kenar Çizildi")
    rospy.loginfo("2. Dönüş Yapiliyor")
    hiz_msg.angular.z = donusHizi
    pub.publish(hiz_msg)
    rospy.sleep(donusAcisi / donusHizi)
    hiz_msg.angular.x = 0.0
    hiz_msg.angular.z = 0.0
    pub.publish(hiz_msg)
    rospy.sleep(1)
    rospy.loginfo("2. Dönüş Yapildi")
    rospy.loginfo("3. Kenar Çiziliyor")
    hiz_msg.linear.x = hiz
    pub.publish(hiz_msg)
    rospy.sleep(kenarUzunluk / hiz)
    hiz_msg.linear.x = 0.0
    pub.publish(hiz_msg)
    rospy.sleep(1)
    rospy.loginfo("Eşkenar üçgen çizimi tamamlandi!")
    hiz_msg.linear.x = 0.0
    hiz_msg.angular.z = 0.0
    pub.publish(hiz_msg)

if __name__ == '__main__':
    try:
        eskenarUcgenCizdirme()
    except rospy.ROSInterruptException:
        pass
