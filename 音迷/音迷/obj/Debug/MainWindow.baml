   M S B A M L   `   `   `  ����A  =音迷, Version=1.0.0.0, Culture=neutral, PublicKeyToken=nullclr-namespace:音迷音迷  5   	       音迷.MainWindow   5   	   W SPresentationCore, Version=4.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35R NWindowsBase, Version=4.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35\ XPresentationFramework, Version=4.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35D 9http://schemas.microsoft.com/winfx/2006/xaml/presentation    5   	   R NSystem.Xaml, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089:x,http://schemas.microsoft.com/winfx/2006/xaml     5   	   @d2http://schemas.microsoft.com/expression/blend/2008     5   	   Jmc;http://schemas.openxmlformats.org/markup-compatibility/2006     5   	   g cXceed.Wpf.AvalonDock.Themes.Aero, Version=3.5.0.0, Culture=neutral, PublicKeyToken=3e4669d2f30244f4i eXceed.Wpf.AvalonDock.Themes.VS2010, Version=3.5.0.0, Culture=neutral, PublicKeyToken=3e4669d2f30244f4h dXceed.Wpf.AvalonDock.Themes.Metro, Version=3.5.0.0, Culture=neutral, PublicKeyToken=3e4669d2f30244f4[ WXceed.Wpf.AvalonDock, Version=3.5.0.0, Culture=neutral, PublicKeyToken=3e4669d2f30244f4?avalon,http://schemas.xceed.com/wpf/xaml/avalondock     5   	   &localclr-namespace:音迷     5   	     � 
ResizeMode$  NoResize=�5   !    � Title$ 音迷-想你所想��5	   	   $	��470��6   $	��800��6&   .��5
      � .+�5   
   �� $��resource/head.jpg��6    J� RenderTransformOrigin$ 	0.5,-1.13&�6+   $��0,-27,0,322q�6M   )  #Xceed.Wpf.AvalonDock.DockingManager  5   
   -   5          Name$ dockingManager��5       $��	0,106,0,0q�68      Layout. 5      ,  &Xceed.Wpf.AvalonDock.Layout.LayoutRoot     	RootPanel. 5      -  'Xceed.Wpf.AvalonDock.Layout.LayoutPanel     Orientation$ 
Horizontal=�6%   �  �Xceed.Wpf.AvalonDock.Layout.LayoutGroup`1[[Xceed.Wpf.AvalonDock.Layout.ILayoutPanelElement, Xceed.Wpf.AvalonDock, Version=3.5.0.0, Culture=neutral, PublicKeyToken=3e4669d2f30244f4]]   Children. 5      4  .Xceed.Wpf.AvalonDock.Layout.LayoutDocumentPane  �  �Xceed.Wpf.AvalonDock.Layout.LayoutPositionableGroup`1[[Xceed.Wpf.AvalonDock.Layout.LayoutContent, Xceed.Wpf.AvalonDock, Version=3.5.0.0, Culture=neutral, PublicKeyToken=3e4669d2f30244f4]]   	DockWidth$	 789 �60   �  �Xceed.Wpf.AvalonDock.Layout.LayoutGroup`1[[Xceed.Wpf.AvalonDock.Layout.LayoutContent, Xceed.Wpf.AvalonDock, Version=3.5.0.0, Culture=neutral, PublicKeyToken=3e4669d2f30244f4]]	   Children.	 5      2  ,Xceed.Wpf.AvalonDock.Layout.LayoutAnchorable  /	  )Xceed.Wpf.AvalonDock.Layout.LayoutContent
 	  Title$
 音迷世界��62    	  Content. 5      �� .+�5   "   �� -   5         ��Name$ xiami_userid��5   *   $��23��6@    �� TextWrapping$
 Wrap=�6L   $��在此输入虾米ID��6`   $��	0,0,655,0q�6�   �� 5   "   -   5         ��Name$ sychro_songlist��5   )   $��同步歌单��6B   $��24��6Q   $��138,-23.8,531,0q�6{   &
   System.Windows.Controls.DataGrid
  5   "   -   5         
 Name$ Music_World��5   +    
  
IsReadOnly . $ 
0.139,0.45&�6R   $��	0,0,-1,-1q�6u   $	��288��6�    
  Columns 5   &   0  *System.Windows.Controls.DataGridTextColumn  5   *   ,  &System.Windows.Controls.DataGridColumn   Header$ 歌曲名称��6=      Width5  /System.Windows.Controls.DataGridLengthConverter$	 105 6K      CanUserResize .     
IsReadOnly . 1  +System.Windows.Controls.DataGridBoundColumn   Binding 6m   �� *	song_name+6�     5   *   $ 歌手��6=   $	 105 6I    .   .  6k   �� *singer+6�   5  /System.Windows.Controls.DataGridHyperlinkColumn  5   *   $ 链接��6B   $	 570 6N    .   .  6p   �� *link+   ElementStyle 5   .   �� 5   2    �� 
TargetType" ��68   .�5   6   -   5        5    3   5"   +   5$   #   5%      5&        5'      $
 热门榜单��62   . 5(      
  -   5        $ Mic_List��5(   '   $��Center=�69   $ 
0.139,0.45&�6V   $��	0,0,-1,-1q�6y   $	��380��6�    .  5)   "     5*   &   $ 歌单名称��69   $	 210 6G    .   .  6i   ��  �� Path$
 name�6�     5+   &   $ 链接��6>   $	 460 6J    .   .  6l   �� $
 link� 5,   *   �� 5-   .   " ��64   .�5.   2   -   5        50   /   52   '     53   &   $ 	播放量��69   $ 80 6F      SortDirection$ 
DescendingX�6Q    .   .  6�   �� $ 
play_count�6�   55      56        57      $
 音迷推荐��62   . 58      �� .+�59   "   �� -   5        $
 xmid��59   *   $��23��68   $
 Wrap=�6D   $��在此输入虾米ID��6X   $��	0,0,655,0q�6�   �� 5:   "   -	   5        $ recommend_songlist��5:   )   $��	音推荐��6E   $��24��6S   $��138,-23.8,531,0q�6�   
  5<   "   -
   5        $ Music_Recommend��5<   +    . $ 
0.139,0.45&�6V   $��	0,0,-1,-1q�6y   $	��288��6�    5=   &     5?   *   $ 歌曲名称��6=   $	 105 6K    .   .  6m   �� *
songname+6�     5@   *   $ 歌手��6=   $	 105 6I    .   .  6k   �� *singer+6�     5A   *   $ 链接��6B   $	 570 6N    .   .  6p   �� *link+ 5B   .   �� 5C   2   " ��68   .�5D   6   -   5        5F   3   5H   +   5J   #   5K      5L        5N      $
 音乐搜索��62   . 5O      �� .��5P   "   �� .+�5Q   &   �� -   5        $ music_search_name��5Q   .   $��23��6I   $
 Wrap=�6U   $$��在此输入歌曲名称……��6i   $��	0,0,655,0q�6�   �� 5R   &   -   5        $ xiami_music_search��5R   -   $
��Left=�6I   $��
50,0,-23,0q�6d   $	��Top=�6�   $	��123��6�   $��35��6�   ��5S   *   �� 5T   .    �� ImageSource$ /resource/xiamilogo.png��69   6a   5V   '   �� 5W   &   -   5        $ qq_music_search��5W   -   $
��Left=�6F   $��100,0,-23,0q�6a   $	��Top=�6�   $	��123��6�   $��35��6�   ��5X   *   �� 5Y   .   $ /resource/qqmusiclogo.png��69   6c   5[   '   �� 5\   &   -   5        $ netease_music_search��5\   -   $
��Left=�6K   $��150,0,-23,0q�6f   $	��Top=�6�   $	��123��6�   $��35��6�   ��5]   *   �� 5^   .   $ /resource/neteaselogo.png��69   6c   5`   '   �� 5a   &   -   5        $ kuwo_music_search��5a   -   $
��Left=�6H   $��200,0,-23,0q�6c   $	��Top=�6�   $	��123��6�   $��35��6�   ��5b   *   �� 5c   .   $ /resource/kuwologo.jpg��69   6`   5e   '   �� 5f   &   -   5        $ kugou_music_search��5f   -   $
��Left=�6I   $��250,0,-23,0q�6d   $	��Top=�6�   $	��123��6�   $��35��6�   ��5g   *   �� 5h   .   $ /resource/kugoulogo.png��69   6a   5j   '   �� 5k   &   -   5        $ qianqian_music_search��5k   -   $
��Left=�6L   $��300,0,-23,0q�6g   $	��Top=�6�   $	��123��6�   $��35��6�   ��5l   *   �� 5m   .   $  /resource/qianqianlogo.png��69   6d   5o   '   �� 5p   &   -   5        $ migu_music_search��5p   -   $
��Left=�6H   $��350,0,-23,0q�6c   $	��Top=�6�   $	��123��6�   $��35��6�   ��5q   *   �� 5r   .   $ /resource/migulogo.png��69   6`   5t   '   5u   #   5v      5w      5x      5y      5z      5{      5|      5}      