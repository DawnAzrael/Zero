using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Data;
using System.Windows.Documents;
using System.Windows.Input;
using System.Windows.Media;
using System.Windows.Media.Imaging;
using System.Windows.Navigation;
using System.Windows.Shapes;
using System.Data;
using MySql.Data.MySqlClient;
using System.Diagnostics;
using Microsoft.Win32;
using Renci.SshNet;

namespace 音迷
{
    /// <summary>
    /// MainWindow.xaml 的交互逻辑
    /// </summary>
    public partial class MainWindow : Window
    {
        // SQL 
        Random rd = new Random();
        //string sqlstr = "Data Source=192.168.1.5;User ID=zero;Password=Azrael.134;DataBase=RecommendRes;Charset=utf8;";
        private string sqlstr = "Server=192.168.199.201;Database=RecommendRes;Uid=zero;Pwd=Azrael.134;";
        MySql.Data.MySqlClient.MySqlConnection con;
        MySql.Data.MySqlClient.MySqlConnection con1;
        MySql.Data.MySqlClient.MySqlConnection con2;
        MySql.Data.MySqlClient.MySqlConnection con3;
        MySql.Data.MySqlClient.MySqlDataAdapter adapter;
        MySql.Data.MySqlClient.MySqlDataAdapter adapter1;
        MySql.Data.MySqlClient.MySqlDataAdapter adapter2;
        MySql.Data.MySqlClient.MySqlDataAdapter adapter3;
        System.Data.DataSet ds;
        System.Data.DataTable dt;
        System.Data.DataSet ds1;
        System.Data.DataTable dt1;
        System.Data.DataSet ds2;
        System.Data.DataTable dt2;
        System.Data.DataSet ds3;
        System.Data.DataTable dt3;

        private void UpdateMySQLData()
        {
            try
            {
                if (con == null)
                {
                    con = new MySql.Data.MySqlClient.MySqlConnection(sqlstr);
                    con.Open();
                }
                if (adapter == null)
                {
                    adapter = new MySql.Data.MySqlClient.MySqlDataAdapter("select * from QQHotList", con);
                }
                if (ds == null)
                {
                    ds = new System.Data.DataSet();
                }
                ds.Clear();
                adapter.Fill(ds, "QQHotList");
                if (dt == null)
                {
                    dt = ds.Tables["QQHotList"];
                }
                Mic_List.ItemsSource = dt.DefaultView;
                con.Close();
            }
            catch
            {
                MessageBox.Show("歌单获取失败，请重新启动……");
            }
        }
        public MainWindow()
        {                       
            InitializeComponent();
            WindowStartupLocation = WindowStartupLocation.CenterScreen;
            UpdateMySQLData();
        }

        private void DataGridHyperlinkColumn_Click(object sender, RoutedEventArgs e)
        {
            try
            {
                Uri destination = ((Hyperlink)e.OriginalSource).NavigateUri;
                string final_destination = destination.ToString();
                System.Diagnostics.Process.Start(final_destination);
            }
            catch
            {
                MessageBox.Show("错误代码201");
            }
        }

        public static void RunPythonScript(string sArgName, string args = "", params string[] teps) // python文件名.py 参数
        {
            Process p = new Process();
            string path = System.AppDomain.CurrentDomain.SetupInformation.ApplicationBase + sArgName;// 获得python文件的绝对路径（将文件放在c#的debug文件夹中可以这样操作）
            path = @"E:\PersonalCode\VS2019-WPF\音迷\音迷\resource\" + sArgName;//(因为我没放debug下，所以直接写的绝对路径,替换掉上面的路径了)
            p.StartInfo.FileName = @"E:\DPKG\Python3.7\python.exe";//没有配环境变量的话，可以像我这样写python.exe的绝对路径。如果配了，直接写"python.exe"即可
            string sArguments = path;
            foreach (string sigstr in teps)
            {
                sArguments += " " + sigstr;//传递参数
            }

            sArguments += " " + args;
            p.StartInfo.Arguments = sArguments;
            p.StartInfo.UseShellExecute = false;
            p.StartInfo.RedirectStandardOutput = true;
            p.StartInfo.RedirectStandardInput = true;
            p.StartInfo.RedirectStandardError = true;
            p.StartInfo.CreateNoWindow = true;
            p.Start();
            p.BeginOutputReadLine();
            Console.ReadLine();
            p.WaitForExit();
        }

        
        public delegate void AppendTextCallback(string text);
        

        private void Sychro_songlist_Click(object sender, RoutedEventArgs e)
        {
            try
            {
                // SELECT song_name, singer, link FROM xiami244467287
                // 先 python
                string[] strArr = new string[1];//参数列表
                string sArguments = @"xiami.py";//这里是python的文件名字
                strArr[0] = xiami_userid.Text; // 244467287
                RunPythonScript(sArguments, "-u", strArr);
                // 然后 db // 再然后 show
                string sychro_sql = "SELECT song_name, singer, link FROM xiami" + xiami_userid.Text;
                con1 = null;
                if (con1 == null)
                {
                    con1 = new MySql.Data.MySqlClient.MySqlConnection(sqlstr);
                    con1.Open();
                }
                adapter1 = null;
                if (adapter1 == null)
                {
                    adapter1 = new MySql.Data.MySqlClient.MySqlDataAdapter(sychro_sql, con1);
                }
                ds1 = null;
                if (ds1 == null)
                {
                    ds1 = new System.Data.DataSet();
                }
                ds1.Clear();
                adapter1.Fill(ds1, "xiami");
                dt1 = null;
                if (dt1 == null)
                {
                    dt1 = ds1.Tables["xiami"];
                }
                Music_World.ItemsSource = dt1.DefaultView;
                con1.Close();
                if (dt1.DefaultView.Count == 0)
                {
                    MessageBox.Show("查询无结果，请检查您的输入！");
                }
            }
            catch
            {
                MessageBox.Show("查询无结果，请检查您的输入！");
            }
        }

        private void Xiami_music_search_Click(object sender, RoutedEventArgs e)
        {
            string url1 = "https://www.xiami.com/search?key=" + music_search_name.Text;
            System.Diagnostics.Process.Start(url1);
        }
        private void Qq_music_search_Click(object sender, RoutedEventArgs e)
        {
            string url2 = "https://y.qq.com/portal/search.html#page=1&searchid=1&remoteplace=txt.yqq.top&t=song&w=" + music_search_name.Text;
            System.Diagnostics.Process.Start(url2);
        }
        private void Netease_music_search_Click(object sender, RoutedEventArgs e)
        {
            string url3 = "https://music.163.com/#/search/m/?s=" + music_search_name.Text;
            System.Diagnostics.Process.Start(url3);
        }
        private void Kuwo_music_search_Click(object sender, RoutedEventArgs e)
        {
            string url4 = "http://sou.kuwo.cn/ws/NSearch?type=all&catalog=yueku20177&key=" + music_search_name.Text;
            System.Diagnostics.Process.Start(url4);            
        }
        private void Kugou_music_search_Click(object sender, RoutedEventArgs e)
        {
            string url5 = "https://www.kugou.com/yy/html/search.html#searchType=song&searchKeyWord=" + music_search_name.Text;
            System.Diagnostics.Process.Start(url5);
        }
        private void Qianqian_music_search_Click(object sender, RoutedEventArgs e)
        {
            string url6 = "http://music.taihe.com/search?key=" + music_search_name.Text;
            System.Diagnostics.Process.Start(url6);            
        }
        private void Migu_music_search_Click(object sender, RoutedEventArgs e)
        {
            string url7 = "http://music.migu.cn/v3/search?keyword=" + music_search_name.Text;
            System.Diagnostics.Process.Start(url7);
        }
        private void todayRecomend()
        {
            try
            {
                string rec_sql = "SELECT songname, singer, link FROM RecommendRes.todayrecommend;";
                con3 = null;
                if (con3 == null)
                {
                    con3 = new MySql.Data.MySqlClient.MySqlConnection(sqlstr);
                    con3.Open();
                }
                adapter3 = null;
                if (adapter3 == null)
                {
                    adapter3 = new MySql.Data.MySqlClient.MySqlDataAdapter(rec_sql, con3);
                }
                ds3 = null;
                if (ds3 == null)
                {
                    ds3 = new System.Data.DataSet();
                }
                ds3.Clear();
                adapter3.Fill(ds3, "rec");
                dt3 = null;
                if (dt3 == null)
                {
                    dt3 = ds3.Tables["rec"];
                }
                Music_Recommend.ItemsSource = dt3.DefaultView;

                con3.Close();
            }
            catch
            {
                MessageBox.Show("Fatal Error For Today Recoomend！");
            }
        }
        private void recommend_songlist_Click(object sender, RoutedEventArgs e)
        {
            try
            {
                using (var sshClient = new SshClient("192.168.199.201", "hadoop", "hadoop"))
                {
                    sshClient.Connect();
                    string command = "python /home/hadoop/PycharmProjects/untitled/recommend.py " + xmid.Text;
                    using (var cmd = sshClient.CreateCommand(command))
                    {
                        var res = cmd.Execute();
                        if (res == "107\n")
                        {
                            string rec_sql = "SELECT songname, singer, link FROM `" + xmid.Text + "_rec`";
                            con2 = null;
                            if (con2 == null)
                            {
                                con2 = new MySql.Data.MySqlClient.MySqlConnection(sqlstr);
                                con2.Open();
                            }
                            adapter2 = null;
                            if (adapter2 == null)
                            {
                                adapter2 = new MySql.Data.MySqlClient.MySqlDataAdapter(rec_sql, con2);
                            }
                            ds2 = null;
                            if (ds2 == null)
                            {
                                ds2 = new System.Data.DataSet();
                            }
                            ds2.Clear();
                            adapter2.Fill(ds2, "rec");
                            dt2 = null;
                            if (dt2 == null)
                            {
                                dt2 = ds2.Tables["rec"];
                            }
                            Music_Recommend.ItemsSource = dt2.DefaultView;
                            if (dt2.DefaultView.Count == 0)
                            {
                                MessageBox.Show("无推荐结果哦，试试今日推荐的音乐吧！");
                                todayRecomend();
                            }
                            con2.Close();
                            
                        }
                        else
                        {
                            MessageBox.Show("无推荐结果哦，试试今日推荐的音乐吧！");
                            todayRecomend();
                        }
                    }
                }
            }
            catch
            {
                MessageBox.Show("无推荐结果哦，试试今日推荐的音乐吧！");
                todayRecomend();
            }
        }

        private void Xiami_userid_GotFocus(object sender, RoutedEventArgs e)
        {
            xiami_userid.Text = "";
        }

        private void Xmid_GotFocus(object sender, RoutedEventArgs e)
        {
            xmid.Text = "";
        }

        private void Music_search_name_GotFocus(object sender, RoutedEventArgs e)
        {
            music_search_name.Text = "";
        }
    }
}
