import os
import sys
import shutil
from mako.template import Template
from mako.lookup import TemplateLookup


def main():
    if len(sys.argv) < 2:
        print "Usage: qsgen.py <outpath> [src]"
        sys.exit(-1)

    out_path = sys.argv[1]
    src_path = '.'
    if len(sys.argv) == 3:
        src_path = sys.argv[2]

    out_path = os.path.abspath(out_path)
    src_path = os.path.abspath(src_path)
    os.chdir(src_path)


    mlook = TemplateLookup(directories = ['.'])

    for root, dirs, files in os.walk('.'):
        for file in files:

            # Skip some common file extensions which shouldn't be copied

            if file[0] == '_':
                continue
            if file[-1] == '~':
                continue


            try:
                os.makedirs(os.path.join(out_path, root))
            except:
                pass
            file = os.path.join(root, file)
            print file,
            if file[-4:] != 'html':
                shutil.copyfile(file, os.path.join(out_path, file))
                print '[copy] ->', os.path.join(out_path, file)
                continue

            templ = mlook.get_template(file)
            f = open( os.path.join(out_path, file), 'w')
            print >> f, templ.render_unicode().encode('UTF-8')
            f.close()
            print '[templ]'

main()
