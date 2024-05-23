from django.shortcuts import render
from .models import RectorsBlogMainInfoModel, RectorsBlogQuestionAnswerModel
from .forms import RectorsBlogQuestionAnswerForm
from django.core.paginator import Paginator


def greeting(request):
    rectors_blog = RectorsBlogMainInfoModel.objects.filter(is_public=True).last()

    return render(request,'rectors_blog/greeting.html', {
        'rectors_blog': rectors_blog
    })

def questions(request):
    rectors_blog = RectorsBlogMainInfoModel.objects.filter(is_public=True).last()
    questions = RectorsBlogQuestionAnswerModel.objects.filter(is_public=True)
    form = RectorsBlogQuestionAnswerForm()

    paginator = Paginator(questions, 10)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)

    return render(request,'rectors_blog/questions.html', {
        'page': page,
        'form': form,
        'rectors_blog': rectors_blog,
    })