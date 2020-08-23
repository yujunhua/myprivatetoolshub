#include <winsock2.h>
#include <stdio.h>
#include <Ws2tcpip.h>
#pragma comment(lib, "ws2_32.lib")
void main()
{
	//初始化套接字
	WORD wVersionRequested;
	WSADATA wsaData;
	wVersionRequested = MAKEWORD(2, 2);	
	WSAStartup(wVersionRequested, &wsaData);

	 //创建套接字
	SOCKET socSrv = socket(AF_INET, SOCK_STREAM, 0);

	//绑定套接字
	SOCKADDR_IN addrSrv;
	addrSrv.sin_addr.S_un.S_addr = htonl(INADDR_ANY);//转换Unsigned long型为网络字节序格式
	addrSrv.sin_family = AF_INET;//指定地址簇
	addrSrv.sin_port = htons(6000);
	bind(socSrv, (SOCKADDR*)&addrSrv, sizeof(SOCKADDR));

	//监听套接字
	listen(socSrv, 5);//等待连接的最大队列长度是5
	SOCKADDR_IN addrClient;
	int len = sizeof(SOCKADDR);

	//此时程序在此发生阻塞
	SOCKET sockConn = accept(socSrv, (SOCKADDR*)&addrClient, &len);


	char sendBuf[100] = { 0 };
	char recvBuf[100] = { 0 };//初始化为0，则下面发送的时候strlen 就不需要加1
	while (1)
	{
		//清空原有数据
		memset(sendBuf, 0, sizeof(sendBuf));
		gets_s(sendBuf);
		if (sendBuf[0] == '0')
			break;

		//char IPdotdec[10];
		//sprintf_s(sendBuf, "Welcome %s to Mars",
		//	inet_ntop(AF_INET, &addrClient.sin_addr, IPdotdec,10));//格式化输出

		//用返回的套接字和客户端进行通信
		send(sockConn, sendBuf, strlen(sendBuf), 0);

		//清空原有数据
		memset(recvBuf, 0, sizeof(recvBuf));
		//接收数据
		recv(sockConn, recvBuf, 100, 0);
		printf("%s\n", recvBuf);
		
	}
	closesocket(sockConn);
	printf("server close\n");
	WSACleanup();
}