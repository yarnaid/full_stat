import wx
import os

APP_EXIT = 1
_ = wx.GetTranslation


class FullStatFrame(wx.Frame):
    '''Main frame class for application'''
    
    def __init__(self, *args, **kwargs):
        super(FullStatFrame, self).__init__(*args, **kwargs)
        
        self.init_ui()
        
        
    def init_ui(self):
        
        menubar = wx.MenuBar()
        
        view_menu = wx.Menu()
        
        self.view_menu_toogle_status_bar = view_menu.Append(wx.ID_ANY,
                                                            '{}\tCtrl+Shift+S'.format(_('Toogle Status Bar')),
                                                       kind=wx.ITEM_CHECK)
        view_menu.Check(self.view_menu_toogle_status_bar.GetId(), True)
        self.Bind(wx.EVT_MENU, self.on_toggle_status_bar, self.view_menu_toogle_status_bar)
        
        file_menu = wx.Menu()
        
        file_menu_open = file_menu.Append(wx.ID_OPEN, '&{}\tCtrl+O'.format(_('Open')))
        self.Bind(wx.EVT_MENU, self.on_open, file_menu_open)
        
        file_menu_save = file_menu.Append(wx.ID_SAVE, '&{}\tCtrl+S'.format(_('Save')))
        self.Bind(wx.EVT_MENU, self.on_save, file_menu_save)

        file_menu.AppendSeparator()
        
        file_menu_quit = wx.MenuItem(file_menu, APP_EXIT, '&{}\tCtrl+Q'.format(_('Quit')))
        if os.path.exists('exti.png'):
            file_menu_quit.SetBitmap(wx.Bitmap('exit.png'))
        file_menu.AppendItem(file_menu_quit)
        self.Bind(wx.EVT_MENU, self.on_quit, file_menu_quit)
        
        #about_menu_item = wx.MenuItem(None, id=wx.ID_ABOUT, text='About')
        
        menubar.Append(file_menu, '&{}'.format(_('File')))
        menubar.Append(view_menu, '&{}'.format(_('View')))
        #menubar.Append(about_menu_item, 'About')
        
        self.SetMenuBar(menubar)
        
        self.status_bar = self.CreateStatusBar()
        self.status_bar.SetStatusText(_('Ready'))
        
        self.Bind(wx.EVT_RIGHT_DOWN, self.on_right_down)
        
        data_sheet = None
        table_tab = wx.Panel(..., wx.ID_ANY)
        
        
        main_sizer = wx.BoxSizer(orient=wx.HORIZONTAL)
        left_sizer = wx.BoxSizer(orient=wx.VERTICAL)
        right_sizer = wx.BoxSizer(orient=wx.VERTICAL)
        
        main_sizer.Add(left_sizer)
        main_sizer.Add(right_sizer)
        
        self.Show()
        self.Center()
        
    def on_save(self, e):
        raise NotImplementedError
        
        
    def on_right_down(self, e):
        self.PopupMenu(ContextMenu(self), e.GetPosition())
        
        
    def on_quit(self, e):
        self.Close()
        
    
    def on_open(self, e):
        raise NotImplementedError
    
    def on_toggle_status_bar(self, e):
        if self.view_menu_toogle_status_bar.IsChecked():
            self.status_bar.Show()
        else:
            self.status_bar.Hide()


########################################################################
class ContextMenu(wx.Menu):
    """Context menu of application"""

    #----------------------------------------------------------------------
    def __init__(self, parent, *args, **kwargs):
        """Constructor"""
        
        super(ContextMenu, self).__init__(*args, **kwargs)
    
        self.parent = parent
        
        minimize_item = wx.MenuItem(self, wx.NewId(), 'Minimize')
        self.AppendItem(minimize_item)
        self.Bind(wx.EVT_MENU, self.on_minimize, minimize_item)
    
    
    def on_minimize(self, e):
        self.parent.Iconize()    