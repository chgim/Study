from isp import XMLEventParser


def analysis(parser: XMLEventParser):   # 구현체는 바뀔 수 있다. 개방 폐쇄의 원칙. 인터페이스만 바라봄
    parser.from_xml("t")


