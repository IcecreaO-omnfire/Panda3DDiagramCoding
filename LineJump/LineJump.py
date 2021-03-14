#                                                                                                                                                                                                                                           
#                                                                                                                                                                                                                                           
#  LLLLLLLLLLL             IIIIIIIIIINNNNNNNN        NNNNNNNNEEEEEEEEEEEEEEEEEEEEEE               JJJJJJJJJJJUUUUUUUU     UUUUUUUUMMMMMMMM               MMMMMMMMPPPPPPPPPPPPPPPPP   IIIIIIIIIINNNNNNNN        NNNNNNNN        GGGGGGGGGGGGG
#  L:::::::::L             I::::::::IN:::::::N       N::::::NE::::::::::::::::::::E               J:::::::::JU::::::U     U::::::UM:::::::M             M:::::::MP::::::::::::::::P  I::::::::IN:::::::N       N::::::N     GGG::::::::::::G
#  L:::::::::L             I::::::::IN::::::::N      N::::::NE::::::::::::::::::::E               J:::::::::JU::::::U     U::::::UM::::::::M           M::::::::MP::::::PPPPPP:::::P I::::::::IN::::::::N      N::::::N   GG:::::::::::::::G
#  LL:::::::LL             II::::::IIN:::::::::N     N::::::NEE::::::EEEEEEEEE::::E               JJ:::::::JJUU:::::U     U:::::UUM:::::::::M         M:::::::::MPP:::::P     P:::::PII::::::IIN:::::::::N     N::::::N  G:::::GGGGGGGG::::G
#    L:::::L                 I::::I  N::::::::::N    N::::::N  E:::::E       EEEEEE                 J:::::J   U:::::U     U:::::U M::::::::::M       M::::::::::M  P::::P     P:::::P  I::::I  N::::::::::N    N::::::N G:::::G       GGGGGG
#    L:::::L                 I::::I  N:::::::::::N   N::::::N  E:::::E                              J:::::J   U:::::D     D:::::U M:::::::::::M     M:::::::::::M  P::::P     P:::::P  I::::I  N:::::::::::N   N::::::NG:::::G              
#    L:::::L                 I::::I  N:::::::N::::N  N::::::N  E::::::EEEEEEEEEE                    J:::::J   U:::::D     D:::::U M:::::::M::::M   M::::M:::::::M  P::::PPPPPP:::::P   I::::I  N:::::::N::::N  N::::::NG:::::G              
#    L:::::L                 I::::I  N::::::N N::::N N::::::N  E:::::::::::::::E                    J:::::j   U:::::D     D:::::U M::::::M M::::M M::::M M::::::M  P:::::::::::::PP    I::::I  N::::::N N::::N N::::::NG:::::G    GGGGGGGGGG
#    L:::::L                 I::::I  N::::::N  N::::N:::::::N  E:::::::::::::::E                    J:::::J   U:::::D     D:::::U M::::::M  M::::M::::M  M::::::M  P::::PPPPPPPPP      I::::I  N::::::N  N::::N:::::::NG:::::G    G::::::::G
#    L:::::L                 I::::I  N::::::N   N:::::::::::N  E::::::EEEEEEEEEE        JJJJJJJ     J:::::J   U:::::D     D:::::U M::::::M   M:::::::M   M::::::M  P::::P              I::::I  N::::::N   N:::::::::::NG:::::G    GGGGG::::G
#    L:::::L                 I::::I  N::::::N    N::::::::::N  E:::::E                  J:::::J     J:::::J   U:::::D     D:::::U M::::::M    M:::::M    M::::::M  P::::P              I::::I  N::::::N    N::::::::::NG:::::G        G::::G
#    L:::::L         LLLLLL  I::::I  N::::::N     N:::::::::N  E:::::E       EEEEEE     J::::::J   J::::::J   U::::::U   U::::::U M::::::M     MMMMM     M::::::M  P::::P              I::::I  N::::::N     N:::::::::N G:::::G       G::::G
#  LL:::::::LLLLLLLLL:::::LII::::::IIN::::::N      N::::::::NEE::::::EEEEEEEE:::::E     J:::::::JJJ:::::::J   U:::::::UUU:::::::U M::::::M               M::::::MPP::::::PP          II::::::IIN::::::N      N::::::::N  G:::::GGGGGGGG::::G
#  L::::::::::::::::::::::LI::::::::IN::::::N       N:::::::NE::::::::::::::::::::E      JJ:::::::::::::JJ     UU:::::::::::::UU  M::::::M               M::::::MP::::::::P          I::::::::IN::::::N       N:::::::N   GG:::::::::::::::G
#  L::::::::::::::::::::::LI::::::::IN::::::N        N::::::NE::::::::::::::::::::E        JJ:::::::::JJ         UU:::::::::UU    M::::::M               M::::::MP::::::::P          I::::::::IN::::::N        N::::::N     GGG::::::GGG:::G
#  LLLLLLLLLLLLLLLLLLLLLLLLIIIIIIIIIINNNNNNNN         NNNNNNNEEEEEEEEEEEEEEEEEEEEEE          JJJJJJJJJ             UUUUUUUUU      MMMMMMMM               MMMMMMMMPPPPPPPPPP          IIIIIIIIIINNNNNNNN         NNNNNNN        GGGGGG   GGGG
#                                                                                                                                                                                                                                           
#                                                                                                                                                                                                                                           
#                                                                                                                                                                                                                                           
#                                                                                                                                                                                                                                           
#                                                                                                                                                                                                                                           
#                                                                                                                                                                                                                                           
#                                                                                                                                                                                       
from direct.showbase.ShowBase import ShowBase
from panda3d.core import *
import re
import io
def inputfile(task):
    textfile=open("LineJump.py")
    fileread=textfile.read()
    textiofile=io.StringIO(fileread)
    searchtext(textfile,textiofile)
    return task.done


def searchtext(openfile,contentsearch):
    searchindex=input("Line Number #: ")
    refind=re.search(searchindex,contentsearch.getvalue())
    textfound=refind.start()
    openfile.seek(textfound)
    text=openfile.read()
    exec(text,globals())
    
#2
print("Before beginning the program")  
startprogram=ShowBase()
taskMgr.add(inputfile,"Line Jumping Beginning")
startprogram.run()
#3
print("After starting the program")
    
