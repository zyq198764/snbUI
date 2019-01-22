#!/usr/bin/env python
#coding=utf-8
#运行所有的测试用例
import os
import threading
import unittest
import time
from JLC_AutoTest.common.HTMLTestRunner_jpg import HTMLTestRunner
from JLC_AutoTest.common.run_server import RunServer
from JLC_AutoTest.common.settings import  log,MACACA_PORT,REPORT_PATH,CASE_PATH
from JLC_AutoTest.model.utils import send_mail,new_report


if __name__ == '__main__':


    discover = unittest.defaultTestLoader.discover(CASE_PATH, "snb*.py")#运行所有以snb开头的用例
    now = time.strftime("%Y-%m-%d %H_%M_%S")
    file_name = now + 'result.html'
    run = HTMLTestRunner(title='拾年宝 UI自动化测试报告',
                         description='用例执行情况',
                         stream=open(REPORT_PATH + '/' + file_name, 'wb'),
                         retry=1)

    run.run(discover)#运行测试用例
#     # 发送邮件
#     file_new=new_report(REPORT_PATH)
#     send_mail(file_new)

# import threading
# import time
#
# # #启动macaca服务
#
# def run(num):
#
#     cmd = 'macaca server -p 3456 --verbose'
#     os.system(cmd)
#     time.sleep(2)
#
# #执行用例，写入到报告里面
# def thread1(num):
#     discover = unittest.defaultTestLoader.discover(CASE_PATH, "snb*.py")  # 运行所有以snb开头的用例
#     now = time.strftime("%Y-%m-%d %H_%M_%S")
#     file_name = now + 'result.html'
#     run = HTMLTestRunner(title='拾年宝 UI自动化测试报告',
#                          description='用例执行情况',
#                          stream=open(REPORT_PATH + '/' + file_name, 'wb'),
#                          retry=1)
#
#     run.run(discover)#运行测试用例
#     #      发送邮件
#     #     file_new=new_report(REPORT_PATH)
#     #     send_mail(file_new)
#
#
#
# if __name__ == '__main__':
#     # LockB.acquire()
#     tq = threading.Thread(target=run, args=(1,))
#     tq.start()#启动线程1
#     # tw = threading.Thread(target=thread1, args=(2,))
#     # tw.start()#启动线程2
#
#     T_POOL = []
#     T_POOL.append(tq)
#     # T_POOL.append(tw)
#     for t in T_POOL:
#         t.join()
#     print('主线程结束')
#     # for i in range(2):
#     #     t = threading.Thread(target=thread, args=(i,))
#     #     t.start()
#     #     T_POOL.append(t)
#
#     # tq.join()#join线程同步，主线程任务结束后，进入阻塞状态，一直等待其他的子线程执行结束之后，主线程再终止
#     # tw.join()
#     # for t in T_POOL:
#     #     t.join()

