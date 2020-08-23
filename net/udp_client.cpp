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
	SOCKET sockClient = socket(AF_INET, SOCK_DGRAM, 0);

	SOCKADDR_IN addrSrv;
	struct in_addr addr;
	inet_pton(AF_INET, "127.0.0.1", (void*)&addr);
	addrSrv.sin_addr.S_un.S_addr = addr.s_addr;
	addrSrv.sin_family = AF_INET;
	addrSrv.sin_port = htons(6000);

	int len = sizeof(SOCKADDR);
	char sendBuff[100] = { 0 };
	while (1)
	{
		//清除原有数据
		memset(sendBuff, 0, sizeof(sendBuff));
		gets_s(sendBuff);
		sendto(sockClient, sendBuff, strlen(sendBuff),
			0, (SOCKADDR*)&addrSrv, len);
	}

	closesocket(sockClient);
	WSACleanup();
}