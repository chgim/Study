# ISP
# abc: Abstract Base Classes 추상 클래스

from abc import ABCMeta, abstractmethod


class XMLEventParser(metaclass=ABCMeta):    # 인터페이스, 추상 메서드
    @abstractmethod
    def from_xml(self, xml_data: str):
        """xml을 분석하는 함수"""    # 주석


class EventParser(XMLEventParser):  # 구현체
    def from_xml(self, xml_data: str):
        print(xml_data)


class Event2Parser(XMLEventParser):  # 구현체
    def from_xml(self, xml_data: str):
        print(xml_data + "-2")


class Event3Parser(XMLEventParser):  # 구현체
    def from_xml(self, xml_data: str):
        print(xml_data + "-3")

# e = EventParser()
# e.from_xml("test")

# x = XMLEventParser()    # TypeError: Can't instantiate abstract class XMLEventParser with abstract method from_xml
# x.from_xml("test") 