from django.shortcuts import render, redirect


# 404 error
def tr_handler404(request, exception):
    return render(request, 'main/error.html', {
        'error_code': 404,
    }, status=404)

# 403 error
def tr_handler403(request, exception):
    return render(request, 'main/error.html', {
        'error_code': 403,
    }, status=403)

# 401 error
def tr_handler401(request, exception):
    return render(request, 'main/error.html', {
        'error_code': 401,
    }, status=401)

# 500 error
def tr_handler500(request):
    return render(request, 'main/error.html', {
        'error_code': 500,
    }, status=500)