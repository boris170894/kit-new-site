from django.http import JsonResponse
from ..forms import RectorsBlogQuestionAnswerForm
from rectors_blog.models import RectorsBlogQuestionAnswerModel
from django.utils import timezone

def question_create(request):
    if request.method == 'POST':
        last_message = RectorsBlogQuestionAnswerModel.objects.filter(is_public=True).last()
        current_time = timezone.now()

        time_difference = current_time - last_message.created
        time_difference_in_minutes = int(time_difference.total_seconds() / 60)

        if time_difference_in_minutes > 30:
            form = RectorsBlogQuestionAnswerForm(request.POST)

            if form.is_valid():
                form.save()
                return JsonResponse({
                    "status": "success",
                    "message": "Question created successfully"
                }, status=201)

            return JsonResponse({
                "status": "error",
                "message": "Error creating question"
            }, status=400)

        return JsonResponse({
            "status": "error",
            "message": "You can only submit a question once every half hour."
        }, status=400)

    return JsonResponse({
        "status": "error",
        "message": "Method not allowed"
    }, status=405)

