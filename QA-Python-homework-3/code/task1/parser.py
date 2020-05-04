#!/usr/bin/python
import glob
import json
import os
import re
import sys


class InvalidNumberOfArgumentsException(Exception):
    pass


class EmptyDirectoryException(Exception):
    pass


class InvalidArgumentException(Exception):
    pass


class UnsupportedFileFormatException(Exception):
    pass


class Parser:

    def __init__(self):
        self.all_count = 0
        self.methods = {}
        self.biggest_request = []
        self.client_error = {}
        self.server_error = {}

    def write_txt_file(self, resname):
        with open(resname, 'w') as result:
            result.write("total count is {}\n".format(self.all_count))
            for i in self.methods.items():
                result.write("count of {} is {}\n".format(i[0], i[1]))
            result.write("top 10 largest queries: \n")
            for i in self.biggest_request:
                result.write("{} {}\n".format(i[0], i[1]))

            for i in sorted(self.client_error.items(), key=lambda kv: kv[1], reverse=True)[:10]:
                result.write("{} is repeated {}\n".format(i[0], i[1]))

            for i in sorted(self.server_error.items(), key=lambda kv: kv[1], reverse=True)[:10]:
                result.write("{} is repeated {}\n".format(i[0], i[1]))

    def write_json_file(self, resname):
        data = {}
        data['total_count'] = self.all_count
        data['methods_count'] = {}
        for i in self.methods.items():
            data.get('methods_count').update({i[0]: i[1]})
        data['largest_requests'] = {}
        for i in self.biggest_request:
            data.get('largest_requests').update({i[1]: i[0]})
        data['client_errors'] = {}
        for i in sorted(self.client_error.items(), key=lambda kv: kv[1], reverse=True)[:10]:
            data.get('client_errors').update({i[0]: i[1]})
        data['redirects'] = {}
        for i in sorted(self.server_error.items(), key=lambda kv: kv[1], reverse=True)[:10]:
            data.get('redirects').update({i[0]: i[1]})
        with open(resname, 'w') as result:
            json.dump(data, result)

    def analyze_file(self, fname, resname):
        self.all_count = 0
        self.methods = {}
        self.biggest_request = []
        self.client_error = {}
        self.server_error = {}

        with open(fname, 'r') as f:
            for line in f:
                self.all_count += 1
                split_line = re.split(' "|" | ', line)
                if self.methods.get(split_line[5]) is not None:
                    self.methods[split_line[5]] = self.methods.pop(split_line[5]) + 1
                else:
                    self.methods[split_line[5]] = 0

                if len(self.biggest_request) < 10:
                    self.biggest_request.append([int(split_line[9]),
                                                 "{} {} {} {} {}".format(split_line[5], split_line[6],
                                                                         split_line[0], split_line[3],
                                                                         split_line[4])])
                elif int(split_line[9]) >= self.biggest_request[0][0]:
                    self.biggest_request.append(
                        [int(split_line[9]),
                         "{} {} {} {} {}".format(split_line[5], split_line[6],
                                                 split_line[0], split_line[3], split_line[4])])
                self.biggest_request.sort(key=lambda req: req[0], reverse=True)
                if len(self.biggest_request) > 10:
                    self.biggest_request.pop(10)

                if split_line[8][0] == '4':
                    req = "{}:{}".format(split_line[6], split_line[8])
                    if self.client_error.get(req) is not None:
                        self.client_error[req] = self.client_error.pop(req) + 1
                    else:
                        self.client_error[req] = 0

                if split_line[8][0] == '3':
                    req = "{}:{}".format(split_line[6], split_line[8])
                    if self.server_error.get(req) is not None:
                        self.server_error[req] = self.server_error.pop(req) + 1
                    else:
                        self.server_error[req] = 0
            if os.path.splitext(resname)[1] == ".txt":
                self.write_txt_file(resname)
            elif os.path.splitext(resname)[1] == ".json":
                self.write_json_file(resname)
            elif resname == "db":
                return self.biggest_request, self.client_error, self.server_error
            else:
                raise UnsupportedFileFormatException


if __name__ == '__main__':
    parser = Parser()
    if len(sys.argv) != 3:
        raise InvalidNumberOfArgumentsException
    if os.path.isdir(sys.argv[1]):
        log_files = glob.glob((os.path.join(sys.argv[1], '*.log')))
        if len(log_files) == 0:
            raise EmptyDirectoryException
        for file in log_files:
            parser.analyze_file(file, sys.argv[2])
    elif os.path.isfile(sys.argv[1]):
        parser.analyze_file(sys.argv[1], sys.argv[2])
    else:
        raise InvalidArgumentException
