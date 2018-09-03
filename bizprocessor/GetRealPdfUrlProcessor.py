#!/usr/bin/env python
#coding: utf-8
'''
Created on Aug 30, 2018

@author: xingtong
'''
from baseprocessor.BaseProcessor import BaseProcessor
from ieeexplorespider.TestWebPageSpider import TestWebPageSpider
from bizprocessor.GetPdfUrlProcessor import GetPdfUrlProcessor

def getWebPageSipder(appConfig):
    mainPageUrl=appConfig.get('WebPageSpider','MAIN_PAGE_URL')
    cookiePath=appConfig.get('WebPageSpider','COOKIE_PATH')
    tempDocPath=appConfig.get('WebPageSpider','TEMP_DOC_PATH')
    return TestWebPageSpider(mainPageUrl,cookiePath,tempDocPath)

class GetRealPdfUrlProcessor(BaseProcessor):
    '''
    this class is used to get real pdf file's url
    '''

    def __init__(self,inputQueue=None,outputQueue=None):
        super(GetRealPdfUrlProcessor,self).__init__(inputQueue=inputQueue,outputQueue=outputQueue)
        self.webSpider=getWebPageSipder(self.appConfig)
            
    def process(self,processObj=None):
        if processObj:
            realPdfUrl=self.webSpider.getRealPdfUrl(processObj.pdfUrl)
#             print realPdfUrl
            processObj.realPdfUrl=realPdfUrl
        return processObj

if __name__ == '__main__':
    result=[{"_id":"5b839c9b7bbd7112ec94e5bf","issn":"0148-9267","start_page":"106","publication_number":6720219,"rank":16,"article_number":"6792690","title":"&#201;velyne Gayou, Editor: Polychrome Portraits 14: Pierre Schaeffer","abstract_url":"https://ieeexplore.ieee.org/xpl/articleDetails.jsp?arnumber=6792690","issue":"1","is_number":6790986,"index_terms":{},"publication_title":"Computer Music Journal","volume":"34","access_type":"LOCKED","content_type":"Journals","authors":{"authors":[{"author_order":1,"affiliation":"San Francisco, California, USA.","full_name":"Thom Blum"}]},"publication_date":"March 2010","fileId":"","publisher":"MIT Press","doi":"10.1162/comj.2010.34.1.106","pdf_url":"https://ieeexplore.ieee.org/stamp/stamp.jsp?arnumber=6792690","partnum":"6792690","end_page":"111","citing_paper_count":0}]
    processObj=GetPdfUrlProcessor()
    processObj.result=result[0]
    obj=GetPdfUrlProcessor()
    processObj=obj.process(processObj)
    realUrlObj=GetRealPdfUrlProcessor()
    processObj=realUrlObj.process(processObj)
    print processObj.realPdfUrl