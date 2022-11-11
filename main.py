import sql
import imports
import check_install
parser = imports.argparse.ArgumentParser()
parser.add_argument('--install', '-i')
parser.add_argument('--view', '-v', action='store_true')
args=parser.parse_args()
print(args.install)









#To view the files
if args.view:
    print(sql.view())
#To check for program
if args.install is not None:
    check_install.chk(args.install)