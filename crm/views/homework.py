from stark.service.v1 import StarkHandler, StarkModelForm, get_datetime_text
from .base import PermissionHandler
from django.conf.urls import url
from crm import models
from stark.forms.widgets import DateTimePickerInput
from django.utils.safestring import mark_safe
from django.shortcuts import HttpResponse, render
from django.urls import reverse


class HomeWorkModelForm(StarkModelForm):
    class Meta:
        model = models.HomeWork
        fields = ['title', 'hand_in_date', "content"]
        widgets = {
            "hand_in_date": DateTimePickerInput
        }


class HomeWorkHandler(PermissionHandler, StarkHandler):

    def display_content(self, obj=None, is_header=None, *args, **kwargs):
        if is_header:
            return '详情'
        record_url = reverse('stark:crm_homework_content', kwargs={'homework_id': obj.pk})
        return mark_safe('<a target="_blank" href="%s">详情</a>' % record_url)

    def display_record(self, obj=None, is_header=None, *args, **kwargs):
        if is_header:
            return '上交记录'
        record_url = reverse('stark:crm_homeworkrecord_list', kwargs={'homework_id': obj.pk})
        return mark_safe('<a href="%s">记录</a>' % record_url)

    list_display = ['title', "course_record", get_datetime_text("创建时间", "create_date"),
                    get_datetime_text("截止时间", "hand_in_date"), display_content,display_record]

    def get_urls(self):
        patterns = [
            url(r'^list/(?P<course_record_id>\d+)/$', self.wrapper(self.changelist_view), name=self.get_list_url_name),
            url(r'^add/(?P<course_record_id>\d+)/$', self.wrapper(self.add_view), name=self.get_add_url_name),
            url(r'^change/(?P<course_record_id>\d+)/(?P<pk>\d+)/$', self.wrapper(self.change_view),
                name=self.get_change_url_name),
            url(r'^delete/(?P<course_record_id>\d+)/(?P<pk>\d+)/$', self.wrapper(self.delete_view),
                name=self.get_delete_url_name),
            url(r'^content/(?P<homework_id>\d+)/$', self.wrapper(self.content_view),
                name=self.get_url_name('content')),

        ]
        patterns.extend(self.extra_urls())
        return patterns

    model_form_class = HomeWorkModelForm

    def save(self, request, form, is_update, *args, **kwargs):
        course_record_id = kwargs.get('course_record_id')
        if not is_update:
            form.instance.course_record_id = course_record_id
        form.save()

    def display_edit_del(self, obj=None, is_header=None, *args, **kwargs):
        if is_header:
            return '操作'
        course_record_id = kwargs.get('course_record_id')
        tpl = '<a href="%s">编辑</a> <a href="%s">删除</a>' % (
            self.reverse_change_url(pk=obj.pk, course_record_id=course_record_id),
            self.reverse_delete_url(pk=obj.pk, course_record_id=course_record_id))
        return mark_safe(tpl)

    def content_view(self, request, homework_id, *args, **kwargs):
        homework = models.HomeWork.objects.filter(pk=homework_id).first()
        return render(request, "homework_content.html", {"homework": homework})

    def get_queryset(self, request, *args, **kwargs):
        course_record_id = kwargs.get('course_record_id')
        return self.model_class.objects.filter(course_record_id=course_record_id)
