from optparse import OptionParser, make_option

option_list = [
    make_option("-f", "--filename",
                action="store", type="string", dest="filename"),
    make_option("-q", "--quiet",
                action="store_true", dest="verbose"),
    make_option("-d", "--download",
                action="store_true", dest="down"),

    ]

parser = OptionParser(option_list=option_list)

(options, args) = parser.parse_args()

print options.verbose
print options.down
