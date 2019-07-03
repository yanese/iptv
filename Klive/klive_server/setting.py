# -*- coding: utf-8 -*-
# 주소  포트
BIND_ADDR = 'input_your_ip_or_url'
BIND_PORT = 9979

# 푹
POOQ_ID				= 'input_your_id'
POOQ_PW				= 'input_your_pw'
POOQ_QUALITY		= '5000'		# 5000 2000 1000 500

# 티빙
TVING_ID			= ''
TVING_PW			= ''
TVING_QUALITY		= 'stream40'	# stream50 stream40 stream30
TVING_LOGIN_TYPE	= 'CJONE'		# CJONE TVING

# 옥수수
OKSUSU_ID			= 'input_your_id'
OKSUSU_PW			= 'input_your_pw'
OKSUSU_QUALITY		= 'FHD'			# FHD HD SD

# 올레 모바일 TV
OLLEH_ID			= ''
OLLEH_PW			= ''
OLLEH_QUALITY		= '4000'		# 4000 2000 1000

# 커스텀
USE_CUSTOM			= True
USE_CUSTOM_SOURCE	= 'custom.txt'



## 수정 X #############################################################
USE_CUSTOM_SPLIT_CHAR	= ':'
USE_CUSTOM_REGEX		= '^(?P<channel_id>.*?)%s(?P<channel_number>.*?)%s(?P<channel_name>.*?)$' % (USE_CUSTOM_SPLIT_CHAR, USE_CUSTOM_SPLIT_CHAR)
USE_CUSTOM_M3U			= 'klive_custom.m3u'
USE_CUSTOM_EPG			= 'klive_custom.xml'

YANESE_CUSTOM_IPTV  = 'iptv.m3u'
YANESE_CUSTOM_XMLTV  = 'xmltv.xml'
CONTENTS_LIST		= 'KBS|MBC|SBS|POOQ|TVING|OKSUSU|OLLEH|VIDEOPORTAL|EVERYON|TVING_VOD|RADIO1'
FILENAME_M3U		= 'klive.m3u'
FILENAME_EPG 		= 'klive.xml'
