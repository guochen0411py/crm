from stark.service.v1 import StarkHandler,get_choice_text,StarkModelForm
from .base import PermissionHandler
from django.conf.urls import url
from crm import models
from django.utils.safestring import mark_safe



class HomeworkRecordModelForm(StarkModelForm):

    class Meta:
        model = models.HomeWorkRecord
        fields = ["content","student"]



class HomeworkRecordHandler(PermissionHandler, StarkHandler):
    model_form_class = HomeworkRecordModelForm
    list_display = ["homework","score","student","teacher",get_choice_text("状态","status"),"content"]
    def get_urls(self):
        patterns = [
            url(r'^list/(?P<homework_id>\d+)/$', self.wrapper(self.changelist_view), name=self.get_list_url_name),
            url(r'^add/(?P<homework_id>\d+)/$', self.wrapper(self.add_view), name=self.get_add_url_name),
            url(r'^change/(?P<homework_id>\d+)/(?P<pk>\d+)/$', self.wrapper(self.change_view),
                name=self.get_change_url_name),
            url(r'^delete/(?P<homework_id>\d+)/(?P<pk>\d+)/$', self.wrapper(self.delete_view),
                name=self.get_delete_url_name),
        ]
        patterns.extend(self.extra_urls())
        return patterns
    def display_edit_del(self, obj=None, is_header=None, *args, **kwargs):
        if is_header:
            return '操作'
        homework_id = kwargs.get('homework_id')
        tpl = '<a href="%s">编辑</a> <a href="%s">删除</a>' % (
            self.reverse_change_url(pk=obj.pk, homework_id=homework_id),
            self.reverse_delete_url(pk=obj.pk, homework_id=homework_id))
        return mark_safe(tpl)

    def save(self, request, form, is_update, *args, **kwargs):
        homework_id = kwargs.get('homework_id')
        homework = models.HomeWork.objects.filter(pk=homework_id).first()
        course_obj = models.CourseRecord.objects.filter(class_object__course_id=homework_id).first()
        if not is_update:
            form.instance.homework = homework
            form.instance.stats = 1
            form.instance.teacher = course_obj.teacher
        form.save()
