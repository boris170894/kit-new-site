from .models import ThemesModel, SocialMediaLinksModel

def change_theme(request):
    theme = ThemesModel.objects.all().last()
    social_media_links = SocialMediaLinksModel.objects.all().last()

    return {
        'theme_gray': theme,
        'social_media_links': social_media_links
    }

