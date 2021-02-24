#                                                                                                                                                                                            
#                                                                                                                                                                                            
#  NNNNNNNN        NNNNNNNN     OOOOOOOOO     DDDDDDDDDDDDD      EEEEEEEEEEEEEEEEEEEEEEPPPPPPPPPPPPPPPPP        AAA         TTTTTTTTTTTTTTTTTTTTTTTHHHHHHHHH     HHHHHHHHH   SSSSSSSSSSSSSSS 
#  N:::::::N       N::::::N   OO:::::::::OO   D::::::::::::DDD   E::::::::::::::::::::EP::::::::::::::::P      A:::A        T:::::::::::::::::::::TH:::::::H     H:::::::H SS:::::::::::::::S
#  N::::::::N      N::::::N OO:::::::::::::OO D:::::::::::::::DD E::::::::::::::::::::EP::::::PPPPPP:::::P    A:::::A       T:::::::::::::::::::::TH:::::::H     H:::::::HS:::::SSSSSS::::::S
#  N:::::::::N     N::::::NO:::::::OOO:::::::ODDD:::::DDDDD:::::DEE::::::EEEEEEEEE::::EPP:::::P     P:::::P  A:::::::A      T:::::TT:::::::TT:::::THH::::::H     H::::::HHS:::::S     SSSSSSS
#  N::::::::::N    N::::::NO::::::O   O::::::O  D:::::D    D:::::D E:::::E       EEEEEE  P::::P     P:::::P A:::::::::A     TTTTTT  T:::::T  TTTTTT  H:::::H     H:::::H  S:::::S            
#  N:::::::::::N   N::::::NO:::::O     O:::::O  D:::::D     D:::::DE:::::E               P::::P     P:::::PA:::::A:::::A            T:::::T          H:::::H     H:::::H  S:::::S            
#  N:::::::N::::N  N::::::NO:::::O     O:::::O  D:::::D     D:::::DE::::::EEEEEEEEEE     P::::PPPPPP:::::PA:::::A A:::::A           T:::::T          H::::::HHHHH::::::H   S::::SSSS         
#  N::::::N N::::N N::::::NO:::::O     O:::::O  D:::::D     D:::::DE:::::::::::::::E     P:::::::::::::PPA:::::A   A:::::A          T:::::T          H:::::::::::::::::H    SS::::::SSSSS    
#  N::::::N  N::::N:::::::NO:::::O     O:::::O  D:::::D     D:::::DE:::::::::::::::E     P::::PPPPPPPPP A:::::A     A:::::A         T:::::T          H:::::::::::::::::H      SSS::::::::SS  
#  N::::::N   N:::::::::::NO:::::O     O:::::O  D:::::D     D:::::DE::::::EEEEEEEEEE     P::::P        A:::::AAAAAAAAA:::::A        T:::::T          H::::::HHHHH::::::H         SSSSSS::::S 
#  N::::::N    N::::::::::NO:::::O     O:::::O  D:::::D     D:::::DE:::::E               P::::P       A:::::::::::::::::::::A       T:::::T          H:::::H     H:::::H              S:::::S
#  N::::::N     N:::::::::NO::::::O   O::::::O  D:::::D    D:::::D E:::::E       EEEEEE  P::::P      A:::::AAAAAAAAAAAAA:::::A      T:::::T          H:::::H     H:::::H              S:::::S
#  N::::::N      N::::::::NO:::::::OOO:::::::ODDD:::::DDDDD:::::DEE::::::EEEEEEEE:::::EPP::::::PP   A:::::A             A:::::A   TT:::::::TT      HH::::::H     H::::::HHSSSSSSS     S:::::S
#  N::::::N       N:::::::N OO:::::::::::::OO D:::::::::::::::DD E::::::::::::::::::::EP::::::::P  A:::::A               A:::::A  T:::::::::T      H:::::::H     H:::::::HS::::::SSSSSS:::::S
#  N::::::N        N::::::N   OO:::::::::OO   D::::::::::::DDD   E::::::::::::::::::::EP::::::::P A:::::A                 A:::::A T:::::::::T      H:::::::H     H:::::::HS:::::::::::::::SS 
#  NNNNNNNN         NNNNNNN     OOOOOOOOO     DDDDDDDDDDDDD      EEEEEEEEEEEEEEEEEEEEEEPPPPPPPPPPAAAAAAA                   AAAAAAATTTTTTTTTTT      HHHHHHHHH     HHHHHHHHH SSSSSSSSSSSSSSS   
#                                                                                                                                                                                            
#                                                                                                                                                                                            
#                                                                                                                                                                                            
#                                                                                                                                                                                            
#                                                                                                                                                                                            
#                                                                                                                                                                                            
#
from panda3d.core import *
from direct.showbase.ShowBase import ShowBase
a=ShowBase()
level2Camera=base.makeCamera(base.win)
strawmodel=loader.loadModel("StrawberryDonut.egg")
level2Camera.node().setScene(strawmodel)
base.cam.node().setActive(False)
level2Camera.node().setActive(True)
a.run()

