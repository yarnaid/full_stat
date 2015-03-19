import wx
import sys
from random import random


########################################################################
class ListCtrl(wx.ListCtrl, wx.lib.mixins.listctrl.ListCtrlAutoWidthMixin):
    """List class for data table"""

    #----------------------------------------------------------------------
    def __init__(self, parent, ID, pos=wx.DefaultPosition,
                 size=wx.DefaultSize, style=0):
        wx.ListCtrl.__init__(self, parent, ID, pos, size, style)
        listmix.ListCtrlAutoWidthMixin.__init__(self)
        
    
########################################################################
class DataTable(wx.Panel, wx.lib.mixins.listctrl.ColumnSorterMixin):
    """Table for view and editing data"""

    #----------------------------------------------------------------------
    def __init__(self, *args, **kwargs):
        """Constructor"""
        wx.Panel.__init__(*args, **kwargs)
        
        self.create_and_layout()
        
    
    def create_and_layout(self):
        sizer = wx.BoxSizer(orient=wx.VERTICAL)
        self.list = ListCtrl(self, wx.ID_ANY, style=wx.LC_REPORT
                             |wx.BORDER_NONE
                             |wx.LC_EDIT_LABELS
                             |wx.LC_SORT_ASCENDING)
        
        sizer.Add(self.list, 1, wx.EXPAND)
        
        self.populate_list()
        
        self.item_data_map = None
        
        cols_number = 3
        wx.lib.mixins.listctrl.ColumnSorterMixin.__init__(self, cols_number)
        
        self.SetSizer(sizer)
        self.SetAutoLayout(True)
        
        
    def populate_list(self):
        
        cols = ['x', 'y', 'err']
        cols_num = len(cols)
        
        for i, col in enumerate(cols):
            self.list.InsertColumn(i, col, wx.LIST_FORMAT_RIGHT)
            
        data = dict([(i, (i, random(), random(), random())) for i in xrange(10)])
        
        for key, value in data.items():
            index = self.list.InsertItem(sys.maxint, value[0])
            for i in xrange(1, cols_num):
                self.list.InsertItem(index, i, value[i])
        
        
        
        raise NotImplementedError
    