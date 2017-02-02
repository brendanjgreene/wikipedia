# Scrapy settings for wikipedia project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#

BOT_NAME = 'wikipedia'

SPIDER_MODULES = ['wikipedia.spiders']
NEWSPIDER_MODULE = 'wikipedia.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'wikipedia (+http://www.yourdomain.com)'
