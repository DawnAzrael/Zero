using System;
using System.Collections.Generic;
using System.Configuration;
using System.Data;
using System.Linq;
using System.Threading.Tasks;
using System.Windows;

namespace 音迷
{
    /// <summary>
    /// App.xaml 的交互逻辑
    /// </summary>
    public partial class App : Application
    {
        App()
        {
            System.Threading.Thread.Sleep(5000);
        }
        protected override void OnStartup(StartupEventArgs e)
        {
            SplashScreen s = new SplashScreen("resource/startup.jpg");
            // 显示初始屏幕 自动关闭设置false
            s.Show(false);
            // 2秒后关闭
            s.Close(new TimeSpan(0, 0, 2));
            base.OnStartup(e);
        }
    }
}
