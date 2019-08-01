import xlsxwriter


class XlsxRow:
    def __init__(self, row_number, row_entrys):
        # row_number: is number of row (int)
        # row_entry: is a list contain value of all columns of this row (list)
        self.row_number = row_number
        self.row_entrys = row_entrys


class MakeXlsx:
    def __init__(self, output_file_path, column_titles, exist_header=False):
        # output_file_path: path of output file.xlsx (str)
        # column_titles: list of column titles (list)
        # exist_header: if xlsx has header row then this variable = True
        self.output_file_path = output_file_path
        self.column_titles = column_titles
        self.exist_header = exist_header
        self.workbook = xlsxwriter.Workbook(self.output_file_path)
        self.worksheet = self.workbook.add_worksheet()

    def make_column_titles(self):
        try:
            bold = self.workbook.add_format({'bold': True})
            header_row = 0
            col = 0
            for column_title in self.column_titles:
                self.worksheet.write(header_row, col, column_title, bold)
                col += 1
            return 0
        except Exception as e:
            return e

    def add_xlsx_row(self, row_obj):
        # row_obj is object of class XlsxRow
        try:
            if self.exist_header:
                row_obj.row_number += 1
            col = 0
            for row_entry in row_obj.row_entrys:
                self.worksheet.write(row_obj.row_number,
                                     col,
                                     row_entry)
                col += 1
            return 0
        except Exception as e:
            return e

    def finish_xlsx(self):
        try:
            self.workbook.close()
            return 0
        except Exception as e:
            return e

def main():
    output_file_path = '/home/dohuuhung1234/Desktop/test_xlsx.xlsx'
    column_titles = ['.No', 'Word', 'Type', 'Meanings']
    exist_header = True

    xlsx_obj = MakeXlsx(output_file_path, column_titles, exist_header=exist_header)
    make_title_result = xlsx_obj.make_column_titles()
    if make_title_result != 0:
        return make_title_result

    word1 = XlsxRow(0, ["0", "dog", "noun", "con cho"])
    word2 = XlsxRow(1, ["1", "cat", "noun", "con meo"])
    word3 = XlsxRow(2, ["2", "bird", "noun", "con chim"])

    words = [word1, word2, word3]
    for word in words:
        add_result = xlsx_obj.add_xlsx_row(word)
        if add_result != 0:
            return add_result
    end_result = xlsx_obj.finish_xlsx()
    if end_result != 0:
        return end_result
    return 0
