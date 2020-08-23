#include <winsock2.h>
#include <stdio.h>
#pragma comment(lib, "ws2_32.lib")

//基于UDP开支套接字服务器程序
void main() 
{
	//初始化套接字
	WORD wVersionRequested;
	WSADATA wsaData;
	wVersionRequested = MAKEWORD(2, 2);
	WSAStartup(wVersionRequested, &wsaData);

	//创建套接字
	SOCKET sockSrv = socket(AF_INET, SOCK_DGRAM, 0);//创建套字(socket)

	//绑定套接字
	SOCKADDR_IN addSrv;
	addSrv.sin_addr.S_un.S_addr = htonl(INADDR_ANY);
	addSrv.sin_family = AF_INET;
	addSrv.sin_port = htons(6000);
	bind(sockSrv, (SOCKADDR*)&addSrv, sizeof(SOCKADDR));


	SOCKADDR_IN addrClient;
	int len = sizeof(SOCKADDR);
	char recvBuf[100] = {0};
	while (1)
	{
		memset(recvBuf, 0, sizeof(recvBuf));
		recvfrom(sockSrv, recvBuf, 100, 0,
			(SOCKADDR*)&addrClient, &len);
		printf("%s\n", recvBuf);
	}

	closesocket(sockSrv);
	WSACleanup();

}