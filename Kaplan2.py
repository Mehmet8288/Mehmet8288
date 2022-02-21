#!/usr/bin/env piton
 işletim sistemini içe aktar
ithalat  sistemi

if  __name__  ==  '__main__' :
    os . çevre . setdefault ( 'DJANGO_SETTINGS_MODULE' , 'PaycellWebClientApplication.settings' )
    dene :
         Django'dan . _ çekirdek . yönetim  içe aktarma  yürütme_from_command_line
     Exc olarak ImportError  hariç : 
        ImportError'ı  yükselt (
            "Django içe aktarılamadı. Kurulduğundan emin misiniz ve"
            "PYTHONPATH ortam değişkeninizde mevcut mu? Yaptınız mı?"
            "sanal bir ortamı etkinleştirmeyi unuttunuz mu?"
        ) exc'den _ 
    execute_from_command_line ( sys.argv ) _ _
