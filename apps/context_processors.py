from django.conf import settings

def cfg_assets_root(request):

    return { 'ASSETS_ROOT' : settings.ASSETS_ROOT }

def flipkart(request):
    return {'FLIPKART_DIR' : settings.FLIPKART_DIR}
