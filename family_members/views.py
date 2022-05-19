from django.shortcuts import render
from family_members.models import Family
# Create your views here.

def index(request):
    return render(request, "family_members/index.html")

def index2(request):
    return render(request, "family_members/index.html")

def cursos(request):
    return render(request, "family_members/cursos.html")

def all_members(request):
    members = Family.objects.all()

    context_dict = {
        'members': members
    }

    return render(
        request=request,
        context=context_dict,
        template_name="family_members/show_all.html"
    )
    
def get_member(request, id):
    member = Family.objects.get(pk=id)

    context_dict = {
        'member': member,
    }

    return render(
        request=request,
        context=context_dict,
        template_name="family_members/get_member.html",
    )
    
#def post_course2(request, fist_name: str, code: int):
#    course = Course(name=name, code=code)
#    course.save() # save into the DB
#
#    context_dict = {
#        'course': course
#    }
#
#    return render(
#        request=request,
#        context=context_dict,
#        template_name="coder_course/post_course.html"
#    )


