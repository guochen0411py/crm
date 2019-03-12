#!/usr/bin/env python
# -*- coding:utf-8 -*-
from stark.service.v1 import site
from crm import models

from crm.views.school import SchoolHandler
from crm.views.depart import DepartmentHandler
from crm.views.userinfo import UserInfoHandler
from crm.views.course import CourseHandler
from crm.views.class_list import ClassListHandler
from crm.views.public_customer import PublicCustomerHandler
from crm.views.private_customer import PrivateCustomerHandler
from crm.views.consult_record import ConsultRecordHandler
from crm.views.payment_record import PaymentRecordHandler
from crm.views.check_payment_record import CheckPaymentRecordHandler
from crm.views.student import StudentHandler
from crm.views.score_record import ScoreHandler
from crm.views.course_record import CourseRecordHandler
from crm.views.homework import HomeWorkHandler
from crm.views.homework_record import HomeworkRecordHandler

site.register(models.School, SchoolHandler)
site.register(models.Department, DepartmentHandler)
site.register(models.UserInfo, UserInfoHandler)
site.register(models.Course, CourseHandler)
site.register(models.ClassList, ClassListHandler)

site.register(models.Customer, PublicCustomerHandler, 'pub')
site.register(models.Customer, PrivateCustomerHandler, 'priv')

site.register(models.ConsultRecord, ConsultRecordHandler)
site.register(models.PaymentRecord, PaymentRecordHandler)
site.register(models.PaymentRecord, CheckPaymentRecordHandler, 'check')
site.register(models.Student, StudentHandler)
site.register(models.ScoreRecord, ScoreHandler)
site.register(models.CourseRecord, CourseRecordHandler)
site.register(models.HomeWork, HomeWorkHandler)
site.register(models.HomeWorkRecord, HomeworkRecordHandler)
