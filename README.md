# EnViWord_list
## Installation
* Download source code.
```
git clone https://github.com/fagolabs/fdict.git
```
* Change directory to source code directory.
```
cd fdict
```
* Install requirement packages.
```
sudo pip install -r requirement.txt
```
* Build program.
```
sudo python setup.py install
```

## Use Guild
### Command Line Interface
Using following command to show CLI information of program:
```
envi-convert -h
```
Results:
```
usage: envi-convert [-h] [-d delimiter_character] [-t number_of_threads]
                    input_file_path output_file_path

positional arguments:
  input_file_path       Path of file which contains words list need tranlate.
  output_file_path      Path of file which will be generated as result of
                        program.

optional arguments:
  -h, --help            show this help message and exit
  -d delimiter_character, --delimiter delimiter_character
                        Delimiter between each word in input file.
  -t number_of_threads, --thread number_of_threads
                        Number of threads will be used to run program. This
                        value must >= 1.
```
