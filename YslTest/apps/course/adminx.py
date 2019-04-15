#coding:utf-8
import xadmin
from xadmin import views
from course.models import *


# class GlobalSettings(object):
#     """此方法不会用"""
#     def get_site_menu(self):
#         return [
#             {
#                 'title':'课程信息',
#                 'perm':self.get_model_perm(Course,'view'),
#                 'icon':'',
#                 'menus':{
#                     {'title':'视频信息','url':self.get_model_url(Course,'videosource')},
#                     {'title':'章节信息','url':self.get_model_url(Course,'section')},
#                     {'title':'讲师信息','url':self.get_model_url(Course,'teacher')},
#                     {'title':'课程信息','url':self.get_model_url(Course,'course')},
#                 }
#             }
#         ]

class VideoSourceAdmin(object):
    list_display = ['name','create_time','update_time']
    search_fileds = ['name']
    list_filter = ['name']

class SectionAdmin(object):
    list_display = ['name','create_time','update_time','video']
    search_fileds = ['name','video']
    list_filter = ['name','video']

class TeacherAdmin(object):
    list_display = ['name','email','introduction', 'create_time', 'update_time']
    search_fileds = ['name','email','introduction']
    list_filter = ['name','email']

class CourseAdmin(object):
    list_display = ['name','time','type','level','introduction','studey_num','create_time','update_time','section','teacher']
    search_fileds = ['name','time','type','level']
    list_filter = ['name','time','type','level']


xadmin.site.register(Course,CourseAdmin)
xadmin.site.register(Section,SectionAdmin)
xadmin.site.register(VideoSource,VideoSourceAdmin)
xadmin.site.register(Teacher,TeacherAdmin)
# xadmin.site.register(views.CommAdminView,GlobalSettings)