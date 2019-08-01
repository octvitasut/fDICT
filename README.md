# EnViWord_list

## Introduce
Fdict is a translation scrawler program. Its input is a file which contains
english word, seperate wich each others using a specified symbol (E.x "," or
"|").
Fdict program will take some information (means, example. antonyms,...) 
about each English word and generate ouput as a xlsx file.

The following is content of an example input file used by fdict:
bird |love | human|interesting| nice| red 

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
E.x: we have an input file with path "/home/fdict/inputfile.txt" and want 
a result file with path "/root/outputfile.xlsx". Run following command in 
console:
```
envi-convert /home/fdict/inputfile.txt /root/outputfile.xlsx -d "|" -t 20
```
The above command run fdict with 20 threads and input file use "|" character
 as delimiter.
