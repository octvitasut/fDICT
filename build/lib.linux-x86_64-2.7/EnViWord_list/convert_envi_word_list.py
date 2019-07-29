import antonyms_srawler
import google_scrawler
import make_xlsx
import threading
import argparse
import time

TITLES_LIST = [".No", "Word", "Pronounce", "Word type",
               "Meaning", "Synonyms", "Antonyms", "Examples"]


def convert_title_to_dict_key(title):
    return title.replace(" ", "_").lower()


def format_dict_into_list_using_titles_list(_dict):
    _list = []
    for title in TITLES_LIST:
        _list.append(_dict[convert_title_to_dict_key(title)])
    return _list


def get_row_of_one_word(row_num, word):
    _as = antonyms_srawler.AntonymsScrawler(word)
    gs = google_scrawler.GoogleScrawler(word)
    row_entrys = {}
    _info = gs.get_info_of_word()
    print("_info: %s " % _info)
    row_entrys.update(_info)
    # row_entrys.update(gs.get_info_of_word())
    row_entrys.update(_as.get_antonyms_of_word())
    row_entrys.update({".no": str(row_num + 1)})
    return make_xlsx.XlsxRow(row_num,
                             format_dict_into_list_using_titles_list(row_entrys))


def thread_function(words_list, list_start_offset, word_row_list):
    for index, word in enumerate(words_list):
        word_row = get_row_of_one_word(index + list_start_offset, word)
        word_row_list.append(word_row)
        # make_xlsx_obj.add_xlsx_row(word_row)


def convert(input_file_path, output_file_path, delimiter, thread_number=1):
    mx = make_xlsx.MakeXlsx(output_file_path, TITLES_LIST, exist_header=True)
    mx.make_column_titles()
    with open(input_file_path, 'r') as f:
        input = f.read()
    input = input.replace("\n", "").replace(" ", "")
    words_list = input.split(delimiter)
    list_offset = len(words_list) / thread_number
    word_row_list = []
    thread_list = []
    for i in range(thread_number):
        word_row_list.append([])
        list_start_offset = i*list_offset
        if i == thread_number - 1:
            x = threading.Thread(target=thread_function,
                                 args=(words_list[list_start_offset::],
                                       list_start_offset,
                                       word_row_list[i]))
            thread_list.append(x)
            x.start()
        else:
            x = threading.Thread(target=thread_function,
                                 args=(words_list[list_start_offset:list_start_offset + list_offset:],
                                       list_start_offset,
                                       word_row_list[i]))
            thread_list.append(x)
            x.start()
    for _thread in thread_list:
        _thread.join()

    total_word_row_list = []
    for i in word_row_list:
        total_word_row_list.extend(i)
    for word_row in total_word_row_list:
        mx.add_xlsx_row(word_row)
    mx.finish_xlsx()
    print("Convert progress complete!")


def main():
    parser = argparse.ArgumentParser()

    # defining arguments for parser object

    parser.add_argument("input_file_path", type=str,
                        help="Path of file which contains words list need tranlate.")

    parser.add_argument("output_file_path", type=str,
                        help="Path of file which will be generated as result of program.")

    parser.add_argument("-d", "--delimiter", type=str, nargs=1,
                        metavar="delimiter_character", default="|",
                        help="Delimiter between each word in input file.")

    parser.add_argument("-t", "--thread", type=int, nargs=1,
                       metavar="number_of_threads", default="1",
                       help="Number of threads will be used to run program. This value must >= 1.")

    # parse the arguments from standard input
    args = parser.parse_args()

    if args.input_file_path == None:
        raise Exception("Argument input_file_path is mandatory!")

    if args.output_file_path == None:
        raise Exception("Argument input_file_path is mandatory!")

    if args.thread:
        if args.thread[0] < 1:
            raise Exception("Value of thread argument must be >= 1!")

    input_file_path = ''.join(args.input_file_path)
    output_file_path = ''.join(args.output_file_path)
    delimiter = args.delimiter[0]
    thread = args.thread[0]

    print("input_file_path: %s" % input_file_path)
    print("output_file_path: %s" % output_file_path)
    print("delimiter: %s" % delimiter)
    print("thread: %s" % thread)

    start_time = time.time()
    convert(input_file_path, output_file_path, delimiter, thread_number=thread)
    end_time = time.time()
    print("process_time: %s" % (end_time - start_time))


if __name__ == "__main__":
	main()