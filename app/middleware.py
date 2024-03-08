from django.utils.translation import activate

class DefaultLanguageMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Проверяем, был ли уже установлен язык для текущего входа на сайт
        if not request.COOKIES.get('language_set_for_session'):
            # Если кука отсутствует, сбрасываем язык на казахский
            activate('kk')
            request.LANGUAGE_CODE = 'kk'

            response = self.get_response(request)
            # Устанавливаем куку
            response.set_cookie('language_set_for_session', 'true')
            return response

        response = self.get_response(request)
        return response
