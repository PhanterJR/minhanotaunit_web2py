# -*- coding: utf-8 -*-
from plugin_phantermobileconstructor.phanterandroid import PhanterAndroid
from plugin_phantermobileconstructor.phanterajaxdevelopment import PhanterAjaxDevelopment

phanterandroid = PhanterAndroid(default_controller='www', advanced_filter=True)
phanteajaxdevelopment = PhanterAjaxDevelopment()
response.ajax_server = phanteajaxdevelopment.urlAjaxServer(
    "%s/%s" % (request.env.http_host, request.application))
phanterandroid.ajaxServer(developer=response.ajax_server, production='http://conexaodidata.com.br/phantermobileconstructor/')