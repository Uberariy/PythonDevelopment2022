import pynames as pn
import readline
import shlex
import cmd

gens = pn.get_all_generators()
genstr = [str(i)[27:] for i in gens]
delang = "NATIVE"

class Repl(cmd.Cmd):
    prompt = "[Name]:~$ "

    def do_language(self, arg):
        args = shlex.split(arg, comments=True)
        if len(args) != 1:
            print("(Not enough/Too many) arguments")
        elif args[0].upper() in ["RU", "EN", "NATIVE"]:
            global delang 
            delang = args[0].upper()
        else:
            print("No such language supported")
            
    def complete_language(self, text, allcommand, beg, end):
        return [s for s in ["RU", "EN", "NATIVE"] if s.startswith(text)]        # Lang find

    def do_generate(self, arg):
        args = shlex.split(arg, comments=True)
        if len(args) < 1:
            print("Not enough arguments")
        else:
            find = -1; lang = 0; gend = 0;
            for ind, i in enumerate(genstr):
                if args[0] == i[:len(args[0])]:
                    if find < 0:
                        find = ind
                    if (len(args) == 1):
                        break
                    elif args[1] == i[len(args[0])+1:len(args[0])+len(args[1])+1]:
                        find = ind
                        break
            if find >= 0:
                for i in args[1:]:
                    if i.upper() in ["RU", "EN", "NATIVE"]:
                        lang = eval("pn.LANGUAGE."+i.upper())
                    if i.upper() in ["MALE", "FEMALE", "ALL", "MF"]:
                        gend = eval("pn.GENDER."+i.upper())
                if not lang:
                    lang = eval("pn.LANGUAGE."+delang)
                if not gend:
                    gend = pn.GENDER.MALE
                try:
                    print(gens[ind]().get_name_simple(gend, lang))
                except Exception as E:
                    print(gens[ind]().get_name_simple(gend, pn.LANGUAGE.NATIVE))
            else:
                print("Wrong Command")
                   
    def complete_generate(self, text, allcommand, beg, end):
        return [s for s in ["elven", "iron_kingdoms", "korean", "mongolian", "orc", "russian", "scandinavian"] if s.startswith(text)] 

    def do_info(self, arg):
        args = shlex.split(arg, comments=True)
        if len(args) < 1:
            print("Not enough arguments")
        else:
            find = -1; lang = 0; gend = 0;
            for ind, i in enumerate(genstr):
                if args[0] == i[:len(args[0])]:
                    if find < 0:
                        find = ind
                    if (len(args) == 1):
                        break
                    elif args[1] == i[len(args[0])+1:len(args[0])+len(args[1])+1]:
                        find = ind
                        break
            if find >= 0:
                for i in args[1:]:
                    if i.upper() in ["LANGUAGE"]:
                        lang = 1
                        break
                    if i.upper() in ["MALE", "FEMALE", "ALL", "MF"]:
                        gend = eval("pn.GENDER."+i.upper())
                        break
                if gend:
                    print(gens[ind]().get_names_number(gend))
                elif lang:
                    print(*gens[ind]().languages)
                else:
                    print(gens[ind]().get_names_number())
            else:
                print("Wrong Command")

    def complete_info(self, text, allcommand, beg, end):
        return [s for s in ["male", "female", "all", "mf", "language", "elven", "iron_kingdoms", "korean", "mongolian", "orc", "russian", "scandinavian"] if s.startswith(text)] 

    def do_q(self, arg):
        print("Exiting!")
        return True


Repl().cmdloop()