/*
csharp实现的一个控制台的，多线程的，tcp的网络聊天程序
学习资源：
http://www.cnblogs.com/haosit/p/6813583.html
https://stackoverflow.com/questions/1337073/net-c-sharp-socket-concurrency-issues
https://docs.microsoft.com/zh-cn/dotnet/csharp/
https://docs.microsoft.com/en-us/dotnet/csharp/
开发平台及工具：win10 pro x64 + vs2017 community
编译选项：.net framework 4
将要实现的：
使用锁进行线程同步
使用winforms编写GUI接口
*/
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

using System.Net;
using System.Net.Sockets;
using System.Threading;

namespace ConsoleApp1
{
    class Program
    {
        static void Main(string[] args)
        {
            ServerSocket.CreateSocket();
        }
    }

    class ServerSocket
    {
        public static void SendMessage(object o)
        {
            Socket s = o as Socket;
            while (true)
            {
                // send message
                string str = Console.ReadLine();
                if (str == "")
                {
                    break;
                }
                byte[] send_bytes = Encoding.UTF8.GetBytes(str);
                s.Send(send_bytes);
            }
        }

        public static void ReceiveMessage(object o)
        {
            Socket s = o as Socket;
            string id = s.RemoteEndPoint.ToString();
            while (true)
            {
                // receive message
                byte[] bytes_recv = new byte[1024 * 1024 * 2];
                int effective = s.Receive(bytes_recv);
                String str = Encoding.UTF8.GetString(bytes_recv, 0, effective);
                Console.WriteLine("Client{0} say: {1}", id, str);
            }
        }

        public static void CreateSocket()
        {
            // basic defination
            IPAddress ip = IPAddress.Parse("127.0.0.1");
            IPEndPoint ipe = new IPEndPoint(ip, 2000);

            // creat socket
            Socket s = new Socket(AddressFamily.InterNetwork, SocketType.Stream, ProtocolType.Tcp);
            s.Bind(ipe);
            s.Listen(2);

            // listen connection
            while (true)
            {
                Socket s0 = s.Accept();
                string sendIpoint = s0.RemoteEndPoint.ToString(); // get client ip address
                Console.WriteLine($"Connection from {sendIpoint}");

                Thread thread_recv = new Thread(ReceiveMessage);
                thread_recv.Start(s0);

                Thread thread_send = new Thread(SendMessage);
                thread_send.Start(s0);

            }
        }
    }
}
