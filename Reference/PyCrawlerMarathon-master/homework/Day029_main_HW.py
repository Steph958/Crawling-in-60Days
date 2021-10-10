import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

# 在 pipelines.py 裡的 open_spider 中改動這行
# self.runtime_file_path = str(self.dir_path / '{}.tmp.json.swp'.format(spider.board))
# 開啟暫存檔案時有不同檔名, 就可以根據不同看板寫入爬到的內容

def main():
    target_board = ['Tech_Job', 'Gossiping']
    #process = []
    #target_board = ['Gossiping']
    for board in target_board:
        process = CrawlerProcess(get_project_settings())
        process.crawl('PTTCrawler', board=board)
        print('\nCrawl {}..............\n'.format(board))
    process.start()

if __name__ == '__main__':
    main()
