#include <winsock2.h>
#include <stdio.h>
#pragma comment(lib, "ws2_32.lib")

//����UDP��֧�׽��ַ���������
void main() 
{
	//��ʼ���׽���
	WORD wVersionRequested;
	WSADATA wsaData;
	wVersionRequested = MAKEWORD(2, 2);
	WSAStartup(wVersionRequested, &wsaData);

	//�����׽���
	SOCKET sockSrv = socket(AF_INET, SOCK_DGRAM, 0);//��������(socket)

	//���׽���
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