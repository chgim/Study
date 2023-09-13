# from isp import EventParser, Event2Parser    # 의존이 강함


# def test():     
#     e = EventParser()
#     e.from_xml("test")

    
# def test2():
#     e = Event2Parser()
#     e.from_xml("test")

from isp import XMLEventParser


def test(e: XMLEventParser):    # 함수의 의존도 낮아짐, 함수의 활용도 높아짐
    e.from_xml("test")