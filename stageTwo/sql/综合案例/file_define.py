"""
和文件相关的定义
"""
import json

from data_define import Record


class FileReader:

    def read_data(self):
        """读取文件的数据，读到的每一条数据都转换为Record对象，将它们都封装到list内返回即可"""
        pass


class TextFileReader(FileReader):

    def __init__(self, path):
        self.path = path

    def read_data(self) -> list[Record]:
        f = open(self.path, "r", encoding="UTF-8")

        record_list: list[Record] = []
        for line in f.readlines():
            line = line.strip()
            data_list = line.split(",")
            record = Record(data_list[0], data_list[1], int(data_list[2]), data_list[3])
            record_list.append(record)

        f.close()
        return record_list


class JsonFileReader(FileReader):
    def __init__(self, path):
        self.path = path

    def read_data(self) -> list[Record]:
        f = open(self.path, "r", encoding="UTF-8")

        record_list: list[Record] = []
        for line in f.readlines():
            data_dict = json.loads(line)
            record = Record(data_dict["date"], data_dict["order_id"], int(data_dict["money"]), data_dict["province"])
            record_list.append(record)

        f.close()
        return record_list


if __name__ == '__main__':
    cvs_file_reader = TextFileReader(r"C:\Users\CaseyL\Desktop\pylearn\stageTwo\数据分析案例\2011年1月销售数据.cvs")
    json_file_reader = JsonFileReader(r"C:\Users\CaseyL\Desktop\pylearn\stageTwo\数据分析案例\2011年2月销售数据.json")
    c1 = cvs_file_reader.read_data()
    c2 = json_file_reader.read_data()
    for cc in c1:
        print(cc)

    print("\n")
    for cc in c2:
        print(cc)


