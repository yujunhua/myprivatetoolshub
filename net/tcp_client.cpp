#include <winsock2.h>
#include <stdio.h>
#include <Ws2tcpip.h>
#pragma comment(lib, "ws2_32.lib")
void main()
{
	//初始化套接字
	WORD wVersionRequested;
	WSADATA wsaData;
	wVersionRequested = MAKEWORD(2,2);
	WSAStartup(wVersionRequested, &wsaData);

	//创建套接字
	SOCKET sockClient = socket(AF_INET, SOCK_STREAM, 0);
	//Socket地址结构体的创建
	SOCKADDR_IN addrSrv;

	struct in_addr addr;
	inet_pton(AF_INET, "127.0.0.1", (void*)&addr);
	addrSrv.sin_addr.S_un.S_addr = addr.s_addr;
	addrSrv.sin_family = AF_INET;//指定地址簇
	addrSrv.sin_port = htons(6000);


	connect(sockClient, (SOCKADDR*)&addrSrv, sizeof(SOCKADDR));

	char recvBuf[100] = { 0 };//初始化为0，则下面发送的时候strlen 就不需要加1
	char sendBuf[100] = { 0 };
	while (1)
	{
		//清空原有数据
		memset(recvBuf, 0, sizeof(recvBuf));
		recv(sockClient, recvBuf, 100, 0);

		printf("%s\n", recvBuf);

		//清空原有数据
		memset(sendBuf, 0, sizeof(sendBuf));
		gets_s(sendBuf);

		send(sockClient, sendBuf, strlen(sendBuf), 0);

	}
	//关闭套接字。
	closesocket(sockClient);
	printf("client close\n");
	WSACleanup();//必须调用这个函数清除参数
}