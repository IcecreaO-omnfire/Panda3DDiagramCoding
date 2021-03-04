#                                                                                                                                                                       
#                                                                                                                                                                       
#  DDDDDDDDDDDDD      IIIIIIIIIIRRRRRRRRRRRRRRRRR   EEEEEEEEEEEEEEEEEEEEEE       CCCCCCCCCCCCCTTTTTTTTTTTTTTTTTTTTTTT       GGGGGGGGGGGGGUUUUUUUU     UUUUUUUUIIIIIIIIII
#  D::::::::::::DDD   I::::::::IR::::::::::::::::R  E::::::::::::::::::::E    CCC::::::::::::CT:::::::::::::::::::::T    GGG::::::::::::GU::::::U     U::::::UI::::::::I
#  D:::::::::::::::DD I::::::::IR::::::RRRRRR:::::R E::::::::::::::::::::E  CC:::::::::::::::CT:::::::::::::::::::::T  GG:::::::::::::::GU::::::U     U::::::UI::::::::I
#  DDD:::::DDDDD:::::DII::::::IIRR:::::R     R:::::REE::::::EEEEEEEEE::::E C:::::CCCCCCCC::::CT:::::TT:::::::TT:::::T G:::::GGGGGGGG::::GUU:::::U     U:::::UUII::::::II
#    D:::::D    D:::::D I::::I    R::::R     R:::::R  E:::::E       EEEEEEC:::::C       CCCCCCTTTTTT  T:::::T  TTTTTTG:::::G       GGGGGG U:::::U     U:::::U   I::::I  
#    D:::::D     D:::::DI::::I    R::::R     R:::::R  E:::::E            C:::::C                      T:::::T       G:::::G               U:::::D     D:::::U   I::::I  
#    D:::::D     D:::::DI::::I    R::::RRRRRR:::::R   E::::::EEEEEEEEEE  C:::::C                      T:::::T       G:::::G               U:::::D     D:::::U   I::::I  
#    D:::::D     D:::::DI::::I    R:::::::::::::RR    E:::::::::::::::E  C:::::C                      T:::::T       G:::::G    GGGGGGGGGG U:::::D     D:::::U   I::::I  
#    D:::::D     D:::::DI::::I    R::::RRRRRR:::::R   E:::::::::::::::E  C:::::C                      T:::::T       G:::::G    G::::::::G U:::::D     D:::::U   I::::I  
#    D:::::D     D:::::DI::::I    R::::R     R:::::R  E::::::EEEEEEEEEE  C:::::C                      T:::::T       G:::::G    GGGGG::::G U:::::D     D:::::U   I::::I  
#    D:::::D     D:::::DI::::I    R::::R     R:::::R  E:::::E            C:::::C                      T:::::T       G:::::G        G::::G U:::::D     D:::::U   I::::I  
#    D:::::D    D:::::D I::::I    R::::R     R:::::R  E:::::E       EEEEEEC:::::C       CCCCCC        T:::::T        G:::::G       G::::G U::::::U   U::::::U   I::::I  
#  DDD:::::DDDDD:::::DII::::::IIRR:::::R     R:::::REE::::::EEEEEEEE:::::E C:::::CCCCCCCC::::C      TT:::::::TT       G:::::GGGGGGGG::::G U:::::::UUU:::::::U II::::::II
#  D:::::::::::::::DD I::::::::IR::::::R     R:::::RE::::::::::::::::::::E  CC:::::::::::::::C      T:::::::::T        GG:::::::::::::::G  UU:::::::::::::UU  I::::::::I
#  D::::::::::::DDD   I::::::::IR::::::R     R:::::RE::::::::::::::::::::E    CCC::::::::::::C      T:::::::::T          GGG::::::GGG:::G    UU:::::::::UU    I::::::::I
#  DDDDDDDDDDDDD      IIIIIIIIIIRRRRRRRR     RRRRRRREEEEEEEEEEEEEEEEEEEEEE       CCCCCCCCCCCCC      TTTTTTTTTTT             GGGGGG   GGGG      UUUUUUUUU      IIIIIIIIII
#                                                                                                                                                                       
#                                                                                                                                                                       
#                                                                                                                                                                       
#                                                                                                                                                                       
#                                                                                                                                                                       
#                                                                                                                                                                       
#    
def go():
    print("Printer")
from panda3d.core import *
from direct.gui.DirectGui import *
from direct.showbase.ShowBase import ShowBase
b=ShowBase()
chalicemodel=loader.loadModel("ChaliceRot.egg")
rotatingchalice=DirectButton(text=("Rotating"),command=go,geom=chalicemodel)
b.run()
