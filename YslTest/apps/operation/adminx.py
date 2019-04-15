import xadmin
from operation.models import MyComments


class MyCommentsAdmin(object):

    list_display = ['user_name','course_name','comments','create_time','update_time']
    search_fileds = ['user_name','course_name']
    list_filter = ['user_name','course_name']

xadmin.site.register(MyComments,MyCommentsAdmin)