import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
import time

def main():
    target_board = ['PC_Shopping', 'e-shopping']
    #process = []
    #target_board = ['Gossiping']
    for board in target_board:
        process = CrawlerProcess(get_project_settings())
        process.crawl('PTTCrawler', board=board)
        print('\nCrawl {}..............\n'.format(board))
    process.start()

if __name__ == '__main__':
    main()
