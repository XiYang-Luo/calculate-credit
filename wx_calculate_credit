import wx
from openfile import Openfile
from countcontents import CountContents
Path=''
class MyFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self,None,-1,"学分统计",pos=(300,50),size=(800,700))
        self.panel=wx.Panel(self)
        
        self.text_name=wx.TextCtrl(self.panel,-1,pos=(10,10),size=(700,30))
        self.text_contents=wx.TextCtrl(self.panel,-1,pos=(10,50),size=(700,520),style=wx.TE_MULTILINE)
        self.text_update=wx.TextCtrl(self.panel,-1,pos=(10,580),size=(700,30),style=wx.TE_MULTILINE)
        
        self.statusbar = self.CreateStatusBar()
        #将状态栏分割为3个区域,比例为1:2:3
        self.statusbar.SetFieldsCount(3)
        self.statusbar.SetStatusWidths([-1, -2, -1])
        
        self.menubar=wx.MenuBar()
        self.menu1=wx.Menu()
        self.menu2=wx.Menu()
        self.menu3=wx.Menu()
        """STEP3在菜单下面，建立选项栏，使用Append（-1，“name”）"""
        self.m1open=self.menu1.Append(-1,"Open")
        #self.m1save=self.menu1.Append(-1,"Save")
        self.m2about=self.menu2.Append(-1,"About")
        #self.m3cds_amino=self.menu3.Append(-1,"Change Cds To Amino")
        #self.m3codon_bias=self.menu3.Append(-1,"Bar Of Codon Bias")
        """STEP4将建好的菜单添加到菜单栏下面去，使用Append(菜单，“name”)"""
        self.menubar.Append(self.menu1,"FILE")
        self.menubar.Append(self.menu2,"HELP")
        self.menubar.Append(self.menu3,"Other")
        """STEP5将菜单栏设置到主窗口中，使用SetMenuBar（）"""
        self.SetMenuBar(self.menubar)
        
        self.button_begin=wx.Button(self.panel,-1,"开始",pos=(720,10),size=(50,30))
        self.button_save=wx.Button(self.panel,-1,"保存",pos=(720,50),size=(50,30))
        
        """绑定"""
        self.menu1.Bind(wx.EVT_MENU,self.Onopen,self.m1open)
        #self.menu1.Bind(wx.EVT_MENU,self.Onsave_menu,self.m1save)
        self.button_begin.Bind(wx.EVT_BUTTON,self.Onbegin)
        self.button_save.Bind(wx.EVT_BUTTON,self.Onsave)
        
        """子窗口绑定"""
        self.menu2.Bind(wx.EVT_MENU,self.Onhelp,self.m2about)
        
        
    def Onhelp(self,event):
        """子窗口界面创建wx.Dialog，在self.panel下面"""
        self.dialog_main_help=wx.Dialog(self.panel,-1,title="Help",pos=(100,100),size=(600,500))
        """创建好之后，便是在，self.dialog_main_help下构建控件"""
        """图片构建
        image = wx.Image('C:\\Users\\luo xi yang\\Desktop\\临时\\ship.png',wx.BITMAP_TYPE_PNG)
        temp = image.ConvertToBitmap()
        size = self.help_list.GetMinWidth(),self.help_list.GetMinHeight()
        wx.StaticBitmap(self.help_list,bitmap=temp)
        """
        #self.help_list=wx.ListBox(self.dialog_main_help,-1,pos=(50,30),size=(700,500))
        listDatas = ['这个软件可以帮助你计算重庆邮电大学教务在线成绩总表中各种性质的课程的学分\n','\n首先需要您将教务在线上成绩总表中除开B学分的内容复制到excel表中（.xlsx）\n',
        '\n该版本不具有联网功能。\n','\n点击菜单栏open打开保存的excel文件，点击开始得到相应结果，点击保存将结果保存为txt文件\n','\n规定毕业需要到达的学分数：必修:60;限选:54;任选:6;实践:40。']
        self.help_listBox = wx.ListBox(self.dialog_main_help, -1, pos=(20, 20), size=(5500, 400), choices=listDatas, style=wx.LB_SINGLE)
        #self.help_listBox.SetFont(self.textFont)
        
        """显示子窗口"""
        self.dialog_main_help.ShowModal()
        
    def Onopen(self,event):
        self.statusbar.SetStatusText("点击'Open'菜单，导入需要计算学分的excel文件（.xlsx）",1)
        self.text_contents.Clear()
        #print('hello')
        with wx.FileDialog(self,"Open file",wildcard="Text files (*.xlsx)|*.xlsx|(*.xls)|*.xls",style=wx.FD_OPEN|wx.FD_FILE_MUST_EXIST) as fileDialog:
            if fileDialog.ShowModal()==wx.ID_OK:
                pathname_open=fileDialog.GetPath()
                #print(pathname_open)
                self.text_contents.SetValue('\n\n\n\n\n\t\t\t\t现在点击“开始“按钮计算各项学分')
                """使用open读入文件，AppendText将列表中所有字符都显示出来，而SetValue是逐行显示
                最终只显示列表中的最后一个字符"""
                """
                fp=open(pathname_open,'r')
                tempstr=fp.readlines()
                print(tempstr)
                for line in tempstr:
                    self.text_contents.AppendText(line)
                """
                global Path
                Path=pathname_open
                #print(Path)
                self.text_name.SetValue(Path)
    def Onbegin(self,event):
        self.statusbar.SetStatusText("点击'开始'按钮，获得当前表格中各项性质课程的学分",1)
        global Path
        path=Path
        #print(path)
        OF=Openfile(path)
        of=OF.contents_of_file()
        compulsory,limited_selection,optional,practice=of[0],of[1],of[2],of[3]
        """计算"""
        cc1=CountContents(compulsory)
        print('必修学分总数：\n',str(cc1.tempcount()))
        c1=str(cc1.tempcount())
        cc1=CountContents(limited_selection)
        print('限选学分总数：\n',str(cc1.tempcount()))
        c2=str(cc1.tempcount())
        cc1=CountContents(optional)
        print('任选学分总数：\n',str(cc1.tempcount()))
        c3=str(cc1.tempcount())
        cc1=CountContents(practice)
        print('实践学分总数：\n',str(cc1.tempcount()))
        c4=str(cc1.tempcount())
        a="下面是各项学分：\n\t必修学分总数：\n\t"
        a1="\n\t限选学分总数：\n\t"
        a2="\n\t任选学分总数：\n\t"
        a3="\n\t实践学分总数：\n\t"
        a4=a+c1+a1+c2+a2+c3+a3+c4
        self.text_contents.SetValue(a4)
        self.text_update.SetValue(str(a4))
        self.text_update.GetValue(a4)
    def Onsave(self,event):
        self.statusbar.SetStatusText("点击'保存'按钮，将各项性质的课程的学分保存为txt文件",1)
        with wx.FileDialog(self,"Save file",wildcard="Text file (*.txt)|*.txt",style=wx.FD_SAVE) as fileDialog:
            if fileDialog.ShowModal()==wx.ID_OK:
                pathname=fileDialog.GetPath()
                fp=open(pathname,'w')
                number1=self.text_update.GetNumberOfLines()
                for i in range(number1):
                    v=self.text_update.GetLineText(i)
                    fp.write(v)
                    fp.write("\n")#换行
                fp.close()#关闭文件
        
        
app=wx.App()
win=MyFrame()
win.Show()
app.MainLoop()
